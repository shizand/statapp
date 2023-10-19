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

from statapp.calculations import squaredPolynom
from statapp.models.squared_polynom_model import SquaredPolynomModel
from statapp.ui.ui_squared_polynom_window import Ui_SquaredPolynomWindow
from statapp.utils import addIcon


class SquaredPolynomWindow(QDialog):
    def __init__(self, data):
        super().__init__()
        self.ui = Ui_SquaredPolynomWindow()
        self.ui.setupUi(self)
        addIcon(self)

        result = squaredPolynom(data)

        # Не округляем, т.к. может получиться коэффициент = 0 и значимый (t-критерий)
        self.model = SquaredPolynomModel(result.paramsAndImportance)
        self.model.powers = result.powers
        self.ui.tableView.setModel(self.model)
        header = self.ui.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.ui.residualVarianceValueLabel.setText(str(result.residualVariance))
