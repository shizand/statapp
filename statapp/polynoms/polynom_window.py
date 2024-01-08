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
import numpy as np
from PySide2.QtWidgets import QDialog, QHeaderView
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from statapp.calculations import prediction
from statapp.mathtex_header_view import MathTexHeaderView
from statapp.models.prediction_table_model import PreditionTableModel
from statapp.models.regression_result_model import RegressionResultModel
from statapp.ui.ui_polynom_window import Ui_PolynomWindow
from statapp.utils import addIcon, FloatDelegate


matplotlib.use('Qt5Agg')

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot()
        super().__init__(fig)

class PolynomWindow(QDialog):
    def __init__(self, data, result, windowTitle):
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

        predictionResult = prediction(data, result)

        self.predictionModel = PreditionTableModel(predictionResult)
        self.ui.predictionTableView.setModel(self.predictionModel)
        header = self.ui.predictionTableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        sc = MplCanvas(self, width=5, height=4, dpi=100)

        xAxes = np.array(range(len(data[:, 0])))

        realY = predictionResult[:, 0]
        calculatedY = predictionResult[:, 1]

        print(xAxes)
        print(realY)
        print(calculatedY)

        sc.axes.scatter(xAxes, realY)

        # xnew = np.linspace(xAxes.min(), xAxes.max(), 300)
        # gfg = scipy.interpolate.make_interp_spline(xAxes, y, k=3)
        # y_new = gfg(xnew)

        sc.axes.plot(xAxes, calculatedY)

        self.ui.plotContainer.addWidget(sc)
