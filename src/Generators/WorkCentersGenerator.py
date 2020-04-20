from typing import List
from numpy import random

from src.Entities.Job import Operation
from src.Entities.WorkCenter import WorkCenter
from src.Generators.JobsGenerator import JobsGenerator
from src.Generators.MachinesGenerator import MachinesGenerator
from src.Generators.OperationsGenerator import OperationsGenerator
from src.Util.Constants.WorkCentersGeneratorConstants import WorkCentersGeneratorConstants


class WorkCentersGenerator:
    def __init__(self, amount_to_generate: int, operations: List[Operation]):
        self.__amount_to_generate = amount_to_generate
        self.__amount_of_machines_in_each = WorkCentersGeneratorConstants.AMOUNT_OF_MACHINES_IN_EACH
        self.__load_factor_low_border = WorkCentersGeneratorConstants.LOAD_FACTOR_LOW_BORDER
        self.__load_factor_high_border = WorkCentersGeneratorConstants.LOAD_FACTOR_HIGH_BORDER

        # отсоритрованный по возрастанию массив операций
        # self.__operations = sorted(operations, key=lambda operation: operation.get_duration())
        self.__operations = operations

        self.__generated_centers = []

    def generate(self) -> List[WorkCenter]:
        if self.__generated_centers:
            return self.__generated_centers
        else:
            k = 0
            calc = int(len(self.__operations) / self.__amount_to_generate)
            amount_of_operations_in_each = calc if len(self.__operations) / self.__amount_to_generate == 0 else calc + 1
            for i in range(self.__amount_to_generate):
                left_border = amount_of_operations_in_each * k
                right_border = left_border + amount_of_operations_in_each

                machines = MachinesGenerator(self.__amount_of_machines_in_each).generate()
                load_factor = round(random.uniform(self.__load_factor_low_border, self.__load_factor_high_border), 2)

                self.__generated_centers.append(
                    WorkCenter(machines, self.__operations[left_border:right_border], load_factor)
                )

                k += 1

            return self.__generated_centers
