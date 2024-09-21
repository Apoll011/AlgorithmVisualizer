def execute(algorithm):
    swap = 0
    n = len(algorithm.data_set)
    for i in range(n):
        algorithm.step("loop_every_thing")
        for j in range(0, n - i - 1): # Search every element that has not passed in the previous loop.
            algorithm.step("search_not_searched")
            algorithm.step("if_bigger")
            if algorithm.data_set[j] > algorithm.data_set[j + 1]: # If the element is bigger than the next one
                swap+=1
                algorithm.data_set[j], algorithm.data_set[j + 1] = algorithm.data_set[j + 1], algorithm.data_set[j] # Swap them
                algorithm.step("swap")
            colors = [(0, 255, 0) if x == j or x == j + 1 else (0, 0, 0) for x in range(n)]
            algorithm.draw(colors)
    algorithm.step()

    return algorithm.data_set, swap