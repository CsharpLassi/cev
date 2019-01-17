class Resistor:
    def __init__(self, value: float = 0):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, Resistor):
            return other.value == self.value

        return False

    def __repr__(self):
        return "R: %d Ohm" % self.value
