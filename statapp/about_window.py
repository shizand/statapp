from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QMainWindow

from statapp.ui.ui_about_window import Ui_AboutWindow


class AboutWindow(QMainWindow):
    pixmap = None

    def __init__(self):
        super().__init__()
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self)

        image_path = 'statapp\\images\\sticker.gif'
        movie = QMovie(image_path)
        self.ui.labelgif.setMovie(movie)
        movie.start()

        self.pixmap = movie
        self.setFixedSize(self.size())
