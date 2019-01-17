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

    def __repr__(self):
        return "R: %d Ohm" % self.value
