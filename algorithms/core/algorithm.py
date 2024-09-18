import pygame
import time

from algorithms.core.time_complexity import TimeComplexity
from config import WHITE, BLACK

class Algorithm:
    waiting_time = 0.01
    algorithm_name = ""

    can_wait = False

    resolved = False

    algorithm_type = ""

    iterations = 0
    time_complexity: TimeComplexity
    time_took: float

    def __init__(self, algorithm_type):
        self.master = None
        self.font = None
        self.algorithm_type = algorithm_type
        self.data_set = []

    def generate_dataset(self, n = 50):
        pass

    def set_font(self, font):
        self.font = font

    def draw(self, win, colors):
        win.fill(WHITE)
        try:
            self.draw_dataset(win, colors)
        finally:
            title = self.font.render(self.title(), 1, BLACK)
            win.blit(title, (win.get_width() // 2 - title.get_width() // 2, 10))
            pygame.display.update()
            self.blit(win)
    def draw_dataset(self, win, colors):
        pass

    def run(self, win):
        pass  # To be implemented by subclasses

    def execute(self, win, WIN):
        if not self.resolved:
            self.master = WIN
            self.iterations = 0
            s_time = time.time()
            self.run(win)
            self.time_took = time.time() - s_time
            self.set_resolved()
            self.master = None
        print(f"Time took: {self.time_took}\nIterations: {self.iterations}")
    def wait(self):
        if self.can_wait:
            time.sleep(self.waiting_time)

    def slow_mo_speed_up(self):
        self.can_wait = not self.can_wait

    def set_resolved(self):
        self.resolved = True

    def is_resolved(self):
        return  self.resolved

    def title(self):
        return f"{self.algorithm_type} ({self.algorithm_name}){"*" if self.can_wait else ""}"

    def iterate(self):
        self.iterations += 1

    def blit(self, main_surface):
        if self.master is not None:
            self.master.blit(main_surface, (0, 0))