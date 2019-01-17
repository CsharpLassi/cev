from collections import deque

from cEV.OpCodes import OpCodes
from cEV.basicElements import Resistor


class Stack(deque):
    push = deque.append

    def top(self):
        return self[-1]


class Machine:
    def __init__(self, code):
        self.data_stack = Stack()
        self.return_addr_stack = Stack()
        self.instruction_pointer = 0
        self.code = code
        self.dispatch_map = {
            OpCodes.CREATE_RESISTOR: self.__create_resitor,
            OpCodes.SET_VALUE: self.__set_value,
            OpCodes.CALC_SERIES: self.__calc_series,
                             }

    def run(self):
        while self.instruction_pointer < len(self.code):
            opcode = self.code[self.instruction_pointer]
            self.instruction_pointer += 1
            self.dispatch(opcode)

    def pop(self):
        return self.data_stack.pop()

    def push(self, value):
        self.data_stack.push(value)

    def top(self):
        return self.data_stack.top()

    def dispatch(self, op):
        if op in self.dispatch_map:
            self.dispatch_map[op]()
        elif isinstance(op, int) or isinstance(op, float):
            self.push(op)
        else:
            raise RuntimeError("Unknown opcode: '%s'" % op)

    def __create_resitor(self):
        self.push(Resistor())

    def __set_value(self):
        value = self.pop()
        element = self.pop()
        element.value = value
        self.push(element)

    def __calc_series(self):
        self.push(self.pop() + self.pop())
