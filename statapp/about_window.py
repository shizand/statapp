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
import sys
from PySide2.QtGui import QMovie
from PySide2.QtWidgets import QMainWindow

from statapp.ui.ui_about_window import Ui_AboutWindow
from statapp.utils import resource_path

if sys.version_info < (3, 8):
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata


class AboutWindow(QMainWindow):
    movie = None

    def __init__(self):
        super().__init__()
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self)

        image_path = resource_path('ui/images/sticker.gif')
        movie = QMovie(image_path)
        self.ui.labelgif.setMovie(movie)
        movie.start()
        self.movie = movie
        self.setFixedSize(self.size())

        version = importlib_metadata.version(__package__ or __name__)
        self.ui.versionLabel.setText(f"Версия: {version}")
