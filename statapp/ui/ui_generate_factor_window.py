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
## Form generated from reading UI file 'generate_factor_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_GenerateFactorWindow(object):
    def setupUi(self, GenerateFactorWindow):
        if not GenerateFactorWindow.objectName():
            GenerateFactorWindow.setObjectName(u"GenerateFactorWindow")
        GenerateFactorWindow.resize(503, 193)
        self.gridLayout_2 = QGridLayout(GenerateFactorWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(GenerateFactorWindow)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(GenerateFactorWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.generatePushButton = QPushButton(GenerateFactorWindow)
        self.generatePushButton.setObjectName(u"generatePushButton")
        self.generatePushButton.setFont(font)

        self.gridLayout.addWidget(self.generatePushButton, 3, 0, 1, 2)

        self.label_2 = QLabel(GenerateFactorWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.matSpinBox = QDoubleSpinBox(GenerateFactorWindow)
        self.matSpinBox.setObjectName(u"matSpinBox")
        self.matSpinBox.setFont(font)
        self.matSpinBox.setMaximum(1000000.000000000000000)

        self.gridLayout.addWidget(self.matSpinBox, 1, 1, 1, 1)

        self.deviationSpinBox = QDoubleSpinBox(GenerateFactorWindow)
        self.deviationSpinBox.setObjectName(u"deviationSpinBox")
        self.deviationSpinBox.setFont(font)
        self.deviationSpinBox.setMaximum(1000000.000000000000000)

        self.gridLayout.addWidget(self.deviationSpinBox, 2, 1, 1, 1)

        self.typeComboBox = QComboBox(GenerateFactorWindow)
        self.typeComboBox.setObjectName(u"typeComboBox")
        self.typeComboBox.setFont(font)
        self.typeComboBox.setEditable(False)

        self.gridLayout.addWidget(self.typeComboBox, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(GenerateFactorWindow)

        QMetaObject.connectSlotsByName(GenerateFactorWindow)
    # setupUi

    def retranslateUi(self, GenerateFactorWindow):
        GenerateFactorWindow.setWindowTitle(QCoreApplication.translate("GenerateFactorWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f \u0444\u0430\u043a\u0442\u043e\u0440\u043e\u0432", None))
        self.label.setText(QCoreApplication.translate("GenerateFactorWindow", u"\u0422\u0438\u043f \u0441\u0432\u044f\u0437\u0438", None))
        self.label_3.setText(QCoreApplication.translate("GenerateFactorWindow", u"\u0421\u0440\u0435\u0434\u043d\u0435\u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u0447\u043d\u043e\u0435 \u043e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0435", None))
        self.generatePushButton.setText(QCoreApplication.translate("GenerateFactorWindow", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("GenerateFactorWindow", u"\u041c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u0435", None))
        self.typeComboBox.setCurrentText("")
        self.typeComboBox.setPlaceholderText("")
    # retranslateUi
