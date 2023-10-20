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

from statapp._vendor.multipolyfit import get_terms
from statapp.models.linear_polynom_model import LinearPolynomModel


class SquaredPolynomModel(LinearPolynomModel):
    powers: list

    def getVerticalHeader(self):
        return ['c' if str(x) == '1' else str(x) for x in get_terms(self.powers)]
