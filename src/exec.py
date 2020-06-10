from statistics import mean

import matplotlib.pyplot as plt
import numpy as np

from src.Generators.DataGenerator import DataGenerator
from src.Util.Constants.GeneralConstants import GeneralConstants

data = DataGenerator().generate_data()

sum_n = data['generator'][0]
list_of_calcs_n = data['generator'][1]
plans_n = data['generator'][2]

sum_o = data['model'][0]
list_of_calcs_o = data['model'][1]
plans_o = data['model'][2]

f = open('aue.txt', "a+", encoding="utf-8")


def print_result():
    print("Keof = " + str(GeneralConstants.LOAD_FACTOR), file=f)
    print("Generator: ", file=f)
    print("Total sum: " + str(sum_n), file=f)
    print(list_of_calcs_n, file=f)

    print("\nImprecise model: ", file=f)
    print("Total sum: " + str(sum_o), file=f)
    print(list_of_calcs_o, file=f)

    print("\nAverage amount of discretes (generator): " + str(mean(plans_n)), file=f)

    print("Average amount of discretes (imprecise model): " + str(mean(plans_o)), file=f)


def draw_graphs():
    list_of_calcs_n_average = [np.mean(list_of_calcs_n)] * len(list_of_calcs_n)
    list_of_calcs_o_average = [np.mean(list_of_calcs_o)] * len(list_of_calcs_o)
    list_of_calcs_no_average = [(list_of_calcs_n_average[0] + list_of_calcs_o_average[0]) / 2] * \
                               len(list_of_calcs_o_average)

    print("\nDifference (times): " + str(list_of_calcs_n_average[0] / list_of_calcs_o_average[0]), file=f)
    print("\n", file=f)

    for i in range(100):
        plt.plot([i, i], [list_of_calcs_n[i], list_of_calcs_o[i]])

    plt.plot(list_of_calcs_n, 'black')
    plt.plot(list_of_calcs_o, 'black')
    plt.plot(list_of_calcs_n_average, 'red')
    plt.plot(list_of_calcs_o_average, 'green')
    plt.plot(list_of_calcs_no_average, 'blue')

    plt.show()


print_result()
draw_graphs()
