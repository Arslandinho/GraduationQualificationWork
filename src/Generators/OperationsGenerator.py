from typing import List

import numpy as np

from src.Entities.Job import Job
from src.Entities.Operation import Operation
from src.Util.Constants.GeneralConstants import GeneralConstants
from src.Util.Constants.OperationsGeneratorConstants import OperationsGeneratorConstants


class OperationsGenerator:
    def __init__(self, jobs: List[Job]):
        self.__delta_interval = GeneralConstants.PLAN_DISCRETE
        self.__min_duration = OperationsGeneratorConstants.MIN_DURATION
        self.__max_duration = OperationsGeneratorConstants.MAX_DURATION

        self.__jobs = jobs

        self.__generated_operations = []

    def generate(self) -> List[Operation]:
        if self.__generated_operations:
            return self.__generated_operations
        else:
            for job in self.__jobs:
                operations = self.__split_job_into_chunks_2_4(job)
                job.add_operations(operations)

                self.__generated_operations.extend(operations)

            return self.__generated_operations

    def __split_job_into_chunks_2_4(self, job: Job) -> List[Operation]:
        job_chunks = []
        job_duration = job.get_duration()

        while job_duration > self.__max_duration:
            random_operation_duration = round(np.random.uniform(self.__min_duration, self.__max_duration), 1)

            operation = Operation(random_operation_duration)
            job_chunks.append(operation)

            job_duration = round((job_duration - random_operation_duration) * 10) / 10.0

        operation = Operation(job_duration)
        job_chunks.append(operation)

        return job_chunks
