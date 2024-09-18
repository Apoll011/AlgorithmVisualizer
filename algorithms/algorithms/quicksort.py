from config import *
from algorithms.core import RecursionAlgorithm

class QuickSort(RecursionAlgorithm):
    def __init__(self):
        super().__init__("Quick Sort")
        self.waiting_time = 0.2

    def partition(self, start, end, win):
        pivot = self.data_set[end]
        i = start - 1
        for j in range(start, end):
            if self.data_set[j] < pivot:
                i += 1
                self.data_set[i], self.data_set[j] = self.data_set[j], self.data_set[i]
            colors = [RED if x == end else GREEN if x == i or x == j else BLACK for x in range(len(self.data_set))]
            self.draw(win, colors)
            self.wait()
        self.data_set[i + 1], self.data_set[end] = self.data_set[end], self.data_set[i + 1]
        return i + 1

    def quick_sort(self, start, end, win):
        if start < end:
            pi = self.partition(start, end, win)
            self.quick_sort(start, pi - 1, win)
            self.quick_sort(pi + 1, end, win)

    def run(self, win):
        self.quick_sort(0, len(self.data_set) - 1, win)