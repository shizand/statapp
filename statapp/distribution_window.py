import numpy as np
from PySide2.QtWidgets import QDialog, QVBoxLayout, QComboBox

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
        self.comboBox.currentIndexChanged.connect(self.onChange)
        self.sc = self.getSc(data[:, 0])
        self.layout.addWidget(self.comboBox)

        self.l = QVBoxLayout()
        self.l.addWidget(self.sc)
        self.layout.addLayout(self.l)


    def onChange(self):
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
        points = np.array(
            [points[0]] +
            [pt for pt, next_pt in zip(points[:-1], points[1:]) if pt != next_pt]
        )
        differences = np.diff(points)
        inverseDifferences = 1 / differences
        for i, (start, end) in enumerate(zip(points[:-1], points[1:])):
            sc.axes.hlines(inverseDifferences[i], start, end, colors='r', linestyles='solid')
        return sc


def normalDensity(x, mu, sigmaSquared):
    return 1 / np.sqrt(2 * np.pi * sigmaSquared) * np.exp(-(x - mu) ** 2 / (2 * sigmaSquared))


class NormalDistributionWindow(DistributionWindow):
    def __init__(self, data: np.array):
        super().__init__("Нормальное распределение", data)

    def getSc(self, points):
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        points = np.sort(points)
        mu = np.mean(points)
        sigmaSquared = np.var(points)
        yValues = normalDensity(points, mu, sigmaSquared)
        sc.axes.plot(points, yValues)
        return sc


class ExponentialDistributionWindow(DistributionWindow):
    def __init__(self, data: np.array):
        super().__init__("Экспоненциальное распределение", data)

    def getSc(self, points):
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        points = np.sort(points)
        mu = np.mean(points)
        lambdaParam = 1 / mu
        yValues = lambdaParam * np.exp(-lambdaParam * points)
        sc.axes.plot(points, yValues)
        return sc
