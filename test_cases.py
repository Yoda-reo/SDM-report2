#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc(unittest.TestCase):

    def test_sample1 (self):
        self.assertEqual(6, calc(2, 3))
        self.assertEqual(20, calc(5, 4))

    def test_sample2 (self):
        self.assertEqual(-1, calc(0, 5))
        self.assertEqual(-1, calc(7, 0))
        self.assertEqual(-1, calc(0, 0))

    def test_sample3 (self):
        self.assertEqual(-1 ,calc(-2, 3))
        self.assertEqual(-1, calc(2, -3))
        self.assertEqual(-1, calc(-2, -3))

    def test_sample4 (self):
        self.assertEqual(1, calc(1, 1))
        self.assertEqual(-1, calc(-1, 1))
        self.assertEqual(-1, calc(1, -1))
        self.assertEqual(-1, calc(-1, -1))
