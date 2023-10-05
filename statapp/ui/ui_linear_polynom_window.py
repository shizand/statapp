# -*- coding: utf-8 -*-
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


################################################################################
## Form generated from reading UI file 'linear_polynom_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LinearPolynomWindow(object):
    def setupUi(self, LinearPolynomWindow):
        if not LinearPolynomWindow.objectName():
            LinearPolynomWindow.setObjectName(u"LinearPolynomWindow")
        LinearPolynomWindow.resize(630, 400)
        self.gridLayout_2 = QGridLayout(LinearPolynomWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableView = QTableView(LinearPolynomWindow)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.residualVarianceLabel = QLabel(LinearPolynomWindow)
        self.residualVarianceLabel.setObjectName(u"residualVarianceLabel")

        self.gridLayout_3.addWidget(self.residualVarianceLabel, 0, 0, 1, 1)

        self.residualVarianceValueLabel = QLabel(LinearPolynomWindow)
        self.residualVarianceValueLabel.setObjectName(u"residualVarianceValueLabel")

        self.gridLayout_3.addWidget(self.residualVarianceValueLabel, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(LinearPolynomWindow)

        QMetaObject.connectSlotsByName(LinearPolynomWindow)
    # setupUi

    def retranslateUi(self, LinearPolynomWindow):
        LinearPolynomWindow.setWindowTitle(QCoreApplication.translate("LinearPolynomWindow", u"\u041b\u0438\u043d\u0435\u0439\u043d\u044b\u0439 \u043f\u043e\u043b\u0438\u043d\u043e\u043c", None))
        self.residualVarianceLabel.setText(QCoreApplication.translate("LinearPolynomWindow", u"\u041e\u0441\u0442\u0430\u0442\u043e\u0447\u043d\u0430\u044f \u0434\u0438\u0441\u043f\u0435\u0440\u0441\u0438\u044f:", None))
        self.residualVarianceValueLabel.setText(QCoreApplication.translate("LinearPolynomWindow", u"undefined", None))
    # retranslateUi
