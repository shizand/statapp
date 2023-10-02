import numpy as np
from PySide2.QtCore import Qt

from statapp.models.ro_table_model import ROTableModel


class EditableTableModel(ROTableModel):
    def __init__(self, data=np.array([[]], dtype=np.float32)):
        super().__init__()

        self._data = data

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
            return float(self._data[index.row(), index.column()])

        return None
