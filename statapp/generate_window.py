from PySide2.QtCore import Slot
from PySide2.QtWidgets import QDialog

from statapp.ui.ui_generate_window import Ui_GenerateWindow


class GenerateWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.deviation = None
        self.mat = None
        self.count = None
        self.ui = Ui_GenerateWindow()
        self.ui.setupUi(self)

    @Slot()
    def on_generatePushButton_clicked(self):

        self.count = self.ui.countSpinBox.value()
        self.mat = self.ui.matSpinBox.value()
        self.deviation = self.ui.deviationSpinBox.value()

        self.accept()
