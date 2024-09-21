import math

import pygame
import time

from algorithms import AlgorithmType
from algorithms.dataset_generator import Generator
from algorithms.draw import Draw
from algorithms.time_complexity import TimeComplexity
from config import WHITE

class Algorithm:
    waiting_time = 0.01
    algorithm_name = ""

    can_wait = False

    resolved = False

    algorithm_type = ""

    iterations = 0
    time_complexity: TimeComplexity
    time_took: float

    description = "Algorithm "

    current = None
    def __init__(self, algorithm_name):
        self.main = None
        self.returned = None
        self.master = None
        self.font = None
        self.algorithm_name = algorithm_name
        self.generator: Generator | None = None
        self.algorithm_type: AlgorithmType | None = None
        self.drawer: Draw | None = None
        self.send_value_to_draw = False
        self.return_name = "Returned"
        self.value_name = "Value"

    def generate_dataset(self):
        self.generator.generate()
        self.resolved = False
        self.iterations = 0
        self.time_took = 0
        self.returned = None

    def set_font(self, font):
        self.font = font

    def draw(self, colors, win = None):
        if win is None:
            self.iterate()
            win = self.main
        win.fill(WHITE)
        try:
            self.draw_dataset(win, colors)
        finally:
            pygame.display.update()
            self.blit(win)
            self.wait()

    def draw_dataset(self, win, colors):
        self.drawer.draw(win, colors, self.data_set, self.value if self.send_value_to_draw else None, self.resolved, self.current)

    def run(self, win) -> int | list:
        pass  # To be implemented by subclasses

    def execute(self, win, WIN):
        if not self.resolved:
            self.master = WIN
            self.main = win
            self.iterations = 0
            s_time = time.time()
            self.returned = self.run()
            self.time_took = time.time() - s_time
            self.set_resolved()
            self.master = None
            self.main = None

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
        return f"{self.algorithm_type.value.replace('_', ' ').title()} Algorithm ({self.algorithm_name}){"*" if self.can_wait else ""}"

    def iterate(self):
        self.iterations += 1

    def blit(self, main_surface):
        if self.master is not None:
            self.master.blit(main_surface, (0, 0))

    def params(self):
        params =  {
            "Iterations": self.iterations,
            "Expected Iterations": int(self.get_expected_iteration()),
            "Time complexity": self.time_complexity.value,
            "Time Took": self.get_time(),
            f"{self.value_name}": self.value if self.value_exists() else "NULL",
        }
        if type(self.return_name) == list:
            i = 0
            for elements in self.return_name:
                params[elements] = "NULL" if self.returned is None or len(self.returned) == 0 else self.returned[i] if type(self.returned[i]) != list else "[...]"
                i += 1
        else:
            params[self.return_name] = "NULL" if self.returned is None else self.returned if type(self.returned) != list else "[...]"
        return params

    def get_time(self):
        try:
            return self.format_float(self.time_took)
        except UnboundLocalError:
            return 0

    @staticmethod
    def format_float(value):
        return "{:.4f}".format(value)

    @property
    def data_set(self):
        return  self.generator.get_dataset()

    @data_set.setter
    def data_set(self, new_dataset):
        self.generator.data_set = new_dataset

    @property
    def value(self):
        return self.generator.get_value()

    def value_exists(self):
        return self.generator.value is not None

    def get_expected_iteration(self):
        n = self.generator.length
        match self.time_complexity:
            case TimeComplexity.O_LOG:
                return math.log(n)
            case TimeComplexity.O_NLOG:
                return n * math.log(n)
            case TimeComplexity.O_LINEAR:
                return n
            case TimeComplexity.O_QUADRATIC:
                return n**2
            case TimeComplexity.O_CONSTANT:
                return 1
            case TimeComplexity.O_EXPONENTIAL:
                return 2**n
            case TimeComplexity.O_FACTORIAL:
                return math.factorial(n)
