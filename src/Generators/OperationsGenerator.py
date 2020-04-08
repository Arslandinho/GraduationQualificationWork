from typing import List

from src.Entities.Job import Job
from src.Entities.Operation import Operation
from src.Util.Constants.OperationsGeneratorConstants import OperationsGeneratorConstants


class OperationsGenerator:
    def __init__(self, jobs: List[Job]):
        self.__delta_interval = OperationsGeneratorConstants.DELTA_INTERVAL

        self.__jobs = jobs

        self.__generated_operations = []

    def generate(self) -> List[Operation]:
        if self.__generated_operations:
            return self.__generated_operations
        else:
            for job in self.__jobs:
                if job.get_duration() <= self.__delta_interval:
                    operation = Operation(job.get_duration())
                    self.__generated_operations.append(operation)
                    job.add_operation(operation)
                else:
                    temp_duration = job.get_duration()

                    while temp_duration > self.__delta_interval:
                        operation = Operation(self.__delta_interval)
                        self.__generated_operations.append(operation)
                        job.add_operation(operation)

                        temp_duration = round((temp_duration - self.__delta_interval) * 10) / 10.0

                    operation = Operation(temp_duration)
                    self.__generated_operations.append(operation)
                    job.add_operation(operation)

            return self.__generated_operations
