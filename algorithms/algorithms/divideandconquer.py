from config import *
from algorithms.core import SearchAlgorithm

class DivideAndConquerAlgorithm(SearchAlgorithm):
    def __init__(self):
        self.sorted = True
        super().__init__("Divide and Conquer")

    def run(self, win):
        self.search(self.data_set, win)

    def search(self, dataset, win):
        n = len(self.data_set)
        half = len(dataset)//2
        half_value = dataset[half]
        colors = [GREEN if x == self.data_set.index(half_value) else BLACK for x in range(n)]
        self.draw(win, colors)
        self.wait()
        if half_value == self.value:
            pass
        elif half_value > self.value:
            self.search(dataset[:half], win)
        else:
            self.search(dataset[half+1:], win)
