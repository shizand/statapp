from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow

from statapp.ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    @Slot()
    def on_aboutmenuaction_triggered(self):
        print("Cock")
        return 0

