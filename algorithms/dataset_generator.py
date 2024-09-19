import random
from typing import Any

class Generator:
    value: Any | None = None
    data_set: Any | None = None

    def __init__(self, length = 50, create_value = False, is_dataset_sorted = False, dataset_unique = False):
        self.length = length
        self.create_value = create_value
        self.is_dataset_sorted = is_dataset_sorted
        self.dataset_unique = dataset_unique

    def generate(self): ...

    def get_value(self):
        if self.value is None:
            self.value = random.choice(self.data_set)

        return self.value

    def get_dataset(self):
        if self.data_set is None:
            raise ReferenceError("Dataset not generated")

        return self.data_set

class RandomList(Generator):
    def generate(self):
        self.data_set = [random.randint(0, 400) for _ in range(self.length)]

        if self.dataset_unique:
            self.data_set = list(set(self.data_set))
        if self.is_dataset_sorted:
            self.data_set = sorted(self.data_set)
        if self.create_value:
            self.value = random.choice(self.data_set)