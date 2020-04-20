from typing import List

from src.Entities.Operation import Operation
from src.Entities.OperationPartition import OperationPartition
from src.Util.Constants.GeneralConstants import GeneralConstants


class Discretion:
    def __init__(self, alpha: float):
        self.__alpha = alpha
        self.__max_duration = GeneralConstants.PLAN_DISCRETION * self.__alpha
        self.__used_duration = 0

        self.__operations = []

    def insert_operation(self, operation: Operation):
        if operation not in self.__operations:
            self.__operations.append(operation)

            return self.__increase_duration(operation.get_duration())
        else:
            return [self]

    def remove_and_get_last_operation(self) -> Operation:
        return self.__operations.pop()

    def __increase_duration(self, duration: float):
        if self.__used_duration + duration <= self.__max_duration:
            self.__used_duration = round(self.__used_duration + duration, 1)

            return [self]
        else:
            left_duration = round(self.__max_duration - self.__used_duration, 1)
            last_operation = self.remove_and_get_last_operation()

            oper_part1 = OperationPartition(last_operation, left_duration).get_new_operation()
            self.__operations.append(oper_part1)

            new_discretion = Discretion(self.__alpha)
            oper_part2 = OperationPartition(last_operation, duration - left_duration).get_new_operation()
            self.__operations.append(oper_part2)

            return [self, new_discretion]

    def get_used_duration(self):
        return self.__used_duration

    def get_all_operations(self) -> List[Operation]:
        return self.__operations
