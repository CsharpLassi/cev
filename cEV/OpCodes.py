from enum import Enum, unique,auto


@unique
class OpCodes(Enum):
    CREATE_RESISTOR = auto()
    CREATE_VOLTAGESOURCE = auto()
    SET_VALUE = auto()
    CALC_SERIES = auto()
    CALC_PARALLEL = auto()
