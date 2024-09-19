import pygame
import time
from config import *
from algorithms.algorithms import *

pygame.init()

FONT = pygame.font.SysFont('comicsans', 25)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Algorithm Visualizer")

main_surface = pygame.Surface((WIDTH * 0.7, HEIGHT * 0.7))
config_surface = pygame.Surface((WIDTH * 0.3, HEIGHT))
description_surface = pygame.Surface((WIDTH * 0.7, HEIGHT * 0.3))

def main():
    running = True
    clock = pygame.time.Clock()
    algorithms = [BubbleSort(), QuickSort(), LinearSearchAlgorithm(), DivideAndConquerAlgorithm()]  # Add more algorithms here
    current_algo = 0
    algorithms[current_algo].generate_dataset()
    algorithms[current_algo].set_font(FONT)
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if algorithms[current_algo].is_resolved():
                        algorithms[current_algo].generate_dataset()
                    algorithms[current_algo].execute(main_surface, WIN)
                if event.key == pygame.K_RIGHT:
                    algorithms[current_algo].generate_dataset()
                    current_algo = (current_algo + 1) % len(algorithms)
                    algorithms[current_algo].set_font(FONT)
                if event.key == pygame.K_LEFT:
                    algorithms[current_algo].generate_dataset()
                    current_algo = (current_algo - 1) % len(algorithms)
                    algorithms[current_algo].set_font(FONT)
                if event.key == pygame.K_LSHIFT:
                    algorithms[current_algo].slow_mo_speed_up()
                if event.key == pygame.K_g:
                    algorithms[current_algo].generate_dataset()

        algorithms[current_algo].draw(main_surface, [BLACK] * len(algorithms[current_algo].data_set))
        config_surface.fill(GREEN)
        description_surface.fill(BLUE)

        title = FONT.render(algorithms[current_algo].title(), 1, BLACK)
        description_surface.blit(title, (config_surface.get_width() // 2, 10))
        y = 15
        for param, value in algorithms[current_algo].params().items():
            text = FONT.render(f"{param}: {value}", True, BLACK)
            config_surface.blit(text, (10, y))
            y += 30

        # Draw on description surface
        description_text = FONT.render(algorithms[current_algo].description, True, BLACK)
        description_surface.blit(description_text, (10, 25))

        # Blit all surfaces to the main window
        WIN.blit(main_surface, (0, 0))
        WIN.blit(config_surface, (WIDTH - WIDTH * 0.3, 0))
        WIN.blit(description_surface, (0, HEIGHT - HEIGHT * 0.3))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()