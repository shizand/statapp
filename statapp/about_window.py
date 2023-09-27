from PySide2.QtGui import QMovie
from PySide2.QtWidgets import QMainWindow

from statapp.ui.ui_about_window import Ui_AboutWindow
from statapp.utils import resource_path


class AboutWindow(QMainWindow):
    pixmap = None

    def __init__(self):
        super().__init__()
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self)

        image_path = resource_path('images/sticker.gif')

        movie = QMovie(image_path)
        self.ui.labelgif.setMovie(movie)
        movie.start()

        self.pixmap = movie
        self.setFixedSize(self.size())
