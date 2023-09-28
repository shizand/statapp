import numpy as np
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QMainWindow, QMessageBox, QApplication

from statapp.generate_factor_window import GenerateFactorWindow, INDIRECT_LINK
from statapp.models.data_model import DataModel
from statapp.generate_window import GenerateWindow
from statapp.about_window import AboutWindow
from statapp.models.fileslc_model import FileSLCModel
from statapp.ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.isDataChanged = False
        self.model = DataModel()
        self.fileModel = FileSLCModel()
        self.ui.tableView.setModel(self.model)

    @Slot()
    def on_openfileaction_triggered(self):
        data = self.fileModel.loadFile()
        self.model.updateAllData(data)
        self.isDataChanged = True

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
            self.model.updateAllData(y)
            self.isDataChanged = True

    @Slot()
    def on_generateXaction_triggered(self):
        gfw = GenerateFactorWindow()

        # dd = np.array([])

        if gfw.exec():
            y = self.model.getY()
            yMat = np.mean(y)

            x_arr = np.array([])

            for cur_y in y:
                k = np.abs(cur_y / yMat)
                if k > 1:
                    k = 2 - 1 / k
                if gfw.typeConnection == INDIRECT_LINK:
                    k = 1 / k

                x = np.random.normal(gfw.mat * (k ** 3), gfw.deviation * k, size=1)
                x_arr = np.append(x_arr, x)
                # if (x > gfw.mat and cur_y > yMat) or (x < gfw.mat and cur_y < yMat):
                #     dd = np.append(dd, 1)
                # else:
                #     dd = np.append(dd, 0)

            data = self.model.getData()

            x_arr = x_arr.reshape(len(x_arr), 1)
            # dd = dd.reshape(len(dd), 1)
            data = np.concatenate((data, x_arr), axis=1)
            # data = np.concatenate((data, dd), axis=1)
            self.model.updateAllData(data)
            self.isDataChanged = True

    @Slot()
    def on_aboutmenuaction_triggered(self):
        global about_window
        about_window = AboutWindow()
        about_window.show()

    def closeEvent(self, event):
        if self.isDataChanged:
            msgBox = QMessageBox()

            msgBox.setIcon(QMessageBox.Question)

            msgBox.setWindowTitle('Завершение работы')

            file = ''
            if self.fileModel.file_name:
                file = '\nФайл сохранения:' + self.fileModel.file_name

            msgBox.setText("Сохранить данные?" + file)

            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            msgBox.setDefaultButton(QMessageBox.Cancel)

            yesButton = msgBox.button(QMessageBox.Yes)
            yesButton.setText("Да")

            noButton = msgBox.button(QMessageBox.No)
            noButton.setText("Нет")

            cancelButton = msgBox.button(QMessageBox.Cancel)
            cancelButton.setText("Отмена")

            QApplication.beep()
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
