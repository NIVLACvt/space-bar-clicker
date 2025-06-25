import pygame
import time
from time import sleep

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

def draw_screen():
    screen.fill((0, 0, 0))
    for x in one:
        pygame.draw.rect(screen, TEEL, [x[0], x[1], space_width, space_height])
        screen.blit(text_surface, text_rect)
    score_surface = score_font.render(f'Score: {score}', True, (255, 255, 255))
    score_rect = score_surface.get_rect(center=(WIDTH // 2, one[0][1] - 30))
    screen.blit(score_surface, score_rect)
    pygame.display.update()

draw_screen()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                score += 1
                draw_screen()
pygame.quit()