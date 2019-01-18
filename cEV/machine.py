from __future__ import annotations

from collections import deque

from cEV.OpCodes import OpCodes
from cEV.basicElements import Resistor, Voltage


class Stack(deque):
    push = deque.append

    def top(self):
        return self[-1]


class Machine:
    __dispatch_map = dict()

    def __init__(self, code):
        self.data_stack = Stack()
        self.return_addr_stack = Stack()
        self.instruction_pointer = 0
        self.code = code

    @staticmethod
    def register(opcode: OpCodes):
        def helper(func):
            Machine.__dispatch_map[opcode] = func
            return func

        return helper

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
        if op in self.__dispatch_map:
            self.__dispatch_map[op](self)
        elif isinstance(op, int) or isinstance(op, float):
            self.push(op)
        elif isinstance(op, str):
            self.push(op)
        else:
            raise RuntimeError("Unknown opcode: '%s'" % op)


@Machine.register(OpCodes.CREATE_RESISTOR)
def __create_resitor(self: Machine):
    self.push(Resistor())


@Machine.register(OpCodes.CREATE_VOLTAGESOURCE)
def __create_voltage(self: Machine):
    self.push(Voltage())


@Machine.register(OpCodes.SET_VALUE)
def __set_value(self: Machine):
    value = self.pop()
    element = self.pop()
    element.value = value
    self.push(element)


@Machine.register(OpCodes.CALC_SERIES)
def __calc_series(self: Machine):
    self.push(self.pop() + self.pop())


@Machine.register(OpCodes.CALC_PARALLEL)
def __calc_parallel(self: Machine):
    self.push(self.pop() | self.pop())


@Machine.register(OpCodes.CREATE_DICT)
def __create_dict(self: Machine):
    self.push(dict())


@Machine.register(OpCodes.ADD_KEY_VALUE)
def __create_dict(self: Machine):
    value = self.pop()
    key = self.pop()
    value_dict = self.pop()

    value_dict[key] = value
    self.push(value_dict)


@Machine.register(OpCodes.CALC_VOLTAGE)
def __calc_volage(self: Machine):
    kargs = self.pop()
    item = self.pop()

    result = item.calc_voltage(**kargs)
    self.push(result)
