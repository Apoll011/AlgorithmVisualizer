from enum import Enum

class TimeComplexity(Enum):
    O_CONSTANT = "O(1)"
    O_LOG = "O(log N)"
    O_LINEAR = "O(N)"
    O_NLOG = "O(N log N)"
    O_QUADRATIC = "O(N^2)"
    O_EXPONENTIAL = "O(2^N)"
    O_FACTORIAL = "O(N!)"