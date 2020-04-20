from typing import List

from src.Entities.Department import Department
from src.Entities.Job import Operation
from src.Generators.WorkCentersGenerator import WorkCentersGenerator


class DepartmentsGenerator:
    def __init__(self, amount_of_work_centers_to_generate: int, operations: List[Operation]):
        self.__amount_of_work_centers_to_generate = amount_of_work_centers_to_generate
        self.__operations = operations

        self.__generated_departments = []

    def generate(self) -> List[Department]:
        if self.__generated_departments:
            return self.__generated_departments
        else:
            centers = WorkCentersGenerator(self.__amount_of_work_centers_to_generate, self.__operations).generate()
            self.__generated_departments.append(Department(centers))

            return self.__generated_departments
