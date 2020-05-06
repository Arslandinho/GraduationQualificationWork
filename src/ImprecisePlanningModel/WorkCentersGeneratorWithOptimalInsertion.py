from typing import List

from src.Entities.Job import Job
from src.Entities.WorkCenter import WorkCenter
from src.Generators.WorkCentersGenerator import WorkCentersGenerator


class WorkCentersGeneratorWithOptimalInsertion:
    def __init__(self, amount_to_generate: int, jobs: List[Job], load_factor):
        self.__amount_to_generate = amount_to_generate
        self.__load_factor = load_factor

        # отсоритрованный по возрастанию (неубыванию) массив работ
        self.__jobs = sorted(jobs, key=lambda job: job.get_duration())

        self.__generated_centers = []

    def generate(self) -> List[WorkCenter]:
        if self.__generated_centers:
            return self.__generated_centers
        else:
            self.__generated_centers = \
                WorkCentersGenerator(self.__amount_to_generate, self.__jobs, self.__load_factor, 1).generate()

            return self.__generated_centers
