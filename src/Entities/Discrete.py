from typing import List

from src.Entities.Operation import Operation
from src.Entities.OperationPartition import OperationPartition
from src.Util.Constants.GeneralConstants import GeneralConstants


discrete_id = 1


class Discrete:
    def __init__(self, alpha: float):
        global discrete_id
        self.__id = discrete_id
        discrete_id += 1

        self.__alpha = alpha
        self.__max_duration = GeneralConstants.PLAN_DISCRETE * self.__alpha
        self.__used_duration = 0

        self.__operations = []

    def get_id(self) -> int:
        return self.__id

    def insert_operation(self, operation: Operation):
        if operation not in self.__operations:
            self.__operations.append(operation)
            operation.set_discrete_id(self.__id)

            return self.__increase_duration(operation.get_duration())
        else:
            return [self]

    def remove_and_get_last_operation(self) -> Operation:
        return self.__operations.pop()

    def __increase_duration(self, duration: float):
        if self.__used_duration + duration <= self.__max_duration:
            self.incr_used_duration(duration)

            return [self]
        else:
            left_duration = round(self.__max_duration - self.__used_duration, 1)
            last_operation = self.remove_and_get_last_operation()

            oper_part1 = OperationPartition(last_operation, left_duration).get_new_operation()
            self.append_operation(oper_part1)

            oper_part1.set_discrete_id(self.__id)

            self.incr_used_duration(oper_part1.get_duration())

            new_discrete = Discrete(self.__alpha)
            oper_part2 = OperationPartition(last_operation, duration - left_duration).get_new_operation()
            new_discrete.append_operation(oper_part2)

            if last_operation.check_if_last():
                oper_part2.assign_as_last()

            oper_part2.set_discrete_id(new_discrete.get_id())

            new_discrete.incr_used_duration(oper_part2.get_duration())

            return [self, new_discrete]

    def get_used_duration(self):
        return self.__used_duration

    def incr_used_duration(self, value):
        self.__used_duration = round(self.__used_duration + value, 1)

    def append_operation(self, operation: Operation):
        self.__operations.append(operation)

    def get_all_operations(self) -> List[Operation]:
        return self.__operations
