import numpy as np
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QMainWindow

from statapp.generate_factor_window import GenerateFactorWindow, INDIRECT_LINK
from statapp.models.data_model import DataModel
from statapp.generate_window import GenerateWindow
from statapp.about_window import AboutWindow
from statapp.ui.ui_main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = DataModel()
        self.ui.tableView.setModel(self.model)

    @Slot()
    def on_generateYaction_triggered(self):
        gw = GenerateWindow()
        if gw.exec():
            y = np.random.normal(gw.mat, gw.deviation, size=(gw.count, 1))

            # self.model._data = y
            self.model.updateAllData(y)

    @Slot()
    def on_generateXaction_triggered(self):
        gfw = GenerateFactorWindow()
        if gfw.exec():
            y = self.model.getY()
            yMat = np.mean(y)

            x_arr = np.array([])

            # y - 5 x1 - прямая 4 -> 6
            # 7
            #
            #

            dd = np.array([])

            for cur_y in y:
                k = np.abs(cur_y / yMat)
                if gfw.typeConnection == INDIRECT_LINK:
                    k = 1 / k

                # def f(x):
                #    x = np.abs(x)
                #    return 2.01375 - (1 / np.exp(x - 0.7))

                # k = f(k)
                x = np.random.normal(gfw.mat * (k ** 3), gfw.deviation * k, size=1)
                x_arr = np.append(x_arr, x)
                # if (x > gfw.mat and cur_y > yMat) or (x < gfw.mat and cur_y < yMat):
                #     dd = np.append(dd, 1)
                # else:
                #     dd = np.append(dd, 0)

            data = self.model.getData()

            # self.model._data = y
            x_arr = x_arr.reshape(len(x_arr), 1)
            # dd = dd.reshape(len(dd), 1)
            data = np.concatenate((data, x_arr), axis=1)
            # data = np.concatenate((data, dd), axis=1)
            self.model.updateAllData(data)

    @Slot()
    def on_aboutmenuaction_triggered(self):
        global about_window
        about_window = AboutWindow()
        about_window.show()
