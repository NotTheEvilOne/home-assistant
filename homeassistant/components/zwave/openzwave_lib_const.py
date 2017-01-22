"""openzwave.lib based Z-Wave Constants."""

from openzwave.lib.manager import COMMAND_CLASS
from openzwave.lib.value_id import ValueGenre, ValueType

__module_dict = vars()

__module_dict.update({ "COMMAND_CLASS_{0}".format(key): COMMAND_CLASS[key]
                       for key in COMMAND_CLASS
                     })

__module_dict.update({ "GENRE_{0}".format(key.upper()): ValueGenre[key]
                       for key in ValueGenre
                     })

__module_dict.update({ "TYPE_{0}".format(key.upper()): ValueType[key]
                       for key in ValueType
                     })
