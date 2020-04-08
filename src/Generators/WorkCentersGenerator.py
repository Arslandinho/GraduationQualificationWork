from typing import List
from numpy import random

from src.Entities.Machine import Machine
from src.Entities.Job import Operation
from src.Entities.WorkCenter import WorkCenter
from src.Generators.MachinesGenerator import MachinesGenerator
from src.Generators.JobsGenerator import JobsGenerator
from src.Util.Constants.WorkCentersGeneratorConstants import WorkCentersGeneratorConstants
from src.Util.Utils import Utils


class WorkCentersGenerator:
    def __init__(self, operations: List[Operation]):
        self.__amount_of_machines_total = WorkCentersGeneratorConstants.AMOUNT_OF_MACHINES_TOTAL
        self.__amount_of_machines_in_each = Utils.chunk(self.__amount_of_machines_total)
        self.__load_factor_low_border = WorkCentersGeneratorConstants.LOAD_FACTOR_LOW_BORDER
        self.__load_factor_high_border = WorkCentersGeneratorConstants.LOAD_FACTOR_HIGH_BORDER

        # отсоритрованный по возрастанию массив операций
        self.__operations = sorted(operations, key=lambda operation: operation.get_duration())

        self.__generated_centers = []

    def generate(self) -> List[WorkCenter]:
        if self.__generated_centers:
            return self.__generated_centers
        else:
            operations_in_each = Utils.split(len(self.__operations), 7)
            operations_count, i = 0, 0
            for amount in self.__amount_of_machines_in_each:
                machines = MachinesGenerator(amount).generate()

                load_factor = round(random.uniform(self.__load_factor_low_border, self.__load_factor_high_border), 2)

                # TODO иногда крашится
                wc_operations = self.__operations[operations_count:operations_count + operations_in_each[i]]
                center = WorkCenter(machines, wc_operations, load_factor)

                # machines_count, j = 0, 0
                # wc_machines: List[Machine] = center.get_all_machines()
                # while len(wc_operations) > 0:
                #     wc_machines[j] = wc

                self.__generated_centers.append(center)

                operations_count += operations_in_each[i]
                i += 1

            return self.__generated_centers


# ops = OperationsGenerator().generate()
# wcs = WorkCentersGenerator(ops).generate()
# for wc in wcs:
#     for op in wc.get_all_operations(): print(op.get_duration())