import numpy as np
from PySide6 import QtCore
from PySide6.QtCore import Qt


class DataModel(QtCore.QAbstractTableModel):
    def __init__(self, data=np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)):
        super().__init__()

        self._data = data

    def updateAllData(self, data):
        self.layoutAboutToBeChanged.emit()
        self._data = data
        self.layoutChanged.emit()

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        if role == Qt.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:

                if section == 0:
                    return 'Y'

                return f'X{section}'

        return None

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            try:
                value = float(value)
            except ValueError:
                return False
            self._data[index.row(), index.column()] = value
            return True
        return False

    def data(self, index, role):
        if role == Qt.DisplayRole or role == Qt.EditRole:
            # ?
            return float(self._data[index.row(), index.column()])

        return None
