from typing import List

from src.Entities.Operation import Operation


class OperationsAllocationToWorkCenters:
    @staticmethod
    # types: 0 - naive, 1 - optimal
    def insertion(amount_of_work_centers: int,
                  operations: List[Operation],
                  insert_type=0):

        if insert_type == 0:
            return OperationsAllocationToWorkCenters.naive_insertion(amount_of_work_centers,
                                                                     operations)
        elif insert_type == 1:
            return OperationsAllocationToWorkCenters.optimal_insertion(amount_of_work_centers, operations)

    @staticmethod
    def naive_insertion(amount_of_work_centers: int,
                        operations: List[Operation]):

        calc = int(len(operations) / amount_of_work_centers)
        amount_of_operations_in_each = calc if len(operations) / amount_of_work_centers == 0 else calc + 1

        operations_chunks = []

        for i in range(amount_of_work_centers):
            left_border = amount_of_operations_in_each * i
            right_border = left_border + amount_of_operations_in_each

            operations_chunks.append(operations[left_border:right_border])

        return operations_chunks

    @staticmethod
    def optimal_insertion(amount_of_work_centers: int, operations: List[Operation]):
        operations_chunks: List[List[Operation]] = [[] for _ in range(amount_of_work_centers)]
        operations_chunks_durations = [0.0] * amount_of_work_centers
        len_operations = len(operations)

        while len_operations > 0:
            i = operations_chunks_durations.index(min(operations_chunks_durations))
            current_operation = operations.pop(0)

            if not operations_chunks[i]:
                operations_chunks[i] = []
            operations_chunks[i].append(current_operation)

            operations_chunks_durations[i] = \
                round(operations_chunks_durations[i] + current_operation.get_duration(), 1)
            len_operations -= 1

        return operations_chunks
