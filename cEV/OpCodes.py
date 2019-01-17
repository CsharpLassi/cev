from enum import Enum, unique


@unique
class OpCodes(Enum):
    CREATE_RESISTOR = 0
    SET_VALUE = 1
    CALC_SERIES = 2
