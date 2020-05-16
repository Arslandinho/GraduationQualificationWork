from typing import List

from src.Entities.Discrete import Discrete
from src.Entities.WorkCenter import WorkCenter


class OperationsAllocationToDiscretes:
    @staticmethod
    # types: 0 - naive, 1 - optimal
    def insertion(work_centers: List[WorkCenter], load_factor, insert_type=0):
        # реализация распределения по машинам (рудимент)
        # calc = int(len(operations) / len(machines))
        # amount_of_operations_in_each = calc if len(operations) % len(machines) == 0 else calc + 1
        #
        # k = 0
        # for machine in machines:
        #     left_border = amount_of_operations_in_each * k
        #     right_border = left_border + amount_of_operations_in_each
        #
        #     machine.add_operations(operations[left_border:right_border])
        #
        #     k += 1

        if insert_type == 0:
            return \
                OperationsAllocationToDiscretes.naive_insertion(work_centers, load_factor)
        elif insert_type == 1:
            return \
                OperationsAllocationToDiscretes.optimal_insertion(work_centers, load_factor)

    @staticmethod
    def naive_insertion(work_centers: List[WorkCenter], load_factor):
        discretes: List[List[Discrete]] = []

        z = 1
        for center in work_centers:
            discrete = Discrete(load_factor)
            temp_discretes = []
            i = 0
            for operation in center.get_all_operations():
                lst = discrete.insert_operation(operation)

                temp_discretes.extend(lst)

                if i < len(center.get_all_operations()) - 1:
                    discrete = temp_discretes.pop()
                    i += 1

            discretes.append(temp_discretes)
            z += 1

        # for discs in discretes:
        #     for disc in discs:
        #         print(disc.get_id())

        return discretes

    @staticmethod
    def optimal_insertion(work_centers: List[WorkCenter], load_factor):
        discretes: List[List[Discrete]] = []

        z = 1
        for center in work_centers:
            operations = sorted(center.get_all_operations(), key=lambda oper: oper.get_duration())

            discrete = Discrete(load_factor)
            temp_discretes = []

            i = 0
            for operation in operations:
                lst = discrete.insert_operation(operation)

                temp_discretes.extend(lst)

                if i < len(operations) - 1:
                    discrete = temp_discretes.pop()
                    i += 1

            discretes.append(temp_discretes)
            z += 1

        # for discs in discretes:
        #     for disc in discs:
        #         print(disc.get_id())

        return discretes
