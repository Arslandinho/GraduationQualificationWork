# класс Операции


class Operation:
    def __init__(self, duration: float):
        self.__duration = duration

    def get_duration(self) -> float:
        return self.__duration
