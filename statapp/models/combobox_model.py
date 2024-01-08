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
from PySide2.QtCore import QAbstractListModel, Qt


class ComboBoxModel(QAbstractListModel):

    def __init__(self, data):
        super().__init__()
        self._data = data

    def updateAllData(self, data: list):
        self.layoutAboutToBeChanged.emit()
        self._data = data
        self.layoutChanged.emit()

    def rawData(self, index: int):
        return self._data[index]

    def findById(self, oid: int):
        for i, x in enumerate(self._data):
            if x[0] == oid:
                return i

        return -1

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][1]

        if role == Qt.UserRole:
            return self._data[index.row()]

        return None

    def rowCount(self, index):
        return len(self._data)
