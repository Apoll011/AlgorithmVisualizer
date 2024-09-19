from algorithms.core.constructor import Constructor
from algorithms.core.visualizer import AlgorithmVisualizer

if __name__ == "__main__":
    visualizer = AlgorithmVisualizer()
    visualizer.get_algorithms("algorithm/")
    visualizer.run()