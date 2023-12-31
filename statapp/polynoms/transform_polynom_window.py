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
from PySide2.QtWidgets import QDialog, QHeaderView

from statapp.calculations import linearPolynom, prediction
from statapp.combo_delegate import ComboDelegate
from statapp.mathtex_header_view import MathTexHeaderView
from statapp.models.prediction_table_model import PreditionTableModel
from statapp.models.transform_polynom_model import TransformPolynomModel, TRANSFORMS
from statapp.ui.ui_polynom_window import Ui_PolynomWindow
from statapp.utils import addIcon


class TransformPolynomWindow(QDialog):
    def __init__(self, data):
        super().__init__()
        self.ui = Ui_PolynomWindow()
        self.ui.setupUi(self)
        addIcon(self)
        self.setWindowTitle("Преобразования")

        self.data = data
        result = linearPolynom(data)

        self.predictionModel = PreditionTableModel(prediction(data, result))
        self.ui.predictionTableView.setModel(self.predictionModel)
        header = self.ui.predictionTableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Создание столбца из нулей
        zeroCol = np.zeros((result.paramsAndImportance.shape[0], 1))
        # Добавление столбца к исходному массиву
        result.paramsAndImportance = np.column_stack((zeroCol, result.paramsAndImportance))

        # self.ui.tableView.setItemDelegate(FloatDelegate())
        self.ui.tableView.setItemDelegate(
            ComboDelegate(
                self.ui.tableView,
                list(TRANSFORMS.keys()),
                list(TRANSFORMS.keys()),
            )
        )
        self.model = TransformPolynomModel(result)
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setVerticalHeader(MathTexHeaderView(self.ui.tableView))
        header = self.ui.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.ui.residualVarianceValueLabel.setText(str(result.residualVariance))
        self.ui.scaledResidualVarianceValueLabel.setText(str(result.scaledResidualVariance))
        self.ui.fStatisticValueLabel.setText(str(result.fStatistic))
        self.ui.rSquaredValueLabel.setText(str(result.scaledResidualVariance))

        self.model.dataChanged.connect(self.on_data_changed)

    def on_data_changed(self):
        data = np.copy(self.data)
        print(len(data[0:]))
        for i in range(len(data[0:])):
            for j in range(1, len(data[i])):
                tr = self.model.data(self.model.createIndex(j, 0), Qt.DisplayRole)
                data[i][j] = TRANSFORMS[tr](data[i][j])

        self.rebuildData(data)

    def rebuildData(self, data):
        result = linearPolynom(data)
        self.predictionModel.updateAllData(prediction(data, result))
        zeroCol = np.zeros((result.paramsAndImportance.shape[0], 1))
        result.paramsAndImportance = np.column_stack((zeroCol, result.paramsAndImportance))
        self.model.updateAllData(result)
        self.ui.residualVarianceValueLabel.setText(str(result.residualVariance))
        self.ui.scaledResidualVarianceValueLabel.setText(str(result.scaledResidualVariance))
        self.ui.fStatisticValueLabel.setText(str(result.fStatistic))
        self.ui.rSquaredValueLabel.setText(str(result.scaledResidualVariance))
