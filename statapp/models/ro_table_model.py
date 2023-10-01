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

    def getY(self):
        return self._data[:, 0]


    def data(self, index, role):
        if role == Qt.DisplayRole:
            return float(self._data[index.row(), index.column()])
        return None
