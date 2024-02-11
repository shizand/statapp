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

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_GenerateFactorWindow(object):
    def setupUi(self, GenerateFactorWindow):
        GenerateFactorWindow.setObjectName("GenerateFactorWindow")
        GenerateFactorWindow.resize(503, 193)
        self.gridLayout_2 = QtWidgets.QGridLayout(GenerateFactorWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(GenerateFactorWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(GenerateFactorWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.generatePushButton = QtWidgets.QPushButton(GenerateFactorWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.generatePushButton.setFont(font)
        self.generatePushButton.setObjectName("generatePushButton")
        self.gridLayout.addWidget(self.generatePushButton, 3, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(GenerateFactorWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.matSpinBox = QtWidgets.QDoubleSpinBox(GenerateFactorWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.matSpinBox.setFont(font)
        self.matSpinBox.setDecimals(5)
        self.matSpinBox.setMaximum(1000000.0)
        self.matSpinBox.setObjectName("matSpinBox")
        self.gridLayout.addWidget(self.matSpinBox, 1, 1, 1, 1)
        self.deviationSpinBox = QtWidgets.QDoubleSpinBox(GenerateFactorWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deviationSpinBox.setFont(font)
        self.deviationSpinBox.setDecimals(5)
        self.deviationSpinBox.setMaximum(1000000.0)
        self.deviationSpinBox.setObjectName("deviationSpinBox")
        self.gridLayout.addWidget(self.deviationSpinBox, 2, 1, 1, 1)
        self.typeComboBox = QtWidgets.QComboBox(GenerateFactorWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.typeComboBox.setFont(font)
        self.typeComboBox.setObjectName("typeComboBox")
        self.gridLayout.addWidget(self.typeComboBox, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(GenerateFactorWindow)
        QtCore.QMetaObject.connectSlotsByName(GenerateFactorWindow)

    def retranslateUi(self, GenerateFactorWindow):
        GenerateFactorWindow.setWindowTitle(QtWidgets.QApplication.translate("GenerateFactorWindow", "Генерация факторов", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("GenerateFactorWindow", "Тип связи", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("GenerateFactorWindow", "Среднеквадратичное отклонение", None, -1))
        self.generatePushButton.setText(QtWidgets.QApplication.translate("GenerateFactorWindow", "Сгенерировать", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("GenerateFactorWindow", "Математическое ожидание", None, -1))
