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
from PySide2.QtCore import Qt

from statapp.models.editable_table_model import EditableTableModel
from statapp.models.regression_result_model import RegressionResultModel

def defaultX(x):
    return x

TRANSFORMS = {
    '-': defaultX,
    'sin(x)': np.sin,
    'cos(x)': np.cos,
    'log(x)': np.log,
    'exp(x)': np.exp,
}

class TransformPolynomModel(RegressionResultModel, EditableTableModel):

    def __init__(self, result):
        super().__init__(result)
        n = result.paramsAndImportance.shape[0]

        self._transforms = ['-'] * n

    def columnCount(self, index):
        return 3

    def updateAllData(self, data):
        d = data.paramsAndImportance
        self._monomials = data.monomials
        super().updateAllData(d)

    def flags(self, index):
        if index.column() == 0 and index.row() != 0:
            return EditableTableModel.flags(self, index)
        return RegressionResultModel.flags(self, index)

    def data(self, index, role):
        if role == Qt.DisplayRole and index.column() == 0:
            return self._transforms[index.row()]
        return super().data(index, role)

    def setData(self, index, value, role):
        if role == Qt.EditRole and index.column() == 0:
            self._transforms[index.row()] = value
            topLeftIndex = self.createIndex(index.row(), 0)
            bottomRightIndex = self.createIndex(index.row(), 0)
            self.dataChanged.emit(topLeftIndex, bottomRightIndex)
            return True
        return super().setData(index, value, role)

    def getHorizontalHeader(self):
        return ['Преобразования'] + super().getHorizontalHeader()
