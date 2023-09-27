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

        image_path = resource_path('images/sticker.gif')
        movie = QMovie(image_path)
        self.ui.labelgif.setMovie(movie)
        movie.start()
        self.movie = movie
        self.setFixedSize(self.size())

        version = importlib_metadata.version(__package__ or __name__)
        self.ui.versionLabel.setText(f"Версия: {version}")
