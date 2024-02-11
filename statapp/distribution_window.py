import numpy as np
from PySide2.QtWidgets import QDialog, QVBoxLayout, QScrollArea, QWidget, QComboBox

from statapp.polynoms.polynom_window import MplCanvas
from statapp.utils import addIcon
from statapp.models.utils import yxHeader


class DistributionWindow(QDialog):
    def __init__(self, title: str, data: np.ndarray):
        super().__init__()
        self.setWindowTitle(title)
        addIcon(self)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.data = data
        self.values = yxHeader(data.shape[1])

        self.comboBox = QComboBox()
        self.comboBox.addItems(self.values)
        self.comboBox.currentIndexChanged.connect(self.on_change)
        self.sc = self.getSc(data[:, 0])
        self.layout.addWidget(self.comboBox)

        self.l = QVBoxLayout()
        self.l.addWidget(self.sc)
        self.layout.addLayout(self.l)


    def on_change(self):
        while ((child := self.l.takeAt(0)) != None):
            child.widget().deleteLater()
        self.sc = self.getSc(self.data[:, self.comboBox.currentIndex()])
        self.l.addWidget(self.sc)


class UniformDistributionWindow(DistributionWindow):
    def __init__(self, data: np.array):
        super().__init__("Равномерное распределение", data)

    def getSc(self, points):
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        points = np.sort(points)
        unique_points = np.array([points[0]] + [pt for pt, next_pt in zip(points[:-1], points[1:]) if pt != next_pt])
        differences = np.diff(unique_points)
        inverse_differences = 1 / differences
        for i, (start, end) in enumerate(zip(unique_points[:-1], unique_points[1:])):
            sc.axes.hlines(inverse_differences[i], start, end, colors='r', linestyles='solid')
        return sc


def normal_density(x, mu, sigma_squared):
    return 1 / np.sqrt(2 * np.pi * sigma_squared) * np.exp(-(x - mu)**2 / (2 * sigma_squared))


class NormalDistributionWindow(DistributionWindow):
    def __init__(self, data: np.array):
        super().__init__("Нормальное распределение", data)

    def getSc(self, points):
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        points = np.sort(points)
        mu = np.mean(points)
        sigma_squared = np.var(points)
        y_values = normal_density(points, mu, sigma_squared)

        sc.axes.plot(points, y_values)

        return sc


class ExponentialDistributionWindow(DistributionWindow):
    def __init__(self, data: np.array):
        super().__init__("Экспоненциальное распределение", data)

    def getSc(self, points):
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        points = np.sort(points)
        mu = np.mean(points)
        lambda_param = 1 / mu
        y_values = lambda_param * np.exp(-lambda_param * points)
        sc.axes.plot(points, y_values)
        return sc