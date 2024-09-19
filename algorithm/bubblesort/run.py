def execute(algorithm):
    n = len(algorithm.data_set)
    for i in range(n):
        for j in range(0, n - i - 1):
            if algorithm.data_set[j] > algorithm.data_set[j + 1]:
                algorithm.data_set[j], algorithm.data_set[j + 1] = algorithm.data_set[j + 1], algorithm.data_set[j]
            colors = [(0, 255, 0) if x == j or x == j + 1 else (0, 0, 0) for x in range(n)]
            algorithm.draw(colors)

    return algorithm.data_set