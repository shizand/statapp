from PySide2.QtCore import QModelIndex, Qt

from statapp.models.ro_table_model import ROTableModel
from statapp.models.utils import yx_header


class CorrelationAnalysisModel(ROTableModel):
    def __init__(self, data):
        super().__init__(data)

    def getHorizontalHeader(self):
        return yx_header(self.columnCount(QModelIndex()))

    def getVerticalHeader(self):
        return yx_header(self.rowCount(QModelIndex()))

    def data(self, index, role):
        if role == Qt.DisplayRole:
            if (index.column() <= index.row()):
                return float(self._data[index.row(), index.column()])
            else:
                None
        return None
