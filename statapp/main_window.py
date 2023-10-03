import numpy as np
from PySide2.QtCore import Slot, QSize
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow, QMessageBox

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

        self.isDataChanged = False
        self.model = InputValuesModel()
        self.fileModel = FileSLCModel()
        self.ui.tableView.setModel(self.model)

    @Slot()
    def on_openfileaction_triggered(self):
        current_data = self.model.getData()
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
                if data is not None:
                    self.model.updateAllData(data)
                    self.isDataChanged = False
        else:
            data = self.fileModel.loadFile()
            if data is not None:
                self.model.updateAllData(data)
                self.isDataChanged = False

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
