import numpy as np
from PySide2.QtWidgets import QFileDialog
from PySide2 import QtCore

class FileSLCModel(QtCore.QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self.file_name = None

    def saveFile(self, data):
        if self.file_name is None:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            self.file_name, _ = QFileDialog.getSaveFileName(None, "Сохранить файл", "", "Text Files (*.txt);;CSV Files (*.csv)")
        if self.file_name:
            np.savetxt(self.file_name, data, delimiter=",")
            return True
        return False

    def loadFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.file_name, _ = QFileDialog.getOpenFileName(None, "Загрузить файл", "", "Files (*.txt;*.csv)")
        if self.file_name:
            content = np.genfromtxt(self.file_name, delimiter=',')
            return content

    def closeFile(self):
        self.file_name = None
        pass