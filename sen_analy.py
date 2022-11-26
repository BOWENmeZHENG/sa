from SALib.analyze import sobol
from automate import run_model
import sa_utils
import utils
import matplotlib.pyplot as plt
import numpy as np

# Generate samples
# variables = ['r_out', 'rim', 'width', 'spoke_width', 'init_angle']
variables = ['A', 'B', 'C', 'D', 'E']
bounds = [[0.25, 0.3], [0.05, 0.1], [0.05, 0.15], [0.02, 0.04], [0, 90]]
problem, param_values = sa_utils.gen_samples(variables=variables, bounds=bounds, N=512)

# Run_model
# with open('results.csv', 'w') as f_results:
#     f_results.write('index,max_s11\n')
# sample_data = utils.read_csv_to_numpy('samples.csv')
# index = 0
# for x in sample_data:
#     index += 1
#     r_out = x[1]
#     r_in = x[1] - x[2]
#     width = x[3]
#     spoke_width = x[4]
#     num_spokes = 4
#     init_angle = x[5]
#     E = 1e9
#     load = 1e4
#     run_model(index=index, r_out=r_out, r_in=r_in, width=width, spoke_width=spoke_width, num_spokes=num_spokes,
#               init_angle=init_angle, E=E, load=load, meshsize=0.02, vis=False)

# Perform analysis
results = utils.read_csv_to_numpy('results.csv')
results = results[results[:, 0].argsort()]
Y = np.squeeze(results[:, -1])
# print(results[3000])
Si = sobol.analyze(problem, Y)
ST, S1, S2 = Si.to_df()[0], Si.to_df()[1], Si.to_df()[2]

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(S1.index, S1['S1'], yerr=S1['S1_conf'], align='center', alpha=0.5, ecolor='black', capsize=10)
plt.tight_layout()
plt.show()
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar([str(index) for index in S2.index], S2['S2'], yerr=S2['S2_conf'],
       align='center', alpha=0.5, ecolor='black', capsize=10)
plt.tight_layout()
plt.show()
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(ST.index, ST['ST'], yerr=ST['ST_conf'], align='center', alpha=0.5, ecolor='black', capsize=10)
plt.tight_layout()
plt.show()

