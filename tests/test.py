from decimal import DivisionByZero
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils
import unittest

class Testing(unittest.TestCase):
    def test_zero(self):
        with self.assertRaises(ZeroDivisionError):
            a = 8
            b = 0
            utils.test_division(a,b)

if __name__ == '__main__':
    unittest.main()