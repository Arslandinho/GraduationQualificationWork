# класс Рабочего центра
from typing import List

from src.Entities.Machine import Machine
from src.Entities.Operation import Operation


class WorkCenter:
    def __init__(self, machines: List[Machine], operations: List[Operation], load_factor: float):
        self.__machines = machines
        self.__operations = operations
        self.__load_factor = load_factor

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
