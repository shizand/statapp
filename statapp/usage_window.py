#
# Copyright (c) 2024 Maxim Slipenko, Eugene Lazurenko.
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
from PySide2.QtCore import QUrl
from PySide2.QtGui import QDesktopServices
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from statapp.utils import addIcon, resourcePath

class ExternalLinksWebEnginePage(QWebEnginePage):
    def acceptNavigationRequest(self, url, _type, isMainFrame):
        if _type == QWebEnginePage.NavigationTypeLinkClicked:
            QDesktopServices.openUrl(url)
            return False  # Prevent the internal view from navigating to the URL
        return True  # Handle all other navigation requests normally

class UsageWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Использование")
        addIcon(self)

        layout = QVBoxLayout()

        self.browser = QWebEngineView()
        customPage = ExternalLinksWebEnginePage(self.browser)
        self.browser.setPage(customPage)

        layout.addWidget(self.browser)

        self.browser.load(QUrl.fromLocalFile(resourcePath("docs/README.html")))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def onLinkClicked(self, url):
        # Open the URL in the default web browser instead of the QWebEngineView
        QDesktopServices.openUrl(url)