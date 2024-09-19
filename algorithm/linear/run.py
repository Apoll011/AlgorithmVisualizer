def execute(algorithm):
    n = len(algorithm.data_set)
    for i in range(n):
        colors = [(0, 255, 0) if x == i else (0, 0, 0) for x in range(n)]
        algorithm.draw(colors)
        if algorithm.data_set[i] == algorithm.value:
            return i