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
import matplotlib.pyplot as plt
import matplotlib as mpl
import sympy
from PySide2 import QtCore, QtGui
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QHeaderView, QStyleOptionHeader, QStyle
from matplotlib.backends.backend_agg import FigureCanvasAgg

# Основано на https://stackoverflow.com/questions/32035251/

plt.rc('mathtext', fontset='cm')


def mathTexToQPixMap(mathTex, fs):
    # ---- set up a mpl figure instance ----
    fig = mpl.figure.Figure()
    fig.patch.set_facecolor('none')
    fig.set_canvas(FigureCanvasAgg(fig))
    renderer = fig.canvas.get_renderer()
    # ---- plot the mathTex expression ----
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    ax.patch.set_facecolor('none')
    t = ax.text(0, 0, f'${mathTex}$', ha='left', va='bottom', fontsize=fs)
    # ---- fit figure size to text artist ----
    fWidth, fHeight = fig.get_size_inches()
    figBBox = fig.get_window_extent(renderer)
    textBBox = t.get_window_extent(renderer)
    tightFWidth = textBBox.width * fWidth / figBBox.width
    tightFHeight = textBBox.height * fHeight / figBBox.height
    fig.set_size_inches(tightFWidth, tightFHeight)
    # ---- convert mpl figure to QPixmap ----
    buf, size = fig.canvas.print_to_buffer()

    return QtGui.QPixmap(
        QtGui.QImage.rgbSwapped(
            QtGui.QImage(
                buf, size[0], size[1], QtGui.QImage.Format_ARGB32
            )
        )
    )


class CacheQPixMap(dict):
    def get(self, __key):
        v = super().get(__key)
        if v is None:
            v = mathTexToQPixMap(sympy.latex(sympy.sympify(__key)), 14)
            super().__setitem__(__key, v)
        return v


class MathTexHeaderView(QHeaderView):
    def __init__(self, view, orientation=QtCore.Qt.Vertical):
        super().__init__(orientation, view)

        if orientation == QtCore.Qt.Vertical:
            self.setStyleSheet(
                "QHeaderView::section { padding-left: 15px; padding-right: 15px }"
            )

        self.converter = CacheQPixMap()

    def paintSection(self, painter, rect, logicalIndex):
        opt = QStyleOptionHeader()
        self.initStyleOption(opt)

        opt.rect = rect
        opt.section = logicalIndex
        opt.text = ""

        mousePos = self.mapFromGlobal(QtGui.QCursor.pos())
        if rect.contains(mousePos):
            opt.state |= QStyle.State_MouseOver

        painter.save()
        self.style().drawControl(QStyle.CE_Header, opt, painter, self)
        painter.restore()

        data = self.model().headerData(logicalIndex, self.orientation(), Qt.DisplayRole)

        if data:
            qPixMap = self.converter.get(data)
            xPix = (rect.width() - qPixMap.size().width()) / 2. + rect.x()
            yPix = (rect.height() - qPixMap.size().height()) / 2. + rect.y()
            rect = QtCore.QRect(xPix, yPix, qPixMap.size().width(),
                                qPixMap.size().height())
            painter.drawPixmap(rect, qPixMap)
