def execute(algorithm):
    quick_sort(0, len(algorithm.data_set) - 1, algorithm)
    return algorithm.data_set

def partition(start, end, algorithm):
    pivot = algorithm.data_set[end]
    i = start - 1
    for j in range(start, end):
        if algorithm.data_set[j] < pivot:
            i += 1
            algorithm.data_set[i], algorithm.data_set[j] = algorithm.data_set[j], algorithm.data_set[i]
        colors = [(255, 0, 0) if x == end else (0, 255, 0) if x == i or x == j else (0, 0, 0) for x in range(len(algorithm.data_set))]
        algorithm.draw(colors)
        algorithm.data_set[i + 1], algorithm.data_set[end] = algorithm.data_set[end], algorithm.data_set[i + 1]
    return i + 1

def quick_sort(start, end, algorithm):
    if start < end:
        pi = partition(start, end, algorithm)
        quick_sort(start, pi - 1, algorithm)
        quick_sort(pi + 1, end, algorithm)