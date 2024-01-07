#
# Copyright (c) 2024 Maxim Slipenko, Eugene Lazurenko.
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
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QDialog

from statapp.ui.ui_generate_factor_window import Ui_GenerateFactorWindow
from statapp.models.combobox_model import ComboBoxModel
from statapp.utils import addIcon

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

        addIcon(self)

    @Slot()
    def on_generatePushButton_clicked(self):
        self.typeConnection = self._typeComboBox.rawData(self.ui.typeComboBox.currentIndex())[0]

        self.mat = self.ui.matSpinBox.value()
        self.deviation = self.ui.deviationSpinBox.value()

        self.accept()
