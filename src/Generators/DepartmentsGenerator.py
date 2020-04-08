from typing import List

from src.Entities.Department import Department
from src.Entities.Job import Operation
from src.Generators.WorkCentersGenerator import WorkCentersGenerator


class DepartmentsGenerator:
    def __init__(self, operations: List[Operation]):
        self.__operations = operations

        self.__generated_departments = []

    def generate(self):
        if self.__generated_departments:
            return self.__generated_departments
        else:
            centers = WorkCentersGenerator(self.__operations).generate()
            self.__generated_departments.append(Department(centers))

            # was right_border
            # amount_of_departments = int((self.__max_amount_of_departments - self.__min_amount_of_departments) *
            #                             np.random.random() + self.__min_amount_of_departments)
            # # amount_of_departments = np.random.randint(self.__min_amount_of_departments, right_board)
            #
            # for i in range(amount_of_departments):
            #     centers = WorkCentersGenerator(self.__max_amount_of_machines_each).generate()
            #     dpt = Department("{}".format(i), centers)
            #     self.__generated_departments.append(dpt)

            return self.__generated_departments
