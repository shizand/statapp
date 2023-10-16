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
from dataclasses import dataclass

import numpy as np
import pandas as pd
from statapp._vendor.multipolyfit import multipolyfit, mk_sympy_function

DIRECT_LINK = 0
INDIRECT_LINK = 1


def generateYValues(mean, std, count):
    return np.random.normal(mean, std, size=(count, 1))


def generateXValues(mean, std, typeConnection, yColumn):
    yMean = np.mean(yColumn)
    values = []
    for y in yColumn:
        raz = np.abs(mean - np.random.normal(mean, std))
        if typeConnection == INDIRECT_LINK:
            raz *= -1
        if y > yMean:
            x = mean + raz
        elif y < yMean:
            x = mean - raz
        else:
            x = mean
        values.append(x)

    res = np.array(values)
    return res.reshape(len(res), 1)


def varianceAnalysis(data):
    return np.array([
        [np.mean(col), np.std(col), np.min(col), np.max(col)] for col in data.T
    ])


def correlationAnalysis(data):
    return pd.DataFrame(data).corr().to_numpy()

@dataclass()
class LinearPolynomResult:
    paramsAndImportance: np.ndarray
    residualVariance: np.float64


def linearPolynom(inputData) -> LinearPolynomResult:
    x = inputData[:, 1:]
    y = inputData[:, 0]
    data = pd.DataFrame(x)
    data.insert(0, 'const', 1)
    # ---
    result = np.linalg.lstsq(data, y, rcond=None)
    # Коэффициенты регрессии
    params = result[0]
    # Остатки
    residues = result[1]

    # Степень свободы
    dof = len(data) - len(params)
    mse = residues / dof
    cov = mse * np.diagonal(np.linalg.inv(data.T @ data))
    se = np.sqrt(cov)
    tStatistics = params / se

    # возможно стоит сделать через np.reshape + np.concatenate
    out = pd.DataFrame()
    out[0] = params
    out[1] = tStatistics

    return LinearPolynomResult(
        out.to_numpy(),
        np.float64(mse[0])
    )

def squaredPolynom(inputData) -> LinearPolynomResult:
    x = inputData[:, 1:]
    y = inputData[:, 0]
    data = pd.DataFrame(x)
    betas, powers = multipolyfit(x, y, 2, powers_out=True)
    res = mk_sympy_function(betas, powers)
    print(data)
    print(res)

    return powers
