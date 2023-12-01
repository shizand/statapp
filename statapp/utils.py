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
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
import os
import sys

from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMessageBox, QDoubleSpinBox, QStyledItemDelegate

from statapp.constants import NUMBERS_PRECISION


def resourcePath(relative):
    if getattr(sys, 'frozen', False):
        # pylint: disable=protected-access
        bundleDir = sys._MEIPASS
    else:
        # we are running in a normal Python environment
        bundleDir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(bundleDir, relative)


def addIcon(windowOrDialog):
    icon = QIcon()
    icon.addFile(resourcePath("ui/images/logo.ico"), QSize(), QIcon.Normal, QIcon.Off)
    windowOrDialog.setWindowIcon(icon)


def safeListGet(lst, idx, default):
    try:
        return lst[idx]
    except IndexError:
        return default


def buildMessageBox(title, text, icon, buttons, defaultButton):
    msgBox = QMessageBox()

    msgBox.setIcon(icon)
    msgBox.setWindowTitle(title)
    msgBox.setText(text)
    msgBox.setStandardButtons(buttons)
    msgBox.setDefaultButton(defaultButton)

    return msgBox


class FloatDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        QStyledItemDelegate.__init__(self, parent=parent)

    def createEditor(self, parent, option, index):
        editor = QDoubleSpinBox(parent)
        editor.setDecimals(NUMBERS_PRECISION)
        editor.setMaximum(10**8)
        editor.setMinimum(-10**8)
        return editor

    def displayText(self, value, locale):
        # Грязный хак, скорее всего нужно было использовать locale
        return f'{value:.{NUMBERS_PRECISION}f}'
