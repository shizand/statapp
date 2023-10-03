import numpy as np
import pandas as pd

DIRECT_LINK = 0
INDIRECT_LINK = 1


def generate_x_values(mean, std, typeConnection, y):
    yMean = np.mean(y)
    values = []
    for cur_y in y:
        raz = np.abs(mean - np.random.normal(mean, std))
        if typeConnection == INDIRECT_LINK:
            raz *= -1
        if cur_y > yMean:
            x = mean + raz
        elif cur_y < yMean:
            x = mean - raz
        else:
            x = mean
        values.append(x)
    return np.array(values)


def variance_analysis(data):
    return np.array([
        [np.mean(col), np.std(col), np.min(col), np.max(col)] for col in data.T
    ])


def correlation_analysis(data):
    return pd.DataFrame(data).corr().round(len(data[-1])).to_numpy()