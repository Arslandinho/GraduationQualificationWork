# класс Операции
from typing import TypeVar, Generic

T = TypeVar('T')


class Operation(Generic[T]):
    def __init__(self, duration: float):
        self.__duration = duration

        self.__partitions = []

    def get_duration(self) -> float:
        return self.__duration

    def add_partition(self, partition: T):
        self.__partitions.append(partition)

    def get_partitions(self):
        return self.__partitions
