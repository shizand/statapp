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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.tableView.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 29))
        self.menubar.setObjectName("menubar")
        self.filemenu = QtWidgets.QMenu(self.menubar)
        self.filemenu.setObjectName("filemenu")
        self.generatemenu = QtWidgets.QMenu(self.menubar)
        self.generatemenu.setObjectName("generatemenu")
        self.analyzemenu = QtWidgets.QMenu(self.menubar)
        self.analyzemenu.setObjectName("analyzemenu")
        self.modelmenu = QtWidgets.QMenu(self.menubar)
        self.modelmenu.setObjectName("modelmenu")
        self.helpmenu = QtWidgets.QMenu(self.menubar)
        self.helpmenu.setObjectName("helpmenu")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.aboutmenuaction = QtWidgets.QAction(MainWindow)
        self.aboutmenuaction.setObjectName("aboutmenuaction")
        self.generateYaction = QtWidgets.QAction(MainWindow)
        self.generateYaction.setObjectName("generateYaction")
        self.generateXaction = QtWidgets.QAction(MainWindow)
        self.generateXaction.setObjectName("generateXaction")
        self.openfileaction = QtWidgets.QAction(MainWindow)
        self.openfileaction.setObjectName("openfileaction")
        self.savefileaction = QtWidgets.QAction(MainWindow)
        self.savefileaction.setObjectName("savefileaction")
        self.closefileaction = QtWidgets.QAction(MainWindow)
        self.closefileaction.setObjectName("closefileaction")
        self.varianceAnalysisAction = QtWidgets.QAction(MainWindow)
        self.varianceAnalysisAction.setObjectName("varianceAnalysisAction")
        self.correlationAnalisisAction = QtWidgets.QAction(MainWindow)
        self.correlationAnalisisAction.setObjectName("correlationAnalisisAction")
        self.linearPolynomAction = QtWidgets.QAction(MainWindow)
        self.linearPolynomAction.setObjectName("linearPolynomAction")
        self.squaredPolynomAction = QtWidgets.QAction(MainWindow)
        self.squaredPolynomAction.setObjectName("squaredPolynomAction")
        self.transformPolynomAction = QtWidgets.QAction(MainWindow)
        self.transformPolynomAction.setObjectName("transformPolynomAction")
        self.usageaction = QtWidgets.QAction(MainWindow)
        self.usageaction.setObjectName("usageaction")
        self.uniformDistributionAction = QtWidgets.QAction(MainWindow)
        self.uniformDistributionAction.setObjectName("uniformDistributionAction")
        self.normalDistributionAction = QtWidgets.QAction(MainWindow)
        self.normalDistributionAction.setObjectName("normalDistributionAction")
        self.exponentialDistributionAction = QtWidgets.QAction(MainWindow)
        self.exponentialDistributionAction.setObjectName("exponentialDistributionAction")
        self.filemenu.addAction(self.openfileaction)
        self.filemenu.addAction(self.savefileaction)
        self.filemenu.addAction(self.closefileaction)
        self.generatemenu.addAction(self.generateYaction)
        self.generatemenu.addAction(self.generateXaction)
        self.analyzemenu.addAction(self.varianceAnalysisAction)
        self.analyzemenu.addAction(self.correlationAnalisisAction)
        self.modelmenu.addAction(self.linearPolynomAction)
        self.modelmenu.addAction(self.squaredPolynomAction)
        self.modelmenu.addAction(self.transformPolynomAction)
        self.helpmenu.addAction(self.usageaction)
        self.helpmenu.addAction(self.aboutmenuaction)
        self.menu.addAction(self.uniformDistributionAction)
        self.menu.addAction(self.normalDistributionAction)
        self.menu.addAction(self.exponentialDistributionAction)
        self.menubar.addAction(self.filemenu.menuAction())
        self.menubar.addAction(self.generatemenu.menuAction())
        self.menubar.addAction(self.analyzemenu.menuAction())
        self.menubar.addAction(self.modelmenu.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.helpmenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Статистическое моделирование", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "СТАТИСТИЧЕСКИЕ ДАННЫЕ", None, -1))
        self.filemenu.setTitle(QtWidgets.QApplication.translate("MainWindow", "Файл", None, -1))
        self.generatemenu.setTitle(QtWidgets.QApplication.translate("MainWindow", "Генерация показателей", None, -1))
        self.analyzemenu.setTitle(QtWidgets.QApplication.translate("MainWindow", "Анализ данных", None, -1))
        self.modelmenu.setTitle(QtWidgets.QApplication.translate("MainWindow", "Моделирование", None, -1))
        self.helpmenu.setTitle(QtWidgets.QApplication.translate("MainWindow", "Справка", None, -1))
        self.menu.setTitle(QtWidgets.QApplication.translate("MainWindow", "Распределения", None, -1))
        self.aboutmenuaction.setText(QtWidgets.QApplication.translate("MainWindow", "О программе", None, -1))
        self.generateYaction.setText(QtWidgets.QApplication.translate("MainWindow", "Генерация отклика", None, -1))
        self.generateXaction.setText(QtWidgets.QApplication.translate("MainWindow", "Генерация фактора", None, -1))
        self.openfileaction.setText(QtWidgets.QApplication.translate("MainWindow", "Открыть", None, -1))
        self.savefileaction.setText(QtWidgets.QApplication.translate("MainWindow", "Сохранить", None, -1))
        self.closefileaction.setText(QtWidgets.QApplication.translate("MainWindow", "Закрыть", None, -1))
        self.varianceAnalysisAction.setText(QtWidgets.QApplication.translate("MainWindow", "Дисперсионный анализ", None, -1))
        self.correlationAnalisisAction.setText(QtWidgets.QApplication.translate("MainWindow", "Корреляционный анализ", None, -1))
        self.linearPolynomAction.setText(QtWidgets.QApplication.translate("MainWindow", "Линейный полином", None, -1))
        self.squaredPolynomAction.setText(QtWidgets.QApplication.translate("MainWindow", "Квадратичный полином", None, -1))
        self.transformPolynomAction.setText(QtWidgets.QApplication.translate("MainWindow", "Преобразования", None, -1))
        self.usageaction.setText(QtWidgets.QApplication.translate("MainWindow", "Использование", None, -1))
        self.uniformDistributionAction.setText(QtWidgets.QApplication.translate("MainWindow", "Равномерное", None, -1))
        self.normalDistributionAction.setText(QtWidgets.QApplication.translate("MainWindow", "Нормальное", None, -1))
        self.exponentialDistributionAction.setText(QtWidgets.QApplication.translate("MainWindow", "Экспоненциальное", None, -1))
