import pygame
import time
from time import sleep
import os
# These environment variables tell Pygame to run in headless mode
os.environ["SDL_VIDEODRIVER"] = "dummy"
os.environ["SDL_AUDIODRIVER"] = "dummy"

WIDTH = 800
HEIGHT = 600
TEEL = (0, 170, 120)
space_width = 700
space_height = 200
score = 0
one = [(50, 50)]

pygame.init()
font = pygame.font.SysFont(None, 72)
score_font = pygame.font.SysFont(None, 48)
text_surface = font.render('space bar', True, (0, 0, 0))
text_rect = text_surface.get_rect()
# Center the text in the box
text_rect.center = (one[0][0] + space_width // 2, one[0][1] + space_height // 2)

width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
screen = pygame.display.set_mode((800, 600))

popped = False
pop_start = 0

def draw_screen(pop=False):
    screen.fill((0, 0, 0))
    # Recalculate text and box position to keep centered
    w = space_width + 10 if pop else space_width
    h = space_height + 10 if pop else space_height
    x = (WIDTH - w) // 2
    y = (HEIGHT - h) // 2
    one[0] = (x, y)
    # Use a bigger font for the pop effect
    font_size = 90 if pop else 72
    font_dynamic = pygame.font.SysFont(None, font_size)
    text_surface_dynamic = font_dynamic.render('space bar', True, (0, 0, 0))
    text_rect_dynamic = text_surface_dynamic.get_rect()
    text_rect_dynamic.center = (x + w // 2, y + h // 2)
    for x1 in one:
        pygame.draw.rect(screen, TEEL, [x1[0], x1[1], w, h])
        screen.blit(text_surface_dynamic, text_rect_dynamic)
    score_surface = score_font.render(f'Score: {score}', True, (255, 255, 255))
    score_rect = score_surface.get_rect(center=(WIDTH // 2, one[0][1] - 30))
    screen.blit(score_surface, score_rect)
    pygame.display.update()

draw_screen()
running = True
popped = False
pop_start = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE and not popped:
                score += 1
                popped = True
                pop_start = pygame.time.get_ticks()
                draw_screen(pop=True)
    if popped and pygame.time.get_ticks() - pop_start > 100:
        popped = False
        draw_screen(pop=False)
pygame.quit()
