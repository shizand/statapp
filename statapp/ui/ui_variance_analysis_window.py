# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'variance_analysis_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_VarianceAnalysisWindow(object):
    def setupUi(self, VarianceAnalysisWindow):
        if not VarianceAnalysisWindow.objectName():
            VarianceAnalysisWindow.setObjectName(u"VarianceAnalysisWindow")
        VarianceAnalysisWindow.resize(630, 400)
        self.gridLayout_2 = QGridLayout(VarianceAnalysisWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableView = QTableView(VarianceAnalysisWindow)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(VarianceAnalysisWindow)

        QMetaObject.connectSlotsByName(VarianceAnalysisWindow)
    # setupUi

    def retranslateUi(self, VarianceAnalysisWindow):
        VarianceAnalysisWindow.setWindowTitle(QCoreApplication.translate("VarianceAnalysisWindow", u"\u0414\u0438\u0441\u043f\u0435\u0440\u0441\u0438\u043e\u043d\u043d\u044b\u0439 \u0430\u043d\u0430\u043b\u0438\u0437", None))
    # retranslateUi

