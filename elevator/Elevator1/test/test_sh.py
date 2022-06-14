# https://betterprogramming.pub/how-to-create-a-post-request-in-fastapi-3dbd017dd998/
import unittest, sys
import pytest
from unittest.mock import MagicMock

# sys.path.append('../')
from src.checker import *
# from utils import * # will test a little

# class TestChecker(unittest.TestCase):
#     def test_outsideRequest_lowerbound(self) -> None:
#         result = Checker.check_outside_request(1,1)
#         self.assertEqual(result, True)

class TestCheckFloor(unittest.TestCase):
    def test_negative_basic(self):
        with self.assertRaises(Exception):
            Checker.check_floor(-1,1)

    def test_negative_complex_small(self):
        with self.assertRaises(Exception):
            Checker.check_floor(-1,11111111)
    
    def test_negative_complex_big(self):
        with self.assertRaises(Exception) as e:
            Checker.check_floor(-12234567, 1234567)
            self.assertEqual('The floor number can not be negative', str(e.exception)
)


if __name__ == '__main__':
    unittest.main()