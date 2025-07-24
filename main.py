import asyncio
import pygame

# Try to declare all your globals at once to facilitate compilation later.
global score
WIDTH, HEIGHT = 800, 600
TEAL = (0, 170, 120)
space_width, space_height = 700, 200
score = 0
one = [(50, 50)]


# Do init here
# Load any assets right now to avoid lag at runtime or network errors.

pygame.init()

try:
    font = pygame.font.Font(None, 72)  # None uses pygame's default font
    score_font = pygame.font.Font(None, 48)
except:
    # Fallback if font initialization fails
    font = pygame.font.Font(None, 72)
    score_font = pygame.font.Font(None, 48)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Bar Clicker")

def draw_screen(pop=False):
    screen.fill((0, 0, 0))
    
    # Calculate box dimensions
    w = space_width + 10 if pop else space_width
    h = space_height + 10 if pop else space_height
    x = (WIDTH - w) // 2
    y = (HEIGHT - h) // 2
    one[0] = (x, y)
    
    # Dynamic font for pop effect
    font_size = 90 if pop else 72
    try:
        dynamic_font = pygame.font.Font(None, font_size)
    except:
        dynamic_font = font  # Fallback to main font
    
    # Render text
    text_surface = dynamic_font.render('space bar', True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(x + w//2, y + h//2))
    
    # Draw elements
    pygame.draw.rect(screen, TEAL, [x, y, w, h])
    screen.blit(text_surface, text_rect)
    
    # Score display
    score_text = score_font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, y - 40))
    
    pygame.display.update()
    
async def main():
    global score
    running = True
    popped = False
    pop_start = 0
    while running:

        # Do your rendering here, note that it's NOT an infinite loop,
        # and it is fired only when VSYNC occurs
        # Usually 1/60 or more times per seconds on desktop
        # could be less on some mobile devices
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE and not popped:
                    score += 1
                    popped = True
                    pop_start = pygame.time.get_ticks()
                    draw_screen(pop=True)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not popped:
                score += 1
                popped = True
                pop_start = pygame.time.get_ticks()
                draw_screen(pop=True)
        if popped and pygame.time.get_ticks() - pop_start > 100:
            popped = False
            draw_screen(pop=False)
        # pygame.display.update() should go right next line

        await asyncio.sleep(0)  # Very important, and keep it 0

# This is the program entry point:
asyncio.run(main())

# Do not add anything from here, especially sys.exit/pygame.quit
# asyncio.run is non-blocking on pygame-wasm and code would be executed
# right before program start main()
