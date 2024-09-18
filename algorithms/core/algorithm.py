import pygame
import time
from config import WHITE, WIDTH, BLACK

class Algorithm:
    waiting_time = 0.01
    algorithm_name = ""

    can_wait = False

    resolved = False

    def __init__(self, type):
        self.type = type
        self.data_set = []

    def generate_dataset(self, n):
        pass

    def set_font(self, font):
        self.font = font

    def draw(self, win, colors):
        win.fill(WHITE)
        try:
            self.draw_dataset(win, colors)
        finally:
            title = self.font.render(f"{self.type} ({self.algorithm_name}){"*" if self.can_wait else ""}", 1, BLACK)
            win.blit(title, (WIDTH // 2 - title.get_width() // 2, 10))
            pygame.display.update()

    def draw_dataset(self, win, colors):
        pass

    def run(self, win):
        pass  # To be implemented by subclasses

    def wait(self):
        if self.can_wait:
            time.sleep(self.waiting_time)

    def slow_mo_speed_up(self):
        self.can_wait = not self.can_wait

    def set_resolved(self):
        self.resolved = True

    def is_resolved(self):
        return  self.resolved