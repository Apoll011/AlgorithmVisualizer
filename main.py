import pygame
from config import *
from algorithms.algorithms import *

pygame.init()

FONT = pygame.font.SysFont('comicsans', 30)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Algorithm Visualizer")

def main():
    running = True
    clock = pygame.time.Clock()
    algorithms = [BubbleSort(), QuickSort(), LinearSearchAlgorithm()]  # Add more algorithms here
    current_algo = 0
    algorithms[current_algo].generate_dataset(50)
    algorithms[current_algo].set_font(FONT)
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    algorithms[current_algo].generate_dataset(50)
                    algorithms[current_algo].run(WIN)
                if event.key == pygame.K_RIGHT:
                    current_algo = (current_algo + 1) % len(algorithms)
                    algorithms[current_algo].set_font(FONT)
                    algorithms[current_algo].generate_dataset(50)
                if event.key == pygame.K_LSHIFT:
                    algorithms[current_algo].slow_mo_speed_up()

        algorithms[current_algo].draw(WIN, [BLACK] * len(algorithms[current_algo].data_set))

    pygame.quit()

if __name__ == "__main__":
    main()