from typing import List

from src.Entities.Job import Job
from src.Entities.Operation import Operation
from src.Entities.WorkCenter import WorkCenter
from src.Generators.MachinesGenerator import MachinesGenerator
from src.Util.Constants.WorkCentersGeneratorConstants import WorkCentersGeneratorConstants
from src.Util.OperationsAllocationToDiscretes \
    import OperationsAllocationToDiscretes as OperationsAllocateDiscretes
from src.Util.OperationsAllocationToWorkCenters \
    import OperationsAllocationToWorkCenters as OperationsAllocateCenters


class WorkCentersGenerator:
    def __init__(self, amount_to_generate: int, jobs: List[Job], load_factor, insert_type=0):
        self.__amount_to_generate = amount_to_generate
        self.__amount_of_machines_in_each = WorkCentersGeneratorConstants.AMOUNT_OF_MACHINES_IN_EACH
        self.__load_factor = load_factor
        self.__insert_type = insert_type

        self.__jobs: List[Job] = jobs
        self.__operations: List[Operation] = []

        for job in self.__jobs:
            for operation in job.get_all_operations():
                self.__operations.append(operation)

        self.__generated_centers: List[WorkCenter] = []

    def generate(self) -> List[WorkCenter]:
        if self.__generated_centers:
            return self.__generated_centers
        else:
            # распределение операций по рабочим центрам
            # параметр insert_type влияет на то, как будут распределены задачи:
            # 0 - по порядку
            # 1 - методом оптимальной вставки
            operations_by_work_centers = OperationsAllocateCenters.insertion(self.__amount_to_generate,
                                                                             self.__operations,
                                                                             self.__insert_type)

            for i in range(self.__amount_to_generate):
                machines = MachinesGenerator(self.__amount_of_machines_in_each).generate()
                # load_factor =
                # round(random.uniform(self.__load_factor_low_border, self.__load_factor_high_border), 2)

                # распределение операций по дискретам
                self.__generated_centers.append(
                    WorkCenter(machines,
                               operations_by_work_centers.pop(0),
                               self.__load_factor)
                )

            discretes = OperationsAllocateDiscretes.insertion(self.__generated_centers,
                                                              self.__load_factor,
                                                              self.__insert_type)

            for center in self.__generated_centers:
                center.add_discretes(discretes.pop(0))

            return self.__generated_centers
