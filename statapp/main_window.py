from PySide6.QtWidgets import QMainWindow

from statapp.models.data_model import DataModel
from statapp.ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = DataModel()
        self.ui.tableView.setModel(self.model)
