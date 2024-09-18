from algorithms.core import SortingAlgorithm
from config import *

class BubbleSort(SortingAlgorithm):
    def __init__(self):
        super().__init__("Bubble Sort")

    def run(self, win):
        n = len(self.data_set)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.data_set[j] > self.data_set[j + 1]:
                    self.data_set[j], self.data_set[j + 1] = self.data_set[j + 1], self.data_set[j]
                colors = [GREEN if x == j or x == j + 1 else BLACK for x in range(n)]
                self.draw(win, colors)
                self.wait()