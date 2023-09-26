import os
import sys


def resource_path(relative):
    if getattr(sys, 'frozen', False):
        bundle_dir = sys._MEIPASS
    else:
        # we are running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(__file__))
    print(bundle_dir)
    return os.path.join(bundle_dir, relative)
