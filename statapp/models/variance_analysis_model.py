from PySide2.QtCore import QModelIndex

from statapp.models.ro_table_model import ROTableModel
from statapp.models.utils import yx_header


class VarianceAnalysisModel(ROTableModel):
    def __init__(self, data):
        super().__init__(data)

    def getHorizontalHeader(self):
        return ['Мат. ожидание', 'Среднекв. отклонение', 'Минимум', 'Максимум']

    def getVerticalHeader(self):
        return yx_header(self.rowCount(QModelIndex()))
