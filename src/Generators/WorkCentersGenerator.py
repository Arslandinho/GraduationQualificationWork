from typing import List

from src.Entities.Job import Job
from src.Entities.WorkCenter import WorkCenter
from src.Generators.MachinesGenerator import MachinesGenerator
from src.Util.Constants.WorkCentersGeneratorConstants import WorkCentersGeneratorConstants
from src.Util.OperationsAllocationToWorkCenters import OperationsAllocationToWorkCenters as OperationsAllocate


class WorkCentersGenerator:
    def __init__(self, amount_to_generate: int, jobs: List[Job], load_factor, insert_type=0):
        self.__amount_to_generate = amount_to_generate
        self.__amount_of_machines_in_each = WorkCentersGeneratorConstants.AMOUNT_OF_MACHINES_IN_EACH
        self.__load_factor = load_factor
        self.__insert_type = insert_type

        self.__jobs = jobs
        self.__operations = []

        for job in self.__jobs:
            for operation in job.get_all_operations():
                self.__operations.append(operation)

        self.__generated_centers = []

    def generate(self) -> List[WorkCenter]:
        if self.__generated_centers:
            return self.__generated_centers
        else:
            calc = int(len(self.__operations) / self.__amount_to_generate)
            amount_of_operations_in_each = calc \
                if len(self.__operations) / self.__amount_to_generate == 0 \
                else calc + 1

            operations_by_work_centers = OperationsAllocate.insertion(self.__amount_to_generate,
                                                                      self.__operations,
                                                                      amount_of_operations_in_each,
                                                                      self.__insert_type)

            for i in range(self.__amount_to_generate):
                machines = MachinesGenerator(self.__amount_of_machines_in_each).generate()
                # load_factor = round(random.uniform(self.__load_factor_low_border, self.__load_factor_high_border), 2)

                self.__generated_centers.append(
                    WorkCenter(machines,
                               operations_by_work_centers.pop(0),
                               self.__load_factor,
                               self.__insert_type)
                )

            return self.__generated_centers
