import numpy as np
from PySide2.QtCore import Qt, QModelIndex

from statapp.models.editable_table_model import EditableTableModel
from statapp.models.utils import yx_header


class InputValuesModel(EditableTableModel):
    def __init__(self, data=np.array([[]], dtype=np.float32)):
        super().__init__(data)

    def getHorizontalHeader(self):
        return yx_header(self.columnCount(QModelIndex()))

    def getY(self):
        return self._data[:, 0]
