from typing import List

import numpy as np

from src.Entities.Operation import Operation
from src.Entities.WorkCenter import WorkCenter
from src.Generators.JobsGenerator import JobsGenerator
from src.Generators.MachinesGenerator import MachinesGenerator
from src.Generators.OperationsGenerator import OperationsGenerator


class OperationsAllocationToWorkCenters:
    @staticmethod
    # types: 0 - naive, 1 - optimal
    def insertion(amount_of_work_centers: int, operations: List[Operation],
                  amount_of_operations_in_each: int, insert_type=0):

        if insert_type == 0:
            OperationsAllocationToWorkCenters.naive_insertion(amount_of_work_centers,
                                                              operations,
                                                              amount_of_operations_in_each)
        elif insert_type == 1:
            OperationsAllocationToWorkCenters.optimal_insertion(amount_of_work_centers,
                                                                operations)

    @staticmethod
    def naive_insertion(amount_of_work_centers: int, operations: List[Operation], amount_of_operations_in_each: int):
        operations_chunks = []

        for i in range(amount_of_work_centers):
            left_border = amount_of_operations_in_each * i
            right_border = left_border + amount_of_operations_in_each

            operations_chunks.append(operations[left_border:right_border])

        return operations_chunks

    @staticmethod
    def optimal_insertion(amount_of_work_centers: int, operations: List[Operation]):
        operations_chunks = [[] for _ in range(amount_of_work_centers)]
        operations_chunks_durations = [0] * amount_of_work_centers
        len_operations = len(operations)

        while len_operations > 0:
            i = operations_chunks_durations.index(min(operations_chunks_durations))
            current_operation = operations.pop(0)

            if not operations_chunks[i]:
                operations_chunks[i] = []
            operations_chunks[i].append(current_operation)

            operations_chunks_durations[i] += current_operation.get_duration()
            len_operations -= 1

        return operations_chunks

