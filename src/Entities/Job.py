# класс Работы
from typing import List

from src.Entities.Operation import Operation


class Job:
    def __init__(self, duration: float, job_name="Default_Name"):
        self.__operations = []
        self.__duration = duration
        self.__job_name = job_name

    def add_operation(self, operation: Operation):
        self.__operations.append(operation)

    def remove_operation(self, operation: Operation):
        self.__operations.remove(operation)

    def get_all_operations(self) -> List[Operation]:
        return self.__operations

    def add_operations(self, operations: List[Operation]):
        self.__operations.extend(operations)

    def get_name(self) -> str:
        return self.__job_name

    def get_duration(self) -> float:
        return self.__duration
