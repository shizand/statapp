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
import PySide2
import numpy as np
from PySide2 import QtCore
from PySide2.QtCore import Qt

from statapp.utils import safe_list_get


class ROTableModel(QtCore.QAbstractTableModel):
    def __init__(self,
                 data=np.array([[]], dtype=np.float32),
                 ):
        super().__init__()
        self._data = data
        self._headers = {
            Qt.Vertical:  self.getVerticalHeader,
            Qt.Horizontal:  self.getHorizontalHeader,
        }

    def updateAllData(self, data):
        self.layoutAboutToBeChanged.emit()
        self._data = data
        self.layoutChanged.emit()

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def getVerticalHeader(self):
        return []

    def getHorizontalHeader(self):
        return []

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        if role == Qt.DisplayRole:
            return safe_list_get(self._headers[orientation](), section, None)

        return None

    def getData(self):
        return self._data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return float(self._data[index.row(), index.column()])
        return None
