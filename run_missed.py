import check_missing as check
import utils
from automate import run_model


missed = check.missing_cases()
all_samples = utils.read_csv_to_numpy("samples.csv")
print(missed)
for m in missed:
    x = all_samples[m - 1]
    r_out = x[1]
    r_in = x[1] - x[2]
    width = x[3]
    spoke_width = x[4]
    num_spokes = 4
    init_angle = x[5]
    E = 1e9
    load = 1e4
    run_model(index=m, r_out=r_out, r_in=r_in, width=width, spoke_width=spoke_width, num_spokes=num_spokes,
              init_angle=init_angle, E=E, load=load, meshsize=0.02, vis=False)
