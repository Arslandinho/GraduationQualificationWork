from typing import List
import numpy as np

from src.Entities.Job import Job
from src.Util.Constants.GeneralConstants import GeneralConstants
from src.Util.Constants.JobsGeneratorConstants import JobsGeneratorConstants


class JobsGenerator:
    def __init__(self):
        self.__min_amount_of_jobs = JobsGeneratorConstants.MIN_AMOUNT_OF_JOBS
        self.__max_amount_of_jobs = JobsGeneratorConstants.MAX_AMOUNT_OF_JOBS
        self.__min_duration_time = JobsGeneratorConstants.MIN_DURATION_TIME
        self.__max_duration_time = JobsGeneratorConstants.MAX_DURATION_TIME

        self.__generated_jobs = []

    def generate(self) -> List[Job]:
        if self.__generated_jobs:
            return self.__generated_jobs
        else:
            jobs_amount = GeneralConstants.PLAN_PERIOD_LONGITUDE

            i = 0
            while jobs_amount >= GeneralConstants.PLAN_DISCRETE:
                duration = round((self.__max_duration_time - self.__min_duration_time) * np.random.random()
                                 + self.__min_duration_time, 1)

                self.__generated_jobs.append(Job(duration, "Job #" + str(i + 1)))

                i += 1
                jobs_amount -= GeneralConstants.PLAN_DISCRETE

            return self.__generated_jobs
