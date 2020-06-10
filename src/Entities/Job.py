# класс Работы
import math
from typing import List

from src.Entities.Operation import Operation
from src.Util.Constants.GeneralConstants import GeneralConstants


class Job:
    def __init__(self, duration: float, job_name="Default_Name"):
        self.__operations = []
        self.__duration = duration
        self.__job_name = job_name
        self.__amount_of_intervals_to_get_done = math.ceil(self.__duration / GeneralConstants.PLAN_DISCRETE)

    def add_operation(self, operation: Operation):
        self.__operations.append(operation)

    def remove_operation(self, operation: Operation):
        self.__operations.remove(operation)

    def get_all_operations(self) -> List[Operation]:
        return self.__operations

    def add_operations(self, operations: List[Operation]):
        for operation in operations:
            self.add_operation(operation)

    def get_name(self) -> str:
        return self.__job_name

    def get_duration(self) -> float:
        return self.__duration

    def get_amount_of_intervals(self):
        return self.__amount_of_intervals_to_get_done
