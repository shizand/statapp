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
from PySide2.QtCore import Slot, QModelIndex
from PySide2.QtWidgets import QDialog, QHeaderView

from statapp.calculations import linearPolynom
from statapp.mathtex_header_view import MathTexHeaderView
from statapp.models.regression_result_model import RegressionResultModel
from statapp.ui.ui_transform_polynom_window import Ui_PolynomWindow
from statapp.utils import addIcon, FloatDelegate


class TransformPolynomWindow(QDialog):
    def __init__(self, data):
        super().__init__()
        self.ui = Ui_PolynomWindow()
        self.ui.setupUi(self)
        addIcon(self)
        self.setWindowTitle("Преобразования")

        self.data = data
        result = linearPolynom(data)

        self.model = RegressionResultModel(result)
        self.ui.tableView.setItemDelegate(FloatDelegate())
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setVerticalHeader(MathTexHeaderView(self.ui.tableView))
        header = self.ui.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.ui.residualVarianceValueLabel.setText(str(result.residualVariance))
        self.ui.scaledResidualVarianceValueLabel.setText(str(result.scaledResidualVariance))
        self.ui.fStatisticValueLabel.setText(str(result.fStatistic))
        self.ui.rSquaredValueLabel.setText(str(result.scaledResidualVariance))

    @Slot(QModelIndex)
    def on_listTransforms_clicked(self, index):
        item = self.ui.listTransforms.currentItem().text()

        data = np.copy(self.data)
        for i in range(len(data[0:])):
            for j in range(1, len(data[i])):
                func = defaultX

                if item == 'sin(x)':
                    func = np.sin
                elif item == 'cos(x)':
                    func = np.cos
                elif item == 'log(x)':
                    func = np.log
                elif item == 'exp(x)':
                    func = np.exp

                data[i][j] = func(data[i][j])

        self.rebuildData(data)

    def rebuildData(self, data):
        result = linearPolynom(data)

        self.model = RegressionResultModel(result)
        self.ui.tableView.setItemDelegate(FloatDelegate())
        self.ui.tableView.setModel(self.model)
        #self.ui.tableView.setVerticalHeader(MathTexHeaderView(self.ui.tableView))
        header = self.ui.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.ui.residualVarianceValueLabel.setText(str(result.residualVariance))
        self.ui.scaledResidualVarianceValueLabel.setText(str(result.scaledResidualVariance))
        self.ui.fStatisticValueLabel.setText(str(result.fStatistic))
        self.ui.rSquaredValueLabel.setText(str(result.scaledResidualVariance))


def defaultX(x):
    return x
