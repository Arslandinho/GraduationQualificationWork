from typing import List

import time
from pathlib import Path

from src.Entities.Department import Department
from src.Entities.Job import Job
from src.Entities.Operation import Operation
from src.Generators.DepartmentsGenerator import DepartmentsGenerator
from src.Generators.OperationsGenerator import OperationsGenerator
from src.Generators.JobsGenerator import JobsGenerator
from src.Util.Constants.GeneralConstants import GeneralConstants


class DataGenerator:
    def __init__(self):
        # self.__insert_type = insert_type

        self.__jobs: List[List[Job]] = []
        self.__operations: List[List[Operation]] = []
        self.__departments_naive: List[Department] = []
        self.__departments_optimal: List[Department] = []

    def generate(self):
        for i in range(1000):
            jobs = JobsGenerator().generate()
            operations = OperationsGenerator(jobs).generate()

            self.__jobs.append(jobs)
            self.__operations.append(operations)

        start_time = time.time()
        for i in range(1000):
            self.__departments_naive.extend(
                DepartmentsGenerator(
                    GeneralConstants.WORK_CENTERS_TO_GENERATE_IN_EACH_DEPARTMENT,
                    self.__jobs[i],
                    0).generate()
            )
        print("Naive algorithm finished within \n%s seconds" % (time.time() - start_time))

        start_time = time.time()
        for i in range(1000):
            self.__departments_optimal.extend(
                DepartmentsGenerator(
                    GeneralConstants.WORK_CENTERS_TO_GENERATE_IN_EACH_DEPARTMENT,
                    self.__jobs[i],
                    1).generate()
            )
        print("Optimal algorithm finished within \n%s seconds" % (time.time() - start_time))

    def get_generated_jobs(self):
        if not self.__jobs:
            self.generate()

        return self.__jobs

    def get_generated_operations(self):
        if not self.__operations:
            self.generate()

        return self.__operations

    # def get_generated_departments(self):
    #     if not self.__departments:
    #         self.generate()
    #
    #     return self.__departments

    def print_data_to_file(self, path_to_file="../generated_data.txt"):
        self.generate()

        import os
        os.remove(path_to_file)

        data_file = open(path_to_file, "a+", encoding="utf-8")

        # for list_of_jobs in self.__jobs:
        #     for job in list_of_jobs:
        #         job_operations: List[Operation] = job.get_all_operations()
        #         data_file.write(job.get_name() + " has a duration = " + str(job.get_duration()) + ". ")
        #         data_file.write("Operations, related to this job: ")
        #
        #         for operation in job_operations:
        #             data_file.write(str(operation.get_duration()) + ", ")
        #
        #         data_file.write("\n")
        #
        # data_file.write("\n")
        #
        # for dpt in departments:
        #     data_file.write("Amount of work centers generated: " + str(dpt.get_amount_of_work_centers()) + "\n\n")
        #     work_centers: List[WorkCenter] = dpt.get_all_work_centers()
        #
        #     i = 1
        #     for work_center in work_centers:
        #         data_file.write("Work center #" + str(i) + " has " + str(work_center.get_amount_of_machines()) +
        #                         " machine(s)\n")
        #         data_file.write("Load factor is " + str(work_center.get_load_factor()) + "\n")
        #         i += 1
        #         data_file.write("Operations that are done in this work center:\n")
        #
        #         j = 1
        #         for machine in work_center.get_all_machines():
        #             data_file.write("Machine #" + str(j) + " has operations:\n")
        #             j += 1
        #
        #             for operation in machine.get_operations():
        #                 data_file.write(str(operation.get_duration()) + ", ")
        #
        #             data_file.write("\n")
        #
        # data_file.write("Overall amount of discretes: " + str(work_center.get_overall_amount_of_discretes()) +
        # "\n\n")

        plans = []
        for dpt in self.__departments_naive:
            plan = len(max(dpt.get_plan(), key=len))
            # data_file.write("Relative overall amount of discretes: " + str(plan) + "\n")
            plans.append(plan)

        data_file.write("Max amount of discretes (naive algorithm): " + str(max(plans)) + "\n")

        plans = []
        for dpt in self.__departments_optimal:
            plan = len(max(dpt.get_plan(), key=len))
            # data_file.write("Relative overall amount of discretes: " + str(plan) + "\n")
            plans.append(plan)

        data_file.write("Max amount of discretes (optimal algorithm): " + str(max(plans)) + "\n")


DataGenerator().print_data_to_file()
