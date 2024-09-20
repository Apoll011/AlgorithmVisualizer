from typing import Any
import math
from pygame import Surface
from config import *
import pygame

class Draw:
    def draw(self, win: Surface, colors: list[tuple[int, int, int]], data_set: list[Any | int], value_r: int | None=None, resolved: bool = False): ...

class DrawBarGraph(Draw):
    def draw(self, win: Surface, colors: list[tuple[int, int, int]], data_set: list[Any | int], value_r: int | None=None, resolved: bool = False):
        bar_width = win.get_width() // (len(data_set) + 10)
        for i, height in enumerate(data_set):
            if value_r is not None and value_r == height and colors[i] != GREEN:
                color = BLUE
            elif i < len(colors):
                color = colors[i]
            else:
                color = BLACK
            pygame.draw.rect(win, color, (i * bar_width + 10 + i, win.get_height() - height, bar_width, height - 5))

class DrawList(Draw):
    def draw(self, win: Surface, colors: list[tuple[int, int, int]], data_set: list[Any | int],
             value_r: int | None = None, resolved: bool = False):
        max_squares_per_row = win.get_width() // 50  # Assuming each square is 80x80 with some padding
        square_size = 40
        padding = 10
        font = pygame.font.Font(None, 36)

        for i, value in enumerate(data_set):
            row = i // max_squares_per_row
            col = i % max_squares_per_row

            x = col * (square_size + padding) + padding
            y = row * (square_size + padding) + padding

            if value_r is not None and value_r == value and colors[i] != GREEN:
                color = BLUE if not resolved else GREEN
            elif i < len(colors):
                color = colors[i]
            else:
                color = BLACK

            pygame.draw.rect(win, color, (x, y, square_size, square_size))

            # Render the value text
            text = font.render(str(value), True, WHITE)
            text_rect = text.get_rect(center=(x + square_size // 2, y + square_size // 2))
            win.blit(text, text_rect)

class DrawPieChart(Draw):
    def draw(self, win: Surface, colors: list[tuple[int, int, int]], data_set: list[Any | int],
             value_r: int | None = None, resolved: bool = False):
        total = sum(data_set)
        center = (win.get_width() // 2, win.get_height() // 2)
        radius = min(win.get_width(), win.get_height()) // 3
        start_angle = 0
        font = pygame.font.Font(None, 24)

        for i, value in enumerate(data_set):
            end_angle = start_angle + (value / total) * 2 * math.pi
            color = colors[i] if i < len(colors) else BLACK

            pygame.draw.arc(
                win, color, (center[0] - radius, center[1] - radius, radius * 2, radius * 2), start_angle, end_angle,
                radius
                )

            # Draw label
            mid_angle = (start_angle + end_angle) / 2
            label_x = center[0] + (radius * 1.2) * math.cos(mid_angle)
            label_y = center[1] + (radius * 1.2) * math.sin(mid_angle)
            label = font.render(f"{value} ({value / total:.1%})", True, WHITE)
            win.blit(label, (label_x - label.get_width() // 2, label_y - label.get_height() // 2))

            start_angle = end_angle

class DrawLineGraph(Draw):
    def draw(self, win: Surface, colors: list[tuple[int, int, int]], data_set: list[Any | int],
             value_r: int | None = None, resolved: bool = False):
        margin = 50
        graph_width = win.get_width() - 2 * margin
        graph_height = win.get_height() - 2 * margin
        max_value = max(data_set)

        # Draw axes
        pygame.draw.line(
            win, WHITE, (margin, win.get_height() - margin), (win.get_width() - margin, win.get_height() - margin), 2
            )
        pygame.draw.line(win, WHITE, (margin, margin), (margin, win.get_height() - margin), 2)

        font = pygame.font.Font(None, 24)

        points = []
        for i, value in enumerate(data_set):
            x = margin + (i / (len(data_set) - 1)) * graph_width
            y = win.get_height() - margin - (value / max_value) * graph_height
            points.append((x, y))

            # Draw point
            pygame.draw.circle(win, RED, (int(x), int(y)), 5)

            # Draw value label
            label = font.render(str(value), True, WHITE)
            win.blit(label, (x - label.get_width() // 2, y - 25))

        # Draw lines connecting points
        if len(points) > 1:
            pygame.draw.lines(win, BLUE, False, points, 2)

        # Draw x-axis labels
        for i, value in enumerate(data_set):
            x = margin + (i / (len(data_set) - 1)) * graph_width
            label = font.render(str(i), True, WHITE)
            win.blit(label, (x - label.get_width() // 2, win.get_height() - margin + 10))

class DrawScatterPlot(Draw):
    def draw(self, win: Surface, colors: list[tuple[int, int, int]], data_set: list[tuple[int, int]],
             value_r: int | None = None, resolved: bool = False):
        margin = 50
        graph_width = win.get_width() - 2 * margin
        graph_height = win.get_height() - 2 * margin

        max_x = max(point[0] for point in data_set)
        max_y = max(point[1] for point in data_set)

        # Draw axes
        pygame.draw.line(
            win, WHITE, (margin, win.get_height() - margin), (win.get_width() - margin, win.get_height() - margin), 2
            )
        pygame.draw.line(win, WHITE, (margin, win.get_height() - margin), (margin, margin), 2)

        font = pygame.font.Font(None, 24)

        for point in data_set:
            x = margin + (point[0] / max_x) * graph_width
            y = win.get_height() - margin - (point[1] / max_y) * graph_height

            color = colors[data_set.index(point) % len(colors)]
            pygame.draw.circle(win, color, (int(x), int(y)), 5)

        # Draw axis labels
        for i in range(5):
            # X-axis
            x_value = int(max_x * (i / 4))
            x = margin + (i / 4) * graph_width
            label = font.render(str(x_value), True, WHITE)
            win.blit(label, (x - label.get_width() // 2, win.get_height() - margin + 10))

            # Y-axis
            y_value = int(max_y * (i / 4))
            y = win.get_height() - margin - (i / 4) * graph_height
            label = font.render(str(y_value), True, WHITE)
            win.blit(label, (margin - 40, y - label.get_height() // 2))