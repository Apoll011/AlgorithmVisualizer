def execute(algorithm):
    return search(algorithm.data_set, algorithm.data_set, algorithm.value, algorithm.draw)

def search(original, dataset, value, draw):
    n = len(original)
    half = len(dataset) // 2
    half_value = dataset[half]
    colors = [(0, 255, 0) if x == original.index(half_value) else (0, 0, 0) for x in range(n)]
    draw(colors)
    if half_value == value:
        return original.index(half_value)
    elif half_value > value:
        return search(original, dataset[:half], value, draw)
    else:
        return search(original, dataset[half + 1:], value, draw)