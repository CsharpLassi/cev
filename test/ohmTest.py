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

    def test_series_connection(self):
        compiler = CEVCompiler()

        self.assertEqual(compiler.executeLine("10R + 20R"), Resistor(30))

        self.assertEqual(compiler.executeLine("10R + 20R +3 R"), Resistor(33))

    def test_parallel_connection(self):
        compiler = CEVCompiler()

        self.assertEqual(compiler.executeLine("10R || 10R"), Resistor(5))
        self.assertEqual(compiler.executeLine("10R || 10R || 5R"), Resistor(2.5))

    def test_seriel_parallel_connection(self):
        compiler = CEVCompiler()

        self.assertEqual(compiler.executeLine("5R + 5R || 10R"), Resistor(5))
