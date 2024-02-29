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
from statapp.calculations import RegressionResult
from statapp.models.ro_table_model import ROTableModel


class RegressionResultModel(ROTableModel):
    def __init__(self, result: RegressionResult):
        data = result.paramsAndImportance
        super().__init__(data)
        self._monomials = result.monomials

    def getHorizontalHeader(self):
        return ['Коэффициент регрессии', 'Коэффициент значимости', 'Весовые коэффициенты']

    def getVerticalHeader(self):
        return self._monomials
