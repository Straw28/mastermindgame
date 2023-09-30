import pygame
import sys
from mastermind import Colors
from mastermind import Match
from mastermind import MasterMindGame

globals().update( Colors.__members__)
globals().update( Match.__members__)

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

QUIT_BUTTON_RECT = pygame.Rect(600, 500, 150, 50)

COLORS_LIST = [YELLOW, RED, GREEN, ORANGE, CYAN, PINK, VIOLET, BLUE, TEAL, MAGENTA]

COLOR_MAP = {
    YELLOW: (255, 255, 0),
    RED: (255, 0, 0),
    GREEN: (0, 255, 0),
    ORANGE: (255, 165, 0),
    CYAN: (0, 255, 255),
    PINK: (255, 182, 193),
    VIOLET: (148, 0, 211),
    BLUE: (0, 0, 255),
    TEAL: (0, 128, 128),
    MAGENTA: (255, 0, 255),
}

COLOR_COORDINATES = [
   
        (45, 500),
        (45, 550),
    
        (125, 500),
        (205, 500),
        (285, 500),
    
        (125, 550),
        (205, 550),
        (285, 550),
        
        (365, 500),
        (365, 550),

]


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("MasterMind Game")

font = pygame.font.Font(None, 36)

game = MasterMindGame()

def draw_text(text, x, y, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def draw_colors():
    color_radius = 20
    for row in range(len(COLOR_COORDINATES)):
        pygame.draw.circle(screen, COLOR_MAP[COLORS_LIST[row]], COLOR_COORDINATES[row], color_radius)
                

def handle_quit_button_click(mouse_pos):
    if QUIT_BUTTON_RECT.collidepoint(mouse_pos):
        pygame.quit()
        sys.exit()

def main(running):
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                handle_quit_button_click(mouse_pos)

        screen.fill(WHITE)
        draw_colors()

        if game.is_game_over():
            draw_text("Game Over!", 20, 200, COLOR_MAP[RED])
            draw_text(f"The secret code was: {', '.join([str(color) for color in game.selected_colors])}", 20, 240, BLACK)
        else:
            draw_text(f"Tries Remaining: {game.MAX_TRIES}", 20, 200, BLACK)
            draw_text("Click your guess (e.g., red blue green):", 20, 260, BLACK)

        pygame.draw.rect(screen, COLOR_MAP[RED], QUIT_BUTTON_RECT)
        draw_text("Quit", QUIT_BUTTON_RECT.x + 25, QUIT_BUTTON_RECT.y + 10, WHITE)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main(True)
