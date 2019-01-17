import unittest

from cEV.basicElements import Resistor
from cEV.compiler import CEVCompiler


class ohmTest(unittest.TestCase):
    def test_single_instance(self):
        compiler = CEVCompiler()

        goal = Resistor(10)

        self.assertEqual(compiler.executeLine("10 Ohm"), goal)
        self.assertEqual(compiler.executeLine("10Ohm"), goal)
        self.assertEqual(compiler.executeLine("10R"), goal)
