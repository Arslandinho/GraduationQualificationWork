# класс Рабочего центра
from typing import List

from src.Entities.Discrete import Discrete
from src.Entities.Machine import Machine
from src.Entities.Operation import Operation


class WorkCenter:
    def __init__(self, machines: List[Machine], operations: List[Operation], load_factor: float):
        self.__load_factor = load_factor

        self.__machines = machines
        self.__operations = operations
        self.__discretes = []

        if self.__machines and self.__operations:
            # логика распределения операций по машинам
            calc = int(len(self.__operations) / len(self.__machines))
            amount_of_operations_in_each = calc if len(self.__operations) % len(self.__machines) == 0 else calc + 1
            k = 0
            for machine in self.__machines:
                left_border = amount_of_operations_in_each * k
                right_border = left_border + amount_of_operations_in_each

                machine.add_operations(self.__operations[left_border:right_border])

                k += 1

            # логика распределения операций по дискретам
            z = 1
            for machine in self.__machines:
                discrete = Discrete(self.__load_factor)
                temp_discretes = []
                i = 0
                for operation in machine.get_operations():
                    lst = discrete.insert_operation(operation)

                    temp_discretes.extend(lst)

                    if i < len(machine.get_operations()) - 1:
                        discrete = temp_discretes.pop()
                        i += 1

                self.__discretes.append(temp_discretes)
                z += 1

    def add_machine(self, machine: Machine):
        self.__machines.append(machine)

    def get_amount_of_machines(self) -> int:
        return len(self.__machines)

    def get_all_machines(self) -> List[Machine]:
        return self.__machines

    def get_all_operations(self) -> List[Operation]:
        return self.__operations

    def get_load_factor(self) -> float:
        return self.__load_factor

    def get_discretes(self) -> List[List[Discrete]]:
        return self.__discretes

    def get_overall_amount_of_discretes(self) -> int:
        return len(max(self.__discretes, key=len))
