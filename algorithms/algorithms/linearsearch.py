from algorithms.core.algorithm import Algorithm
from algorithms.core.dataset_generator import RandomList
from algorithms.core.draw import DrawList
from algorithms.core.time_complexity import TimeComplexity
from config import *
from algorithms.core import AlgorithmType

class LinearSearchAlgorithm(Algorithm):
    def __init__(self):
        super().__init__("Linear Search")
        self.time_complexity = TimeComplexity.O_LINEAR
        self.generator = RandomList(create_value=True, dataset_unique=True)
        self.generate_dataset()
        self.algorithm_type = AlgorithmType.SEARCH
        self.drawer = DrawList()
        self.send_value_to_draw = True
        self.return_name = "Index"
        self.waiting_time = 0.1

    def run(self):
        n = len(self.data_set)
        for i in range(n):
            colors = [BLUE if self.value == self.data_set[x] else GREEN if x == i else BLACK for x in range(n)]
            self.draw(colors)
            if self.data_set[i] == self.value:
                return i