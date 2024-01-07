# -*- coding: utf-8 -*-
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


################################################################################
## Form generated from reading UI file 'correlation_analysis_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CorrelationAnalysisWindow(object):
    def setupUi(self, CorrelationAnalysisWindow):
        if not CorrelationAnalysisWindow.objectName():
            CorrelationAnalysisWindow.setObjectName(u"CorrelationAnalysisWindow")
        CorrelationAnalysisWindow.resize(630, 400)
        self.gridLayout_2 = QGridLayout(CorrelationAnalysisWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableView = QTableView(CorrelationAnalysisWindow)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(CorrelationAnalysisWindow)

        QMetaObject.connectSlotsByName(CorrelationAnalysisWindow)
    # setupUi

    def retranslateUi(self, CorrelationAnalysisWindow):
        CorrelationAnalysisWindow.setWindowTitle(QCoreApplication.translate("CorrelationAnalysisWindow", u"\u041a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u0430\u043d\u0430\u043b\u0438\u0437", None))
    # retranslateUi
