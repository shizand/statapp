#
# Copyright (c) 2023 Maxim Slipenko, Euegene Lazurenko.
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
# along with this program. If not, see <http://www.gnu.org/licenses/>.#
import numpy as np
from PySide2.QtWidgets import QFileDialog, QMessageBox


class FileSLCModel:
    def __init__(self):
        super().__init__()
        self.file_name = None

    def saveFile(self, data):
        if not self.file_name:
            self.file_name, _ = QFileDialog.getSaveFileName(None, "Сохранить файл", "", "Text Files (*.txt);;CSV Files (*.csv)")
        if self.file_name:
            np.savetxt(self.file_name, data, delimiter=",")
            return True
        return False

    def loadFile(self):
        self.file_name, _ = QFileDialog.getOpenFileName(None, "Загрузить файл", "", "Files (*.txt *.csv)")
        if self.file_name:
            try:
                content = np.genfromtxt(self.file_name, delimiter=',', invalid_raise=True)
            except ValueError as e:
                QMessageBox.warning \
                    (None,
                    'Ошибка',
                    "Ошибка чтения файла!\nФайл нельзя открыть или файл неверного формата")
                return None
            return content

    def closeFile(self):
        self.file_name = None
        pass
