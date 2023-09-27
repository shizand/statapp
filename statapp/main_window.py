import numpy as np
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QMainWindow

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
    def on_aboutmenuaction_triggered(self):
        global about_window
        about_window = AboutWindow()
        about_window.show()
