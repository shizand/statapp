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
from PySide2.QtCore import Qt

from statapp.models.ro_table_model import ROTableModel


class PreditionTableModel(ROTableModel):
    def getHorizontalHeader(self):
        return ['Отклик', 'Прогноз', 'Отклонение', '1-3 сигмовые зоны']

    def data(self, index, role):
        if role == Qt.DisplayRole and index.column() == 3:
            value = super().data(index, role)
            return 'x' if value == 1 else ''
        return super().data(index, role)
