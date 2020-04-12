# класс Рабочего центра
from typing import List

from src.Entities.Machine import Machine
from src.Entities.Operation import Operation
from src.Util.Constants.GeneralConstants import GeneralConstants


class WorkCenter:
    def __init__(self, machines: List[Machine], operations: List[Operation], load_factor: float):
        self.__machines = machines
        self.__operations = operations
        self.__load_factor = load_factor
        self.__plan_discretion_available = GeneralConstants.PLAN_DISCRETION * load_factor

        if self.__machines and self.__operations:
            calc = int(len(self.__operations) / len(self.__machines))
            amount_of_operations_in_each = calc if len(self.__operations) / len(self.__machines) == 0 else calc + 1
            k = 0
            for machine in self.__machines:
                left_border = amount_of_operations_in_each * k
                right_border = left_border + amount_of_operations_in_each

                machine.add_operations(self.__operations[left_border:right_border])

                k += 1

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
