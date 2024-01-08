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
from PySide2 import QtCore
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QDialog, QHeaderView

from statapp.calculations import correlationAnalysis
from statapp.constants import NUMBERS_PRECISION
from statapp.mathtex_header_view import MathTexHeaderView
from statapp.models.correlation_analysis_model import CorrelationAnalysisModel
from statapp.ui.ui_correlation_analysis_window import Ui_CorrelationAnalysisWindow
from statapp.utils import resourcePath


class CorrelationAnalysisWindow(QDialog):
    def __init__(self, data):
        super().__init__()
        self.ui = Ui_CorrelationAnalysisWindow()
        self.ui.setupUi(self)

        res = correlationAnalysis(data)
        self.model = CorrelationAnalysisModel(res.round(NUMBERS_PRECISION))
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setVerticalHeader(
            MathTexHeaderView(self.ui.tableView)
        )
        self.ui.tableView.setHorizontalHeader(
            MathTexHeaderView(self.ui.tableView,orientation=QtCore.Qt.Horizontal)
        )
        header = self.ui.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        icon = QIcon()
        icon.addFile(resourcePath("ui/images/logo.ico"), QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
