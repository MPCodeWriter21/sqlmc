###################################################################
# This file is licensed under the Affero General Public License   #
#                  Version 3 (AGPLv3)                             #
#                                                                 #
# You should have received a copy of the GNU Affero General       #
# Public License along with this program. If not, see             #
# <https://www.gnu.org/licenses/agpl-3.0.html>.                   #
#                                                                 #
# Author: thegexi@gmail.com                                       #
###################################################################

from dataclasses import dataclass

@dataclass
class SqlInjectionReport:
    error: bool
    db: str

@dataclass
class Form:
    url: str
    inputs: list

@dataclass
class FormSumbit:
    url: str
    data: str