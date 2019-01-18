class Resistor:
    def __init__(self, value: float = 0):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, Resistor):
            return other.value == self.value

        return False

    def __add__(self, other):
        if isinstance(other, Resistor):
            return Resistor(self.value + other.value)

        raise RuntimeError("Add is not allowed with '%s'" % other)

    def __or__(self, other):
        if isinstance(other, Resistor):
            return Resistor(self.value * other.value / (self.value + other.value))

        raise RuntimeError("Add is not allowed with '%s'" % other)

    def calc_voltage(self, i: float = None):
        return Voltage(self.value * i)

    def __repr__(self):
        return "R: %d Ohm" % self.value


class Voltage:
    def __init__(self, value: float = 0):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, Voltage):
            return other.value == self.value

        return False

    def __repr__(self):
        return "U: %d V" % self.value
