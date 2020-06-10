from typing import List

import time

from src.Entities.Department import Department
from src.Entities.Job import Job
from src.Entities.Operation import Operation
from src.Generators.DepartmentsGenerator import DepartmentsGenerator
from src.Generators.OperationsGenerator import OperationsGenerator
from src.Generators.JobsGenerator import JobsGenerator
from src.Util.Constants.GeneralConstants import GeneralConstants


class DataGenerator:
    def __init__(self):
        self.__jobs: List[List[Job]] = []
        self.__operations: List[List[Operation]] = []
        self.__departments_naive: List[Department] = []
        self.__departments_optimal: List[Department] = []

    def __generate(self):
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

    def __calc(self, dprtmnt, flag=0):
        discretes_operations_dict = {}
        for jobs_list in self.__jobs:
            for job in jobs_list:
                discretes_operations_dict[job.get_name()] = []

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
            init_amount_of_intervals = self.__get_right_job(job_name).get_amount_of_intervals()
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

                actual_amount_of_intervals = max(list(res_as_dict.values()))

            sum_of_lag += max(0, actual_amount_of_intervals + 1 - init_amount_of_intervals)

        return sum_of_lag

    def __get_right_job(self, key):
        for jobs_list in self.__jobs:
            for job in jobs_list:
                if job.get_name() == key:
                    return job

    def get_generated_jobs(self):
        if not self.__jobs:
            self.__generate()

        return self.__jobs

    def get_generated_operations(self):
        if not self.__operations:
            self.__generate()

        return self.__operations

    def generate_data(self):
        self.__generate()

        sum_n = 0
        list_of_calcs_n = []
        for dpt in self.__departments_naive:
            calc_result = self.__calc(dpt)
            sum_n += calc_result
            list_of_calcs_n.append(calc_result)

        sum_o = 0
        list_of_calcs_o = []
        for dpt in self.__departments_optimal:
            calc_result = self.__calc(dpt, 1)
            sum_o += calc_result
            list_of_calcs_o.append(calc_result)

        plans_n = []
        for dpt in self.__departments_naive:
            plan = len(max(dpt.get_plan(), key=len))
            plans_n.append(plan)

        plans_o = []
        for dpt in self.__departments_optimal:
            plan = len(max(dpt.get_plan(), key=len))
            plans_o.append(plan)

        return {'generator': [sum_n, list_of_calcs_n, plans_n], 'model': [sum_o, list_of_calcs_o, plans_o]}
