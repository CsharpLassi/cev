import unittest

from cEV.basicElements import Voltage
from cEV.compiler import CEVCompiler


class VolategTest(unittest.TestCase):
    def test_instance(self):
        compiler = CEVCompiler()

        self.assertEqual(compiler.executeLine('3V'), Voltage(3))
