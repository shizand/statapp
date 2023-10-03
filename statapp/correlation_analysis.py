from PySide2.QtWidgets import QDialog, QHeaderView

from statapp.calculations import correlation_analysis
from statapp.models.correlation_analysis_model import CorrelationAnalysisModel
from statapp.ui.ui_correlation_analysis_window import Ui_CorrelationAnalysisWindow


class СorrelationAnalysisWindow(QDialog):
    def __init__(self, data):
        super().__init__()
        self.ui = Ui_CorrelationAnalysisWindow()
        self.ui.setupUi(self)

        res = correlation_analysis(data)
        self.model = CorrelationAnalysisModel(res.round(2))
        self.ui.tableView.setModel(self.model)
        header = self.ui.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
