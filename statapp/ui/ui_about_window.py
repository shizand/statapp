# -*- coding: utf-8 -*-
#
# Copyright (c) 2023 Maxim Slipenko, Eugene Lazurenko.
#
# This file is part of Statapp
# (see https://github.com/shizand/statapp).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.#


################################################################################
## Form generated from reading UI file 'about_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        if not AboutWindow.objectName():
            AboutWindow.setObjectName(u"AboutWindow")
        AboutWindow.setEnabled(True)
        AboutWindow.resize(483, 543)
        AboutWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(AboutWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelgif = QLabel(self.centralwidget)
        self.labelgif.setObjectName(u"labelgif")
        self.labelgif.setMinimumSize(QSize(50, 50))
        self.labelgif.setMaximumSize(QSize(500, 600))
        font = QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.labelgif.setFont(font)
        self.labelgif.setFrameShape(QFrame.NoFrame)
        self.labelgif.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelgif, 5, 1, 1, 1)

        self.labelowner = QLabel(self.centralwidget)
        self.labelowner.setObjectName(u"labelowner")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(50)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.labelowner.setFont(font1)
        self.labelowner.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelowner, 6, 1, 1, 1)

        self.labeldevelopers = QLabel(self.centralwidget)
        self.labeldevelopers.setObjectName(u"labeldevelopers")
        self.labeldevelopers.setFont(font)
        self.labeldevelopers.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labeldevelopers, 2, 1, 1, 1)

        self.versionLabel = QLabel(self.centralwidget)
        self.versionLabel.setObjectName(u"versionLabel")
        font2 = QFont()
        font2.setPointSize(12)
        self.versionLabel.setFont(font2)
        self.versionLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.versionLabel, 1, 1, 1, 1)

        self.labelbasegigamen = QLabel(self.centralwidget)
        self.labelbasegigamen.setObjectName(u"labelbasegigamen")
        self.labelbasegigamen.setFont(font)
        self.labelbasegigamen.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelbasegigamen, 3, 1, 1, 1)

        self.mainLabel = QLabel(self.centralwidget)
        self.mainLabel.setObjectName(u"mainLabel")
        font3 = QFont()
        font3.setPointSize(20)
        self.mainLabel.setFont(font3)
        self.mainLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.mainLabel, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        AboutWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AboutWindow)

        QMetaObject.connectSlotsByName(AboutWindow)
    # setupUi

    def retranslateUi(self, AboutWindow):
        AboutWindow.setWindowTitle(QCoreApplication.translate("AboutWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u0435", None))
        self.labelgif.setText("")
        self.labelowner.setText(QCoreApplication.translate("AboutWindow", u"\u0414\u043e\u043d\u0435\u0446\u043a\u0438\u0439 \u041d\u0430\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0439 \u0422\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0423\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442", None))
        self.labeldevelopers.setText(QCoreApplication.translate("AboutWindow", u"\u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u0438: \u0421\u043b\u0438\u043f\u0435\u043d\u043a\u043e \u041c., \u041b\u0430\u0437\u0443\u0440\u0435\u043d\u043a\u043e \u0415.", None))
        self.versionLabel.setText(QCoreApplication.translate("AboutWindow", u"\u0412\u0435\u0440\u0441\u0438\u044f:", None))
        self.labelbasegigamen.setText(QCoreApplication.translate("AboutWindow", u"\u0422\u0435\u043e\u0440\u0435\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0444\u0443\u043d\u0434\u0430\u043c\u0435\u043d\u0442: \u0414\u043c\u0438\u0442\u0440\u044e\u043a \u0422. \u0413.", None))
        self.mainLabel.setText(QCoreApplication.translate("AboutWindow", u"Statapp", None))
    # retranslateUi
