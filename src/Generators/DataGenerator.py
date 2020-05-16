import math
from typing import List

import time

import numpy as np

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
        for i in range(100):
            jobs = JobsGenerator().generate()
            operations = OperationsGenerator(jobs).generate()

            self.__jobs.append(jobs)
            self.__operations.append(operations)

        start_time = time.time()
        for i in range(100):
            self.__departments_naive.extend(
                DepartmentsGenerator(
                    GeneralConstants.WORK_CENTERS_TO_GENERATE_IN_EACH_DEPARTMENT,
                    self.__jobs[i],
                    0).generate()
            )
        print("Naive algorithm finished within \n%s seconds" % (time.time() - start_time))

        start_time = time.time()
        for i in range(100):
            self.__departments_optimal.extend(
                DepartmentsGenerator(
                    GeneralConstants.WORK_CENTERS_TO_GENERATE_IN_EACH_DEPARTMENT,
                    self.__jobs[i],
                    1).generate()
            )
        print("Optimal algorithm finished within \n%s seconds" % (time.time() - start_time))

    def calc(self, dprtmnt, flag=0):
        discretes_operations_dict = {}
        for jobs_list in self.__jobs:
            for job in jobs_list:
                discretes_operations_dict[job.get_name()] = []

        # for dp in dprtmnt:
        wcs = dprtmnt.get_all_work_centers()
        for j in range(len(wcs)):
            discrs = wcs[j].get_discretes()
            for i in range(len(discrs)):
                for operat in discrs[i].get_all_operations():
                    if flag == 0:
                        discretes_operations_dict[operat.get_job_name()].append((j, i))
                    elif flag == 1:
                        discretes_operations_dict[operat.get_job_name()].append((j, 1))

        discretes_operations_dict_upd = {}
        for k in discretes_operations_dict.keys():
            if discretes_operations_dict[k]:
                discretes_operations_dict_upd[k] = discretes_operations_dict[k]

        sum_of_lag = 0
        for job_name in discretes_operations_dict_upd.keys():
            init_amount_of_intervals = self.get_right_job(job_name).get_amount_of_intervals()
            opers = discretes_operations_dict_upd[job_name]

            res = [tuple(sub) for sub in opers]
            res_as_dict = {}

            actual_amount_of_intervals = 0
            if flag == 0:
                actual_amount_of_intervals = len(list(set(res)))
            elif flag == 1:
                for r in res:
                    if r[0] in res_as_dict:
                        res_as_dict[r[0]] = res_as_dict[r[0]] + 1
                    else:
                        res_as_dict[r[0]] = 1

                # x = {k: v for k, v in res_as_dict.items() if v is not None}
                # print(len(x))
                actual_amount_of_intervals = max(list(res_as_dict.values()))

            with open('../result.txt', 'a+', encoding="utf-8") as f:
                print("flag: " + str(flag), file=f)
                print("actual_amount_of_intervals: " + str(actual_amount_of_intervals), file=f)
                print("init_amount_of_intervals: " + str(init_amount_of_intervals), file=f)
                print("\n", file=f)

            sum_of_lag += max(0, actual_amount_of_intervals + 1 - init_amount_of_intervals)

        return sum_of_lag

    def get_right_job(self, key):
        for jobs_list in self.__jobs:
            for job in jobs_list:
                if job.get_name() == key:
                    return job

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

        print("\nnaive: ")
        sum_n = 0
        list_of_calcs_n = []
        for dpt in self.__departments_naive:
            calc_result = self.calc(dpt)
            sum_n += calc_result
            list_of_calcs_n.append(calc_result)
        print("sum naive: " + str(sum_n))
        print(list_of_calcs_n)

        print("\noptimal: ")
        sum_o = 0
        list_of_calcs_o = []
        for dpt in self.__departments_optimal:
            calc_result = self.calc(dpt, 1)
            sum_o += calc_result
            list_of_calcs_o.append(calc_result)
        print("sum optimal: " + str(sum_o))
        print(list_of_calcs_o)

        import os
        # os.remove(path_to_file)

        data_file = open(path_to_file, "w+", encoding="utf-8")

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
