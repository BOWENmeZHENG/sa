import numpy as np
import SALib.sample.sobol as sobol_sample
import utils
import fileinput
import sys


def gen_samples(variables: list, bounds: list, N: int):
    problem = {'num_vars': len(variables), 'names': variables, 'bounds': bounds}
    param_values = np.array(sobol_sample.sample(problem, N))
    np.savetxt('samples.csv', param_values, fmt='%.5f', delimiter=',')
    index = 0
    for line in fileinput.input(['samples.csv'], inplace=True):
        index += 1
        sys.stdout.write(f'{index},{line}')
    header = 'index,'
    for i, name in enumerate(problem['names']):
        header += name
        if i != len(problem['names']) - 1:
            header += ','
    utils.line_prepender('samples.csv', header)
    return problem, param_values


