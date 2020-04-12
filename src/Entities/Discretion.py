from src.Util.Constants.GeneralConstants import GeneralConstants


class Discretion:
    def __init__(self):
        self.__max_duration = GeneralConstants.PLAN_DISCRETION
        self.__available_duration = 0

    def increase_duration(self, duration: float):
        if self.__available_duration + duration <= self.__max_duration:
            self.__available_duration += duration
        else:
            new_discretion = Discretion()
            new_discretion.increase_duration(duration)
            return [self, new_discretion]

    def get_available_duration(self):
        return self.__available_duration
