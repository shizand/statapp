#
# Copyright (c) 2024 Maxim Slipenko, Eugene Lazurenko.
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
import sympy as sp
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


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


def _prepareDataAndFeatures(data, degree):
    y = data[:, 0]
    x = data[:, 1:]
    polyFeatures = PolynomialFeatures(degree=degree, include_bias=False)
    xPoly = polyFeatures.fit_transform(x)
    return y, x, xPoly, polyFeatures


def _trainModelAndPredict(y, xPoly):
    model = LinearRegression(fit_intercept=True)
    model.fit(xPoly, y)
    predictions = model.predict(xPoly)
    return model, predictions


def _calculateStatistics(y, x, xPoly, predictions, model, polyFeatures):
    # Рассчитываем Среднеквадратическую ошибку (MSE) между фактическими и прогнозируемыми значениями
    mse = mean_squared_error(y, predictions)
    # Рассчитываем коэффициент детерминации R^2, который
    # показывает долю вариации зависимой переменной, объясненную моделью
    rSquared = r2_score(y, predictions)
    # Определяем количество наблюдений
    n = xPoly.shape[0]
    # Определяем количество предикторов (признаков) плюс один для свободного члена
    k = xPoly.shape[1] + 1
    # Рассчитываем F-статистику для оценки значимости всей регрессионной модели
    fStatistic = (rSquared / (k - 1)) / ((1 - rSquared) / (n - k))
    # Собираем параметры модели, включая свободный член и коэффициенты перед переменными
    params = np.hstack([model.intercept_, model.coef_])
    # Вычисляем остатки модели как разницу между фактическими и прогнозируемыми значениями
    residuals = y - predictions
    # Добавляем столбец единиц к матрице признаков для учета свободного члена в регрессионной модели
    xWithIntercept = np.hstack([np.ones((n, 1)), xPoly])
    # Рассчитываем дисперсии коэффициентов модели
    varB = mse * np.linalg.pinv(xWithIntercept.T @ xWithIntercept).diagonal()
    # Вычисляем стандартные ошибки коэффициентов, берем корень из дисперсий
    seB = np.sqrt(np.maximum(varB, 0))
    # Рассчитываем t-статистики для каждого коэффициента
    tStats = params / seB
    # Рассчитываем дисперсию остатков с поправкой на количество параметров
    residualVariance = np.var(residuals, ddof=k)
    # Рассчитываем скорректированную дисперсию остатков
    scaledResidualVariance = 1 - rSquared
    # Генерируем список мономов (названий признаков после
    # полиномиализации), добавляя константу для свободного члена
    monomials = ['c'] + list(
        polyFeatures.get_feature_names_out(['x' + str(i) for i in range(1, x.shape[1] + 1)])
    )
    # Заменяем пробелы на звездочки для представления умножения в названиях мономов
    monomials = [monomial.replace(' ', '*') for monomial in monomials]
    # Возвращаем рассчитанные статистики и названия мономов
    return params, tStats, residualVariance, scaledResidualVariance, rSquared, fStatistic, monomials



def _regressionAnalysis(data, degree):
    y, x, xPoly, polyFeatures = _prepareDataAndFeatures(
        data, degree
    )
    model, predictions = _trainModelAndPredict(y, xPoly)
    (params, tStats, residualVariance,
     scaledResidualVariance, rSquared, fStatistic, monomials) = (
        _calculateStatistics(
        y,
        x,
        xPoly,
        predictions,
        model,
        polyFeatures
    ))

    return RegressionResult(
        np.vstack((params, tStats)).T,
        residualVariance,
        scaledResidualVariance,
        rSquared,
        fStatistic,
        monomials
    )

def linearPolynom(data):
    return _regressionAnalysis(data, 1)


def squaredPolynom(data):
    return _regressionAnalysis(data, 2)


def prediction(inputData, result: RegressionResult):
    inputs = inputData[:, 1:]
    outputs = inputData[:, 0]

    params = result.paramsAndImportance[:, 0]

    expr = sp.sympify(' '.join(
        [
            f'{param}' if m == 'c' else f' + ({param}) * {m}'
            for param, m in zip(params, result.monomials)
        ]
    ))

    results = []

    numVars = inputs.shape[1]
    symbolsStr = ' '.join([f'x{i}' for i in range(1, numVars + 1)])
    symbols = sp.symbols(symbolsStr)

    for y, xValues in zip(outputs, inputs):
        subsDict = dict(zip(symbols, xValues))
        predictedResult = expr.subs(subsDict)
        difference = predictedResult - y

        results.append([y, predictedResult, difference, 0.0])

    results = np.array(results, dtype=np.float32)

    # Расчет среднего значения и стандартного отклонения разностей
    meanDifference = np.mean(results[:, 2])
    stdDifference = np.std(results[:, 2])

    # Установка флага 1.0, если разность выходит за пределы 3 стандартных отклонений
    for row in results:
        if abs(row[2] - meanDifference) > 3 * stdDifference:
            row[3] = 1.0

    return results
