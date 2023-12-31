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
from PySide2 import QtCore
from PySide2.QtWidgets import QComboBox, QItemDelegate


class ComboDelegate(QItemDelegate):
    commitData = QtCore.Signal(object)
    """
    A delegate that places a fully functioning QComboBox in every
    cell of the column to which it's applied
    """
    def __init__(self, parent, objects, objectNames):
        """
        Constructoe
        :param parent: QTableView parent object
        :param objects: List of objects to set. i.e. [True, False]
        :param objectNames: List of Object names to display. i.e. ['True', 'False']
        """
        QItemDelegate.__init__(self, parent)

        # objects to sent to the model associated to the combobox. i.e. [True, False]
        self.objects = objects

        # object description to display in the combobox. i.e. ['True', 'False']
        self.objectNames = objectNames

    @QtCore.Slot()
    def currentIndexChanged(self):
        self.commitData.emit(self.sender())

    def createEditor(self, parent, option, index):
        combo = QComboBox(parent)
        combo.addItems(self.objectNames)
        combo.currentIndexChanged.connect(self.currentIndexChanged)
        return combo

    def setEditorData(self, editor, index):
        editor.blockSignals(True)
        val = index.model().data(index, role=QtCore.Qt.DisplayRole)
        idx = self.objects.index(val)
        editor.setCurrentIndex(idx)
        editor.blockSignals(False)

    def setModelData(self, editor, model, index):
        model.setData(index, self.objects[editor.currentIndex()], QtCore.Qt.EditRole)
