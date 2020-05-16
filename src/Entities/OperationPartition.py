from src.Entities.Operation import Operation


class OperationPartition:
    def __init__(self, operation: Operation, duration: float):
        duration = round(duration, 1)
        self.__new_operation = Operation(duration)
        self.__new_operation.set_job_name(operation.get_job_name())

        operation.add_partition(self.__new_operation)

    def get_new_operation(self):
        return self.__new_operation
