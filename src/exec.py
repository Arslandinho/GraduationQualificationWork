# скрипт запуска генератора
from typing import List

from src.Entities.Operation import Operation
from src.Entities.WorkCenter import WorkCenter
from src.Generators.DepartmentsGenerator import DepartmentsGenerator
from src.Generators.OperationsGenerator import OperationsGenerator
from src.Generators.JobsGenerator import JobsGenerator

jobs = JobsGenerator().generate()
operations = OperationsGenerator(jobs).generate()

data_file = open("generated_data.txt", "w+", encoding="utf-8")

for job in jobs:
    job_operations: List[Operation] = job.get_all_operations()
    data_file.write(job.get_name() + " has a duration = " + str(job.get_duration()) + ". ")
    data_file.write("Operations, related to this job: ")

    for operation in job_operations:
        data_file.write(str(operation.get_duration()) + ", ")

    data_file.write("\n")

data_file.write("\n")

departments = DepartmentsGenerator(5, operations).generate()

for dpt in departments:
    data_file.write("Amount of work centers generated: " + str(dpt.get_amount_of_work_centers()) + "\n\n")
    work_centers: List[WorkCenter] = dpt.get_all_work_centers()

    discretions = []

    i = 1
    for work_center in work_centers:
        data_file.write("Work center #" + str(i) + " has " + str(work_center.get_amount_of_machines()) +
                        " machine(s)\n")
        data_file.write("Load factor is " + str(work_center.get_load_factor()) + "\n")
        i += 1
        data_file.write("Operations that are done in this work center:\n")

        j = 1
        for machine in work_center.get_all_machines():
            data_file.write("Machine #" + str(j) + " has operations:\n")
            j += 1

            for operation in machine.get_operations():
                data_file.write(str(operation.get_duration()) + ", ")

            data_file.write("\n")

        data_file.write("Overall amount of discretions: " + str(work_center.get_overall_amount_of_discretions()) + "\n")
        discretions.append(work_center.get_overall_amount_of_discretions())

        # k = 1
        # for disc_list in work_center.get_discretions():
        #     for disc in disc_list:
        #         data_file.write("Discretion #" + str(k) + ":")
        #         for op in disc.get_all_operations():
        #             data_file.write(str(op.get_duration()) + ", ")
        #
        #         k += 1
        #         data_file.write("\n")

        data_file.write("\n\n")

    data_file.write("Relative overall amount of discretions: " + str(max(discretions)))
