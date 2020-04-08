from typing import List

from src.Entities.Machine import Machine


class MachinesGenerator:
    def __init__(self, amount: int):
        self.__amount = amount
        self.__generated_machines = []

    def generate(self) -> List[Machine]:
        if self.__generated_machines:
            return self.__generated_machines
        else:
            for i in range(self.__amount):
                machine = Machine()
                self.__generated_machines.append(machine)

            return self.__generated_machines

