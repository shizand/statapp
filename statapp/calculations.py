#
# Copyright (c) 2023 Maxim Slipenko, Eugene Lazurenko.
#
# This file is part of Statapp
# (see https://github.com/shizand/statapp).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
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
    return pd.DataFrame(data).corr().to_numpy()
