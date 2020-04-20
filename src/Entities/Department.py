# класс Завода (Цеха)
from typing import List

from src.Entities.Discretion import Discretion
from src.Entities.WorkCenter import WorkCenter


class Department:
    def __init__(self, work_centers: List[WorkCenter], name="Default_Name"):
        self.__name = name
        self.__work_centers = work_centers
        self.__plan_discretions = []

    def add_work_centers(self, work_center: WorkCenter):
        self.__work_centers.append(work_center)

    def get_all_work_centers(self) -> List[WorkCenter]:
        return self.__work_centers

    def get_amount_of_work_centers(self) -> int:
        return len(self.__work_centers)

    def get_name(self) -> str:
        return self.__name

    def get_plan(self):
        return self.__plan_discretions

    def add_discretion(self, discretion: Discretion):
        self.__plan_discretions.append(discretion)
