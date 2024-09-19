from algorithms.core import AlgorithmType
from algorithms.core.algorithm import Algorithm
from algorithms.core.dataset_generator import RandomList
from algorithms.core.draw import DrawBarGraph
from algorithms.core.time_complexity import TimeComplexity
from config import *

class BubbleSort(Algorithm):
    def __init__(self):
        super().__init__("Bubble Sort")
        self.time_complexity = TimeComplexity.O_QUADRATIC
        self.generator = RandomList()
        self.generate_dataset()
        self.algorithm_type = AlgorithmType.SORTING
        self.drawer = DrawBarGraph()

    def run(self, win):
        n = len(self.data_set)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.data_set[j] > self.data_set[j + 1]:
                    self.data_set[j], self.data_set[j + 1] = self.data_set[j + 1], self.data_set[j]
                colors = [GREEN if x == j or x == j + 1 else BLACK for x in range(n)]
                self.draw(win, colors)
        return self.data_set