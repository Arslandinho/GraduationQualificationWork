from src.Util.Constants.OperationsGeneratorConstants import OperationsGeneratorConstants


class JobsGeneratorConstants:
    MIN_AMOUNT_OF_JOBS = 5
    MAX_AMOUNT_OF_JOBS = 15

    # от 1 до 4 операций в каждой работе
    MIN_DURATION_TIME = OperationsGeneratorConstants.MIN_DURATION
    MAX_DURATION_TIME = OperationsGeneratorConstants.MAX_DURATION * 4
