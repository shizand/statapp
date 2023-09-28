import numpy as np
from PySide2.QtWidgets import QFileDialog, QMessageBox


class FileSLCModel:
    def __init__(self):
        super().__init__()
        self.file_name = None

    def saveFile(self, data):
        if self.file_name is None:
            self.file_name, _ = QFileDialog.getSaveFileName(None, "Сохранить файл", "", "Text Files (*.txt);;CSV Files (*.csv)")
        if self.file_name:
            np.savetxt(self.file_name, data, delimiter=",")
            return True
        return False

    def loadFile(self):
        self.file_name, _ = QFileDialog.getOpenFileName(None, "Загрузить файл", "", "Files (*.txt;*.csv)")
        if self.file_name:
            try:
                content = np.genfromtxt(self.file_name, delimiter=',', invalid_raise=True)
            except ValueError as e:
                QMessageBox.warning \
                    (None,
                    'Ошибка',
                    "Ошибка чтения файла!\nФайл нельзя открыть или файл неверного формата")
                return None
            return content

    def closeFile(self):
        self.file_name = None
        pass