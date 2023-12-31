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

from statapp.ui.ui_generate_window import Ui_GenerateWindow
from statapp.utils import addIcon


class GenerateWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.deviation = None
        self.mat = None
        self.count = None
        self.ui = Ui_GenerateWindow()
        self.ui.setupUi(self)

        addIcon(self)


    @Slot()
    def on_generatePushButton_clicked(self):

        self.count = self.ui.countSpinBox.value()
        self.mat = self.ui.matSpinBox.value()
        self.deviation = self.ui.deviationSpinBox.value()

        self.accept()
