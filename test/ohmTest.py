import sys
import unittest

from cEV.basicElements import Resistor, Voltage
from cEV.compiler import CEVCompiler


class ohmTest(unittest.TestCase):
    def execute(self, line: str):
        compiler = CEVCompiler()

        try:
            return compiler.executeLine(line)
        except:
            code = compiler.compileLine(line)
            i = 0

            print(line, file=sys.stderr)

            for line in code:
                print("%d:%s" % (i, line), file=sys.stderr)
                i += 1
            print("<EOF>", file=sys.stderr)
            raise

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

    def test_volatage(self):

        self.assertEqual(self.execute("U(1R,I=1A)"), Voltage(1))
