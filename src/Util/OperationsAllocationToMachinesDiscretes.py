from src.Entities.Discrete import Discrete


class OperationsAllocationToMachinesDiscretes:
    @staticmethod
    # types: 0 - naive, 1 - optimal
    def insertion(machines, operations, discretes, load_factor, insert_type=0):
        if insert_type == 0:
            return \
                OperationsAllocationToMachinesDiscretes.naive_insertion(machines, operations, discretes, load_factor)
        elif insert_type == 1:
            return \
                OperationsAllocationToMachinesDiscretes.optimal_insertion(machines, operations, discretes, load_factor)

    @staticmethod
    def naive_insertion(machines, operations, discretes, load_factor):
        calc = int(len(operations) / len(machines))
        amount_of_operations_in_each = calc if len(operations) % len(machines) == 0 else calc + 1

        k = 0
        for machine in machines:
            left_border = amount_of_operations_in_each * k
            right_border = left_border + amount_of_operations_in_each

            machine.add_operations(operations[left_border:right_border])

            k += 1

        z = 1
        for machine in machines:
            discrete = Discrete(load_factor)
            temp_discretes = []
            i = 0
            for operation in machine.get_operations():
                lst = discrete.insert_operation(operation)

                temp_discretes.extend(lst)

                if i < len(machine.get_operations()) - 1:
                    discrete = temp_discretes.pop()
                    i += 1

            discretes.append(temp_discretes)
            z += 1

    @staticmethod
    def optimal_insertion(machines, operations, discretes, load_factor):
        pass
