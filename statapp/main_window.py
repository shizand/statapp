from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow

from statapp.about_window import AboutWindow
from statapp.ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    about_window = None

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    @Slot()
    def on_aboutmenuaction_triggered(self):
        global about_window
        about_window = AboutWindow()
        about_window.show()