# класс Операции
from typing import TypeVar, Generic

T = TypeVar('T')


class Operation(Generic[T]):
    def __init__(self, duration: float):
        self.__id = None
        self.__duration = duration
        self.__job_name = ""
        self.__discrete_id = None
        self.__is_last = False

        self.__partitions = []

    def get_duration(self) -> float:
        return self.__duration

    def add_partition(self, partition: T):
        self.__partitions.append(partition)

    def get_partitions(self):
        return self.__partitions

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_job_name(self):
        return self.__job_name

    def set_job_name(self, job_name):
        self.__job_name = job_name

    def get_discrete_id(self):
        return self.__discrete_id

    def set_discrete_id(self, id):
        self.__discrete_id = id

    def assign_as_last(self):
        self.__is_last = True

    def check_if_last(self):
        return self.__is_last
