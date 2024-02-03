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
## Form generated from reading UI file 'polynom_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PolynomWindow(object):
    def setupUi(self, PolynomWindow):
        if not PolynomWindow.objectName():
            PolynomWindow.setObjectName(u"PolynomWindow")
        PolynomWindow.resize(537, 444)
        self.gridLayout_2 = QGridLayout(PolynomWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(PolynomWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        self.model = QWidget()
        self.model.setObjectName(u"model")
        self.gridLayout_3 = QGridLayout(self.model)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableView = QTableView(self.model)
        self.tableView.setObjectName(u"tableView")
        self.tableView.horizontalHeader().setMinimumSectionSize(40)
        self.tableView.verticalHeader().setMinimumSectionSize(40)
        self.tableView.verticalHeader().setDefaultSectionSize(40)

        self.gridLayout.addWidget(self.tableView, 1, 3, 1, 1)

        self.polynomResult = QGridLayout()
        self.polynomResult.setObjectName(u"polynomResult")
        self.polynomResult.setContentsMargins(-1, 10, -1, -1)
        self.residualVarianceValueLabel = QLabel(self.model)
        self.residualVarianceValueLabel.setObjectName(u"residualVarianceValueLabel")

        self.polynomResult.addWidget(self.residualVarianceValueLabel, 0, 1, 1, 1)

        self.scaledResidualVarianceValueLabel = QLabel(self.model)
        self.scaledResidualVarianceValueLabel.setObjectName(u"scaledResidualVarianceValueLabel")

        self.polynomResult.addWidget(self.scaledResidualVarianceValueLabel, 1, 1, 1, 1)

        self.fStatisticLabel = QLabel(self.model)
        self.fStatisticLabel.setObjectName(u"fStatisticLabel")

        self.polynomResult.addWidget(self.fStatisticLabel, 2, 0, 1, 1)

        self.residualVarianceLabel = QLabel(self.model)
        self.residualVarianceLabel.setObjectName(u"residualVarianceLabel")

        self.polynomResult.addWidget(self.residualVarianceLabel, 0, 0, 1, 1)

        self.scaledResidualVarianceLabel = QLabel(self.model)
        self.scaledResidualVarianceLabel.setObjectName(u"scaledResidualVarianceLabel")

        self.polynomResult.addWidget(self.scaledResidualVarianceLabel, 1, 0, 1, 1)

        self.rSquaredLabel = QLabel(self.model)
        self.rSquaredLabel.setObjectName(u"rSquaredLabel")

        self.polynomResult.addWidget(self.rSquaredLabel, 3, 0, 1, 1)

        self.fStatisticValueLabel = QLabel(self.model)
        self.fStatisticValueLabel.setObjectName(u"fStatisticValueLabel")

        self.polynomResult.addWidget(self.fStatisticValueLabel, 2, 1, 1, 1)

        self.rSquaredValueLabel = QLabel(self.model)
        self.rSquaredValueLabel.setObjectName(u"rSquaredValueLabel")

        self.polynomResult.addWidget(self.rSquaredValueLabel, 3, 1, 1, 1)


        self.gridLayout.addLayout(self.polynomResult, 2, 3, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.tabWidget.addTab(self.model, "")
        self.prediction = QWidget()
        self.prediction.setObjectName(u"prediction")
        self.gridLayout_4 = QGridLayout(self.prediction)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.predictionTableView = QTableView(self.prediction)
        self.predictionTableView.setObjectName(u"predictionTableView")
        self.predictionTableView.verticalHeader().setVisible(False)

        self.gridLayout_4.addWidget(self.predictionTableView, 0, 0, 1, 1)

        self.tabWidget.addTab(self.prediction, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_5 = QGridLayout(self.tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.plotContainer = QGridLayout()
        self.plotContainer.setObjectName(u"plotContainer")

        self.gridLayout_5.addLayout(self.plotContainer, 0, 0, 1, 1)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)

        self.gridLayout_5.setRowStretch(0, 1)
        self.tabWidget.addTab(self.tab, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 6, 1, 1)


        self.retranslateUi(PolynomWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PolynomWindow)
    # setupUi

    def retranslateUi(self, PolynomWindow):
        PolynomWindow.setWindowTitle(QCoreApplication.translate("PolynomWindow", u"\u041f\u043e\u043b\u0438\u043d\u043e\u043c", None))
        self.residualVarianceValueLabel.setText(QCoreApplication.translate("PolynomWindow", u"undefined", None))
        self.scaledResidualVarianceValueLabel.setText(QCoreApplication.translate("PolynomWindow", u"undefined", None))
        self.fStatisticLabel.setText(QCoreApplication.translate("PolynomWindow", u"F1 - \u043e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u0435 \u0424\u0438\u0448\u0435\u0440\u0430", None))
        self.residualVarianceLabel.setText(QCoreApplication.translate("PolynomWindow", u"\u041e\u0441\u0442\u0430\u0442\u043e\u0447\u043d\u0430\u044f \u0434\u0438\u0441\u043f\u0435\u0440\u0441\u0438\u044f:", None))
        self.scaledResidualVarianceLabel.setText(QCoreApplication.translate("PolynomWindow", u"\u041e\u0441\u0442\u0430\u0442\u043e\u0447\u043d\u0430\u044f \u0434\u0438\u0441\u043f\u0435\u0440\u0441\u0438\u044f (\u043c\u0430\u0441\u0448\u0442\u0430\u0431\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u0430\u044f):", None))
        self.rSquaredLabel.setText(QCoreApplication.translate("PolynomWindow", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u043c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0439 \u0434\u0435\u0442\u0435\u0440\u043c\u0438\u043d\u0430\u0446\u0438\u0438", None))
        self.fStatisticValueLabel.setText(QCoreApplication.translate("PolynomWindow", u"undefined", None))
        self.rSquaredValueLabel.setText(QCoreApplication.translate("PolynomWindow", u"undefined", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.model), QCoreApplication.translate("PolynomWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.prediction), QCoreApplication.translate("PolynomWindow", u"\u041f\u0440\u043e\u0433\u043d\u043e\u0437", None))
        self.label.setText(QCoreApplication.translate("PolynomWindow", u"\u0422\u043e\u0447\u043a\u0438 - \u043e\u0442\u043a\u043b\u0438\u043a. \u041b\u0438\u043d\u0438\u044f - \u043f\u0440\u043e\u0433\u043d\u043e\u0437", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("PolynomWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a", None))
    # retranslateUi
