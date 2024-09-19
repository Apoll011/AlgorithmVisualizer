from config import *
import pygame

class Draw:
    def draw(self, win, colors, data_set, value_r = None, resolved: bool = False): ...

class DrawBarGraph(Draw):
    def draw(self, win, colors, data_set, value_r = None, resolved: bool = False):
        bar_width = win.get_width() // (len(data_set) + 1)
        for i, height in enumerate(data_set):
            if value_r is not None and value_r == height and colors[i] != GREEN:
                color = BLUE
            elif i < len(colors):
                color = colors[i]
            else:
                color = BLACK
            pygame.draw.rect(win, color, (i * bar_width + 10, win.get_height() - height, bar_width, height))

class DrawList(Draw):
    def draw(self, win, colors, data_set, value_r = None, resolved: bool = False):
        box_width = win.get_width() // (len(data_set) + 5)
        for i, value in enumerate(data_set):
            if value_r is not None and value_r == value and colors[i] != GREEN:
                color = BLUE if not resolved else GREEN
            elif i < len(colors):
                color = colors[i]
            else:
                color = BLACK
            pygame.draw.rect(win, color, (i * box_width + 2 * i, win.get_height() / 2 - 40, box_width, 80))