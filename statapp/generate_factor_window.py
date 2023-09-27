from PySide2.QtCore import Slot
from PySide2.QtWidgets import QDialog

from statapp.ui.ui_generate_factor_window import Ui_GenerateFactorWindow
from statapp.models.combobox_model import ComboBoxModel


DIRECT_LINK = 0
INDIRECT_LINK = 1


class GenerateFactorWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.deviation = None
        self.mat = None
        self.typeConnection = None
        self._typeComboBox = ComboBoxModel([
            [DIRECT_LINK, "прямая"],
            [INDIRECT_LINK, "обратная"]
        ])

        self.ui = Ui_GenerateFactorWindow()
        self.ui.setupUi(self)
        self.ui.typeComboBox.setModel(self._typeComboBox)

    @Slot()
    def on_generatePushButton_clicked(self):
        self.typeConnection = self._typeComboBox.rawData(self.ui.typeComboBox.currentIndex())[0]

        self.mat = self.ui.matSpinBox.value()
        self.deviation = self.ui.deviationSpinBox.value()

        self.accept()
