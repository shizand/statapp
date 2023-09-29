# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.aboutmenuaction = QAction(MainWindow)
        self.aboutmenuaction.setObjectName(u"aboutmenuaction")
        self.generateYaction = QAction(MainWindow)
        self.generateYaction.setObjectName(u"generateYaction")
        self.generateXaction = QAction(MainWindow)
        self.generateXaction.setObjectName(u"generateXaction")
        self.openfileaction = QAction(MainWindow)
        self.openfileaction.setObjectName(u"openfileaction")
        self.savefileaction = QAction(MainWindow)
        self.savefileaction.setObjectName(u"savefileaction")
        self.closefileaction = QAction(MainWindow)
        self.closefileaction.setObjectName(u"closefileaction")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.verticalHeader().setVisible(False)

        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.filemenu = QMenu(self.menubar)
        self.filemenu.setObjectName(u"filemenu")
        self.generatemenu = QMenu(self.menubar)
        self.generatemenu.setObjectName(u"generatemenu")
        self.analyzemenu = QMenu(self.menubar)
        self.analyzemenu.setObjectName(u"analyzemenu")
        self.modelmenu = QMenu(self.menubar)
        self.modelmenu.setObjectName(u"modelmenu")
        self.helpmenu = QMenu(self.menubar)
        self.helpmenu.setObjectName(u"helpmenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.filemenu.menuAction())
        self.menubar.addAction(self.generatemenu.menuAction())
        self.menubar.addAction(self.analyzemenu.menuAction())
        self.menubar.addAction(self.modelmenu.menuAction())
        self.menubar.addAction(self.helpmenu.menuAction())
        self.filemenu.addAction(self.openfileaction)
        self.filemenu.addAction(self.savefileaction)
        self.filemenu.addAction(self.closefileaction)
        self.generatemenu.addAction(self.generateYaction)
        self.generatemenu.addAction(self.generateXaction)
        self.helpmenu.addAction(self.aboutmenuaction)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043c\u043e\u0434\u0435\u043b\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.aboutmenuaction.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.generateYaction.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f \u043e\u0442\u043a\u043b\u0438\u043a\u0430", None))
        self.generateXaction.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f \u0444\u0430\u043a\u0442\u043e\u0440\u0430", None))
        self.openfileaction.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.savefileaction.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.closefileaction.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0422\u0410\u0422\u0418\u0421\u0422\u0418\u0427\u0415\u0421\u041a\u0418\u0415 \u0414\u0410\u041d\u041d\u042b\u0415", None))
        self.filemenu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.generatemenu.setTitle(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u0435\u0439", None))
        self.analyzemenu.setTitle(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0437 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.modelmenu.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0435\u043b\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.helpmenu.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi
