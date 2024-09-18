from algorithms.core.time_complexity import TimeComplexity
from config import *
from algorithms.core import SearchAlgorithm

class LinearSearchAlgorithm(SearchAlgorithm):
    def __init__(self):
        super().__init__("Linear Search")
        self.time_complexity = TimeComplexity.O_LINEAR

    def run(self, win):
        n = len(self.data_set)
        for i in range(n):
            self.iterate()
            colors = [GREEN if x == i else BLACK for x in range(n)]
            self.draw(win, colors)
            if self.data_set[i] == self.value:
                break
            self.wait()
