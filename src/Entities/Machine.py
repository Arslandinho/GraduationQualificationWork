# класс Рабочей машины (станка)
import numpy as np

from src.Entities.Job import Operation


class Machine:
    def __init__(self):
        self.__max_error_probability = 0.2
        self.__error_probability = round(self.__max_error_probability * np.random.random(), 2)

        self.__operations = []

    def add_operation(self, operation: Operation):
        self.__operations.append(operation)

    def get_error_probability(self) -> float:
        return self.__error_probability