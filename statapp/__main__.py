import sys

from PySide2 import QtCore
from PySide2.QtWidgets import QApplication

from statapp.main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    translator = QtCore.QTranslator(app)
    locale = QtCore.QLocale.system().name()
    path = QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath)
    translator.load('qt_%s' % locale, path)
    app.installTranslator(translator)

    window = MainWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())
