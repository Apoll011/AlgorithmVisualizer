from codecs import replace_errors

from algorithms.core.algorithm import Algorithm
from algorithms.core.dataset_generator import RandomList
from algorithms.core.draw import DrawList
from algorithms.core.time_complexity import TimeComplexity
from config import *
from algorithms.core import AlgorithmType

class DivideAndConquerAlgorithm(Algorithm):
    def __init__(self):
        super().__init__("Divide and Conquer")
        self.waiting_time = 0.2
        self.time_complexity = TimeComplexity.O_LOG
        self.generator = RandomList(create_value=True, dataset_unique=True, is_dataset_sorted=True)
        self.generate_dataset()
        self.algorithm_type = AlgorithmType.DIVIDE_AND_CONQUER
        self.drawer = DrawList()
        self.send_value_to_draw = True
        self.return_name = "Index"

    def run(self, win):
        return self.search(self.data_set, win)

    def search(self, dataset, win):
        n = len(self.data_set)
        half = len(dataset)//2
        half_value = dataset[half]
        colors = [GREEN if x == self.data_set.index(half_value) else BLACK for x in range(n)]
        self.draw(win, colors)
        if half_value == self.value:
            return self.data_set.index(half_value)
        elif half_value > self.value:
            return self.search(dataset[:half], win)
        else:
            return self.search(dataset[half+1:], win)
