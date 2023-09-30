import pygame
import sys
from mastermind import Colors
from mastermind import Match
from mastermind import MasterMindGame

globals().update( Colors.__members__)
globals().update( Match.__members__)

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create a dictionary to map Colors Enum to RGB values
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
    BROWN: (139, 69, 19),
    SKY_BLUE: (135, 206, 235)
}

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("MasterMind Game")

# Fonts
font = pygame.font.Font(None, 36)

# Initialize the game
game = MasterMindGame()

def draw_text(text, x, y, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def draw_colors():
    x = 100
    y = 100
    color_radius = 30

    for color in Colors:
        pygame.draw.circle(screen, COLOR_MAP[color], (x, y), color_radius)
        x += 2 * color_radius + 20

def main():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        draw_text("MasterMind Game", 20, 20, BLACK)
        draw_colors()

        if game.is_game_over():
            draw_text("Game Over!", 20, 200, RED)
            draw_text(f"The secret code was: {', '.join([str(color) for color in game.selected_colors])}", 20, 240, BLACK)
        else:
            draw_text(f"Tries Remaining: {game.MAX_TRIES}", 20, 200, BLACK)
            draw_text("Enter your guess (e.g., red blue green):", 20, 260, BLACK)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
