import pandas as pd


def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)


def read_csv_to_numpy(filename: str):
    data = pd.read_csv(filename)
    return data.to_numpy()
