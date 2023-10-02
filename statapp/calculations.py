import numpy as np

DIRECT_LINK = 0
INDIRECT_LINK = 1

def generate_x_values(mean, std, typeConnection, y):
    yMean = np.mean(y)
    values = []
    for cur_y in y:
        k = np.abs(cur_y / yMean)
        if k > 1:
            k = 2 - 1 / k
        if typeConnection == INDIRECT_LINK:
            k = 1 / k
        if std == 0:
            k = 1

        x = np.random.normal(mean * (k ** 3), std * k)
        values.append(x)
        # if (x > gfw.mat and cur_y > yMat) or (x < gfw.mat and cur_y < yMat):
        #     dd = np.append(dd, 1)
        # else:
        #     dd = np.append(dd, 0)

    # x_arr = x_arr.reshape(len(x_arr), 1)

    return np.array(values)

def variance_analysis(data):
    return np.array([
        [np.mean(col), np.std(col), np.min(col), np.max(col)] for col in data.T
    ])
