import pandas as pd


def missing_cases():
    missed = []
    results_indices = pd.read_csv("results.csv")["index"].values
    sample_indices = pd.read_csv("samples.csv")["index"].values
    for i in range(len(sample_indices)):
        idx = sample_indices[i]
        if idx not in results_indices:
            missed.append(idx)
    return missed

m = missing_cases()
print(m)


