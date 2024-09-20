import random
from typing import Any

class Generator:
    value: Any | None = None
    data_set: Any | None | list = None

    def __init__(self, length = 50, create_value = False, is_dataset_sorted = False, dataset_unique = False, start = 10, end = 400, step = 1, dimensions = 2):
        self.length = length
        self.create_value = create_value
        self.is_dataset_sorted = is_dataset_sorted
        self.dataset_unique = dataset_unique
        self.start = start
        self.end = end
        self.step = step
        self.dimensions = dimensions

    def generate(self): ...

    def get_value(self):
        if self.value is None:
            self.value = random.choice(self.data_set)

        return self.value

    def get_dataset(self):
        if self.data_set is None:
            raise ReferenceError("Dataset not generated")

        return self.data_set

    def filter(self):
        if self.dataset_unique:
            self.data_set = list(set(self.data_set))
        if self.is_dataset_sorted:
            self.data_set = sorted(self.data_set)
        if self.create_value:
            self.value = random.choice(self.data_set)

    def get_random_element(self):
        element = random.choice(self.data_set)
        if self.value is not None and element != self.value:
            return element
        elif self.value is None:
            return  element

        return self.get_random_element()

class RandomList(Generator):
    def generate(self):
        self.data_set = [random.randint(self.start, self.end) for _ in range(self.length)]
        self.filter()

class SequentialNumber(Generator):
    def generate(self):
        self.data_set = [i for i in range(self.start, self.end, self.step)]
        self.filter()

class RandomMultidimensionalSpace(Generator):
    def generate(self):
        self.data_set = [self.generate_point() for _ in range(self.length)]
        self.filter()

    def generate_point(self):
        point = (random.randint(self.start, self.end), random.randint(self.start, self.end))
        if point != self.data_set:
            return point
        return self.generate_point()