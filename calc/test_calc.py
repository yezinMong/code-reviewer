from unittest import TestCase
from calc import Calc


class TestCalc(TestCase):
    def test_getSum(self):
        calc = Calc()
        self.assertEqual(3, calc.getSum(1, 2))

    def test_getGop(self):
        calc = Calc()
        self.assertEqual(2, calc.getGop(1, 2))

    def test_getZegop(self):
        calc = Calc()
        self.assertEqual(4, calc.getZegop(2))

    def test_getMinus(self):
        calc = Calc()
        self.assertEqual(1, calc.getMinus(2, 1))

    def test_getDivide(self):
        calc = Calc()
        self.assertEqual(2, calc.getDivide(4, 2))

    def test_getSumSum(self):
        calc = Calc()
        self.assertEqual(6, calc.getSumSum(1, 2, 3))