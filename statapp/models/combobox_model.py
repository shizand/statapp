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
