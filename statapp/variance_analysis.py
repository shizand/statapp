#
# Copyright (c) 2023 Maxim Slipenko, Euegene Lazurenko.
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
# along with this program. If not, see <http://www.gnu.org/licenses/>.#
from PySide2.QtWidgets import QDialog, QHeaderView

from statapp.calculations import variance_analysis
from statapp.models.variance_analysis_model import VarianceAnalysisModel
from statapp.ui.ui_variance_analysis_window import Ui_VarianceAnalysisWindow


class VarianceAnalysisWindow(QDialog):
    def __init__(self, data):
        super().__init__()
        self.ui = Ui_VarianceAnalysisWindow()
        self.ui.setupUi(self)

        res = variance_analysis(data)
        self.model = VarianceAnalysisModel(res.round(2))
        self.ui.tableView.setModel(self.model)
        header = self.ui.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
