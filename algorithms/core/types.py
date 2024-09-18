from algorithms.core.algorithm import Algorithm
from config import *
import random
import pygame

class SortingAlgorithm(Algorithm):
    def __init__(self, algorithm_name):
        super().__init__("Sorting Algorithm")
        self.algorithm_name = algorithm_name

    def generate_dataset(self, n):
        self.data_set = [random.randint(10, HEIGHT - 10) for _ in range(n)]

    def draw_dataset(self, win, colors):
        bar_width = WIDTH // (len(self.data_set) + 1)
        for i, height in enumerate(self.data_set):
            color = colors[i] if i < len(colors) else BLACK
            pygame.draw.rect(win, color, (i * bar_width, HEIGHT - height, bar_width, height))

class RecursionAlgorithm(Algorithm):
    def __init__(self, algorithm_name):
        super().__init__("Recursion Algorithm")
        self.algorithm_name = algorithm_name

    def generate_dataset(self, n):
        self.data_set = [random.randint(10, HEIGHT - 10) for _ in range(n)]

    def draw_dataset(self, win, colors):
        bar_width = WIDTH // (len(self.data_set) + 1)
        for i, height in enumerate(self.data_set):
            color = colors[i] if i < len(colors) else BLACK
            pygame.draw.rect(win, color, (i * bar_width, HEIGHT - height, bar_width, height))

class SearchAlgorithm(Algorithm):
    def __init__(self, algorithm_name):
        super().__init__("Searching Algorithm")
        self.value = None
        self.sorted = False
        self.waiting_time = 0.1
        self.algorithm_name = algorithm_name

    def generate_dataset(self, n):
        self.data_set = [random.randint(10, HEIGHT - 10) for _ in range(n)]
        if self.sorted:
            self.data_set = sorted(self.data_set)
        self.value = random.choice(self.data_set)

    def draw_dataset(self, win, colors):
        box_width = WIDTH // (len(self.data_set) + 5)
        for i, value in enumerate(self.data_set):
            if value == self.value and colors[i] != GREEN:
                color = BLUE
            elif i < len(colors):
                color = colors[i]
            else:
                color = BLACK
            pygame.draw.rect(win, color, (i * box_width + 2 * i, HEIGHT / 2 - 40, box_width, 80))
