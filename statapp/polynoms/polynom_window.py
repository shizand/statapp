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
from PySide2.QtWidgets import QDialog, QHeaderView
from statapp.mathtex_header_view import MathTexHeaderView
from statapp.models.regression_result_model import RegressionResultModel
from statapp.ui.ui_polynom_window import Ui_PolynomWindow
from statapp.utils import addIcon, FloatDelegate


class PolynomWindow(QDialog):
    def __init__(self, result, windowTitle):
        super().__init__()
        self.ui = Ui_PolynomWindow()
        self.ui.setupUi(self)
        addIcon(self)
        self.setWindowTitle(windowTitle)

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
