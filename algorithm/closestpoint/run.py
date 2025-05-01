import math

def execute(algorithm):
    n = len(algorithm.data_set)
    shortest = None
    shortest_length = None
    algorithm.step("search_randomly")
    for i in range(n):
        point = algorithm.data_set[i]
        distance = math.dist(point, algorithm.value)
        algorithm.step("if_lower")
        if (shortest_length is None or shortest_length > distance) and point != algorithm.value:
            shortest_length = distance
            shortest = point
            algorithm.step("set")

        colors = [(0, 0, 255) if (algorithm.data_set[x] == shortest and algorithm.data_set[x] != algorithm.value) else (0, 255, 0) if x == i else (0, 0, 0) for x in range(n)]
        algorithm.current = shortest
        algorithm.draw(colors)

    return shortest, algorithm.format_float(shortest_length)