# класс Завода (Цеха)
from typing import List

from src.Entities.Discrete import Discrete
from src.Entities.WorkCenter import WorkCenter


class Department:
    def __init__(self, work_centers: List[WorkCenter], name="Default_Name"):
        self.__name = name
        self.__work_centers = work_centers
        self.__plan_discretes = []

    def add_work_centers(self, work_center: WorkCenter):
        self.__work_centers.append(work_center)

    def get_all_work_centers(self) -> List[WorkCenter]:
        return self.__work_centers

    def get_amount_of_work_centers(self) -> int:
        return len(self.__work_centers)

    def get_name(self) -> str:
        return self.__name

    def get_plan(self):
        for work_center in self.__work_centers:
            self.__plan_discretes.append(work_center.get_overall_amount_of_discretes())
        return self.__plan_discretes

    def add_discretion(self, discretion: Discrete):
        self.__plan_discretes.append(discretion)
