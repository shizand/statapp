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
import sys

import numpy as np
import pandas as pd
from PySide2 import QtCore
from PySide2.QtWidgets import QApplication

from statapp.calculations import linearPolynom
from statapp.main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    translator = QtCore.QTranslator(app)
    locale = QtCore.QLocale.system().name()
    path = QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath)
    translator.load(f'qt_{locale}', path)
    app.installTranslator(translator)

    window = MainWindow()
    window.show()
    return app.exec_()

data = [
    [6014.700000,  2995.067340,  2982.474660],
    [6031.200000,  2971.594560,  2993.546160],
    [6145.800000,  3017.328000,  2970.497280],
    [6133.200000,  2977.476480,  2970.796320],
    [6063.600000,  3006.012960,  2982.839040],
    [5934.900000,  2979.831420,  2992.026240],
    [6016.800000,  2997.121680,  2984.065920],
    [6070.200000,  2996.335920,  2975.729640],
    [5935.800000,  2982.114960,  2976.811560],
    [6108.300000,  2987.822700,  2974.378500]
]

data = pd.DataFrame(data).to_numpy()

if __name__ == "__main__":
    n = len(data)

    # y = generateYValues(100, 5, n)
    # x1 = generateXValues(20, 2, 0, y)
    # x2 = generateXValues(10, 1, 0, y)
    # x3 = generateXValues(5, 0, 0, y)
    # y = np.array([18, 19, 22, 20, 24, 23])
    # x1 = np.array([13, 14, 15, 17, 16, 15])
    # x2 = np.array([18, 19, 22, 20, 24, 23])

    # data = np.concatenate([y, x1, x2, x3], axis=1)

    res = linearPolynom(data)

    solution = res[0]
    residues = res[1]
    rank = res[2]

    SSE = np.sum(residues)

    print(SSE)

    df = n - rank

    MSE = SSE / df

    # MSE = np.mean(residues)
    SSE = np.sum(residues)

    print("Остаточная дисперсия (MSE = S^2):", MSE)

    # sys.exit(main())
