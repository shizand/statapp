from PySide2.QtWidgets import QDialog, QHeaderView

from statapp.calculations import variance_analysis
from statapp.models.variance_analysis_model import VarianceAnalysisModel
from statapp.ui.ui_variance_analysis_window import Ui_VarianceAnalysisWindow


class VarianceAnalysisWindow(QDialog):
    def __init__(self, data):
        super().__init__()
        self.ui = Ui_VarianceAnalysisWindow()
        self.ui.setupUi(self)

        res = variance_analysis(data)
        self.model = VarianceAnalysisModel(res.round(2))
        self.ui.tableView.setModel(self.model)
        header = self.ui.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
