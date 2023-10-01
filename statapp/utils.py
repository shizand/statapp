import os
import sys

from PySide2.QtWidgets import QMessageBox


def resource_path(relative):
    if getattr(sys, 'frozen', False):
        bundle_dir = sys._MEIPASS
    else:
        # we are running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(bundle_dir, relative)


def safe_list_get(l, idx, default):
    try:
        return l[idx]
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
