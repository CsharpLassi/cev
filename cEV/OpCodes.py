from enum import Enum, unique, auto


@unique
class OpCodes(Enum):
    CREATE_RESISTOR = auto()
    CREATE_VOLTAGESOURCE = auto()
    SET_VALUE = auto()
    CALC_SERIES = auto()
    CALC_PARALLEL = auto()
    CALC_VOLTAGE = auto()
    CREATE_DICT = auto()
    ADD_KEY_VALUE = auto()
