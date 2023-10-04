#
# Copyright (c) 2023 Maxim Slipenko, Eugene Lazurenko.
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
import numpy as np
from PySide2.QtWidgets import QFileDialog, QMessageBox


class FileSLCModel:
    def __init__(self):
        super().__init__()
        self.fileName = None

    def saveFile(self, data):
        if not self.fileName:
            self.fileName, _ = QFileDialog.getSaveFileName(
                None, "Сохранить файл", "", "Text Files (*.txt);;CSV Files (*.csv)"
            )
        if self.fileName:
            np.savetxt(self.fileName, data, delimiter=",")
            return True
        return False

    def loadFile(self):
        self.fileName, _ = QFileDialog.getOpenFileName(
            None, "Загрузить файл", "", "Files (*.txt *.csv)"
        )
        if self.fileName:
            try:
                content = np.genfromtxt(self.fileName, delimiter=',', invalid_raise=True, ndmin=2)
            except ValueError:
                QMessageBox.warning \
                    (None,
                    'Ошибка',
                    "Ошибка чтения файла!\nФайл нельзя открыть или файл неверного формата")
                self.fileName = None
                return None
            return content

        return None

    def closeFile(self):
        self.fileName = None
