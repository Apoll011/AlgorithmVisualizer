import importlib
import json
import os

from algorithms import AlgorithmType
from algorithms.algorithm import Algorithm
from algorithms.dataset_generator import RandomList, RandomMultidimensionalSpace, SequentialNumber
from algorithms.time_complexity import TimeComplexity
from algorithms.draw import DrawBarGraph, DrawLineGraph, DrawList, DrawPieChart, DrawScatterPlot

class Constructor:
    def __init__(self, path):
        self.algorithms = []
        for algorithm in os.listdir(path):
            with open(f"{path}/{algorithm}/.config", "r") as config_file:
                config = self.filter_config(json.load(config_file))

            run_instance = importlib.import_module(path.replace("/", ".") + f"{algorithm}.run")
            run_method = getattr(run_instance, "execute")

            self.factory(config, run_method)

    def factory(self, config, run_method):
            algorithm_obj = Algorithm(config["name"])
            algorithm_obj.drawer = self.get_drawer(config["drawer"])
            algorithm_obj.description = config["description"]
            algorithm_obj.algorithm_type = self.get_algorithm_type(config["algorithm_type"])
            algorithm_obj.waiting_time = config["waiting_time"]
            algorithm_obj.time_complexity = self.get_time_complexity(config["time_complexity"])
            algorithm_obj.generator = self.generate_generator(config["generator"])
            algorithm_obj.send_value_to_draw = config["send_value_to_draw"]
            algorithm_obj.return_name = config["return_name"]
            algorithm_obj.generate_dataset()
            algorithm_obj.run = lambda: run_method(algorithm_obj)

            self.algorithms.append(algorithm_obj)

    @staticmethod
    def get_drawer(name):
        match name:
            case "list":
                return DrawList()
            case "bar":
                return DrawBarGraph()
            case "line":
                return DrawLineGraph()
            case "pie":
                return DrawPieChart()
            case "scatter":
                return DrawScatterPlot()
            case _:
                raise KeyError(f"Unknown draw class {name}")

    @staticmethod
    def get_algorithm_type(name):
        return AlgorithmType(name)

    @staticmethod
    def get_time_complexity(name):
        return TimeComplexity(name)

    @staticmethod
    def generate_generator(params):
        match params["name"]:
            case "r_list":
                return RandomList(**params["args"])
            case "r_dimension":
                return RandomMultidimensionalSpace(**params["args"])
            case "sequential":
                return SequentialNumber(**params["args"])
            case _:
                raise KeyError(f"Unknown Dataset generator {params["name"]}")

    @staticmethod
    def filter_config(config):
        default = {
            "waiting_time": 0.01,
            "time_complexity": "O(N)",
            "generator": {
                "name": "r_list",
                "args": {
                    "create_value": False,
                    "dataset_unique": False,
                    "is_dataset_sorted": False,
                }
            },
            "send_value_to_draw": False,
            "return_name": "Return"
        } | config

        return default