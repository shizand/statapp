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
from PySide2.QtCore import Slot, QSize
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow, QMessageBox, QAction

from statapp.calculations import generate_x_values
from statapp.generate_factor_window import GenerateFactorWindow
from statapp.models.input_values_model import InputValuesModel
from statapp.generate_window import GenerateWindow
from statapp.about_window import AboutWindow
from statapp.models.fileslc_model import FileSLCModel
from statapp.ui.ui_main_window import Ui_MainWindow
from statapp.utils import resource_path, buildMessageBox
from statapp.variance_analysis import VarianceAnalysisWindow
from statapp.correlation_analysis import СorrelationAnalysisWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        icon = QIcon()
        icon.addFile(resource_path("ui/images/logo.ico"), QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        self.ui.generateXaction.setEnabled(False)
        self.ui.varianceAnalysisAction.setEnabled(False)
        self.ui.correlationAnalisisAction.setEnabled(False)

        self.isDataChanged = False
        self.model = InputValuesModel()
        self.fileModel = FileSLCModel()
        self.ui.tableView.setModel(self.model)

    @Slot()
    def on_openfileaction_triggered(self):
        current_data = self.model.getData()
        data = np.array([])
        if current_data.size > 1:
            file = ''
            if self.fileModel.file_name:
                file = '\nФайл сохранения: ' + self.fileModel.file_name

            msgBox = buildMessageBox \
                ('Сохранение данных',
                 "Сохранить данные?" + file,
                 QMessageBox.Question,
                 QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                 QMessageBox.Cancel)

            reply = msgBox.exec_()
            if reply == QMessageBox.StandardButton.Yes:
                self.fileModel.saveFile(self.model.getData())
            elif reply == QMessageBox.StandardButton.Cancel:
                return
            else:
                data = self.fileModel.loadFile()
                if data is not None and data.shape[0] > 0:
                    self.model.updateAllData(data)
                    self.isDataChanged = False
        else:
            data = self.fileModel.loadFile()
            if data is not None and data.shape[0] > 0:
                self.model.updateAllData(data)
                self.isDataChanged = False

        if data.shape[1] == 1:
            self.ui.generateXaction.setEnabled(True)
            self.ui.varianceAnalysisAction.setEnabled(False)
            self.ui.correlationAnalisisAction.setEnabled(False)
        elif data.shape[1] > 1:
            self.ui.generateXaction.setEnabled(True)
            self.ui.varianceAnalysisAction.setEnabled(True)
            self.ui.correlationAnalisisAction.setEnabled(True)
        else:
            self.ui.generateXaction.setEnabled(False)
            self.ui.varianceAnalysisAction.setEnabled(False)
            self.ui.correlationAnalisisAction.setEnabled(False)

    @Slot()
    def on_savefileaction_triggered(self):
        self.isDataChanged = not self.fileModel.saveFile(self.model.getData())

    @Slot()
    def on_closefileaction_triggered(self):
        self.fileModel.closeFile()
        self.isDataChanged = False

    @Slot()
    def on_generateYaction_triggered(self):
        gw = GenerateWindow()

        if gw.exec():
            y = np.random.normal(gw.mat, gw.deviation, size=(gw.count, 1))
            self.model.updateAllData(y.round(2))
            self.isDataChanged = True
            self.ui.generateXaction.setEnabled(True)

    @Slot()
    def on_generateXaction_triggered(self):
        gfw = GenerateFactorWindow()

        if gfw.exec():
            data = self.model.getData()
            y = self.model.getY()
            x_arr = generate_x_values(gfw.mat, gfw.deviation, gfw.typeConnection, y)
            x_arr = x_arr.reshape(len(x_arr), 1).round(2)
            # dd = dd.reshape(len(dd), 1)
            data = np.concatenate((data, x_arr), axis=1)
            self.model.updateAllData(data)
            self.ui.varianceAnalysisAction.setEnabled(True)
            self.ui.correlationAnalisisAction.setEnabled(True)
            self.isDataChanged = True

    @Slot()
    def on_aboutmenuaction_triggered(self):
        global about_window
        about_window = AboutWindow()
        about_window.show()

    @Slot()
    def on_varianceAnalysisAction_triggered(self):
        dw = VarianceAnalysisWindow(self.model.getData())
        dw.exec()

    @Slot()
    def on_correlationAnalisisAction_triggered(self):
        dw = СorrelationAnalysisWindow(self.model.getData())
        dw.exec()

    def closeEvent(self, event):
        if self.isDataChanged:
            file = ''
            if self.fileModel.file_name:
                file = '\nФайл сохранения: ' + self.fileModel.file_name

            msgBox = buildMessageBox \
                ('Завершение работы',
                 "Сохранить данные?" + file,
                 QMessageBox.Question,
                 QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                 QMessageBox.Cancel)

            reply = msgBox.exec_()
            if reply == QMessageBox.StandardButton.Yes:
                self.fileModel.saveFile(self.model.getData())
                event.accept()
            elif reply == QMessageBox.StandardButton.No:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()
