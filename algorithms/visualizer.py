import pygame
from pygame.event import Event

from algorithms.algorithm import Algorithm
from algorithms.constructor import Constructor
from config import *

class AlgorithmVisualizer:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('comicsans', 25)

        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Algorithm Visualizer")

        self.main_surface = pygame.Surface((WIDTH * 0.69, HEIGHT * 0.7))
        self.config_surface = pygame.Surface((WIDTH * 0.3, HEIGHT))
        self.description_surface = pygame.Surface((WIDTH * 0.69, HEIGHT * 0.28))

        self.algorithms: list[Algorithm] = []
        self.current_algo = 0

        self.running = True

    def get_algorithms(self, path):
        constructor = Constructor(path)
        self.algorithms = constructor.algorithms

    def events(self, event: Event):
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.current.is_resolved():
                    self.current.generate_dataset()
                self.current.execute(self.main_surface, self.win)
            if event.key == pygame.K_RIGHT:
                self.current.generate_dataset()
                self.current_algo = (self.current_algo + 1) % len(self.algorithms)
                self.current.set_font(self.font)
            if event.key == pygame.K_LEFT:
                self.current.generate_dataset()
                self.current_algo = (self.current_algo - 1) % len(self.algorithms)
                self.current.set_font(self.font)
            if event.key == pygame.K_LSHIFT:
                self.current.slow_mo_speed_up()
            if event.key == pygame.K_g:
                self.current.generate_dataset()

    @property
    def current(self):
        return self.algorithms[self.current_algo]

    def run(self):
        clock = pygame.time.Clock()

        self.current.generate_dataset()
        self.current.set_font(self.font)

        while self.running:
            clock.tick(60)
            for event in pygame.event.get():
                self.events(event)

            self.draw()

        pygame.quit()

    def draw(self):
        self.current.draw([BLACK] * len(self.current.data_set), win = self.main_surface)

        self.win.fill(BLACK)
        self.description_surface.fill(WHITE)
        self.config_surface.fill(WHITE)

        y = 15
        for param, value in self.current.params().items():
            text = self.font.render(f"{param}: {value}", True, BLACK)
            self.config_surface.blit(text, (10, y))
            y += 30

        # Draw on description surface
        title = self.font.render(self.current.title(), 1, BLACK)
        self.description_surface.blit(title, (self.config_surface.get_width() // 2, 10))
        description_text = self.font.render(self.current.description, True, BLACK)
        self.description_surface.blit(description_text, (10, 25))

        # Blit all surfaces to the main window
        self.win.blit(self.main_surface, (0, 0))
        self.win.blit(self.config_surface, (WIDTH - WIDTH * 0.3, 0))
        self.win.blit(self.description_surface, (0, HEIGHT - HEIGHT * 0.28))

        pygame.display.flip()

