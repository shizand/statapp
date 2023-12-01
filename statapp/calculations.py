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
from statapp._vendor.multipolyfit import multipolyfit, getTerms

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
class RegressionResult:
    """
    Attributes:
        paramsAndImportance (np.ndarray): Параметры модели. Первая колонка -
        residualVariance (np.float64): Остаточная дисперсия
        scaledResidualVariance (np.float64): Остаточная дисперсия (масштабированная)
        monomials (list): Список одночленов в строковом виде без коэффициентов. Свободный член - c
    """
    paramsAndImportance: np.ndarray
    residualVariance: np.float64
    scaledResidualVariance: np.float64
    rSquared: np.float64
    fStatistic: np.float64
    monomials: list


def commonPolynom(inputData, deg) -> RegressionResult:
    x = inputData[:, 1:]
    y = inputData[:, 0]
    result, powers, data = multipolyfit(x, y, deg, full=True)
    (out, mse, scaledResidualVariance,
     rSquared, fStatistic) = calculateStats(data, result[0], result[1], y)

    return RegressionResult(
        out.to_numpy(),
        np.float64(mse),
        np.float64(scaledResidualVariance),
        np.float64(rSquared),
        np.float64(fStatistic),
        ['c' if str(x) == '1' else str(x) for x in getTerms(powers)]
    )


def linearPolynom(inputData) -> RegressionResult:
    return commonPolynom(inputData, 1)


def squaredPolynom(inputData) -> RegressionResult:
    return commonPolynom(inputData, 2)


def calculateStats(data, params, residues, y):
    # pylint: disable-msg=too-many-locals

    k = len(params)  # Количество оцениваемых параметров (коэффициентов)
    n = len(data)  # Количество наблюдений

    # Степень свободы (degrees of freedom) для остатков
    dof = n - k  # Количество наблюдений минус количество оцениваемых параметров
    # Остаточная дисперсия (Mean Squared Error, MSE)
    mse = residues / dof
    # Среднее значение остатков
    meanResiduals = np.sum(residues) / dof
    # Масштабированная остаточная дисперсия
    scaledResidualVariance = residues / meanResiduals ** 2
    # Ковариационная матрица коэффициентов
    cov = mse * np.diagonal(np.linalg.inv(data.T @ data))
    # Стандартные ошибки коэффициентов
    se = np.sqrt(cov)
    # T-статистики для каждого коэффициента регрессии
    tStatistics = params / se

    # R-squared (коэффициент множественной детерминации)
    sst = np.sum((y - np.mean(y)) ** 2)  # Сумма квадратов отклонений
    rSquared = 1 - (mse[0] / sst)

    # F-statistic (статистика Фишера)
    fStatistic = (rSquared / (k - 1)) / ((1 - rSquared) / (n - k))

    out = pd.DataFrame()
    out[0] = params
    out[1] = tStatistics

    return out, mse[0], scaledResidualVariance, rSquared, fStatistic
