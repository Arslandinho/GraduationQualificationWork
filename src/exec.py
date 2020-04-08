# скрипт запуска генератора
from typing import List

from src.Entities.Operation import Operation
from src.Entities.WorkCenter import WorkCenter
from src.Generators.DepartmentsGenerator import DepartmentsGenerator
from src.Generators.OperationsGenerator import OperationsGenerator
from src.Generators.JobsGenerator import JobsGenerator

operations = JobsGenerator().generate()
jobs = JobsGenerator(operations).generate()

with(open("generated_data.txt", "w+", encoding="utf-8")) as data_file:
    for operation in operations:
        op_jobs: List[Operation] = operation.get_all_jobs()
        data_file.write(operation.get_operation_name() + " has a duration = " + str(operation.get_duration()) + ". ")
        data_file.write("Jobs, related to this operation: ")

        for job in op_jobs:
            data_file.write(str(job.get_duration()) + ", ")

        data_file.write("\n")

    data_file.write("\n")

    departments = DepartmentsGenerator(operations).generate()

    for dpt in departments:
        data_file.write("Amount of work centers generated: " + str(dpt.get_amount_of_work_centers()) + "\n")
        work_centers: List[WorkCenter] = dpt.get_all_work_centers()

        i = 1
        for work_center in work_centers:
            data_file.write("Work center #" + str(i) + " has " + str(work_center.get_amount_of_machines()) +
                            " machines\n")
            i += 1
            data_file.write("Operations that are done in this work center:\n")

            for operation in work_center.get_all_operations():
                data_file.write(str(operation.get_operation_name()) + " [")

                operation_jobs = operation.get_all_jobs()

                for job in operation_jobs:
                    data_file.write(str(job.get_duration()) + ", ")

                data_file.write("]\n")

            data_file.write("\n\n")
