import unittest

from studentas import Studentas
from unittest import TestCase
# from cmath import exp
#
# import datetime
# from studentas import Studentas
# from unittest import TestCase

class TestStudent(unittest.TestCase):
    validation_credits_list = [(0, 0), [30, 30], [15, 15], [-15, 0], [31, 30], [100, 30]]
    zero_credits_list = [-1, -7, -101]
    thirty_credits_list = [31, 59, 1000]

    def setUp(self):
        self.studentas = Studentas("Tomas", 54)

    def test_if_right_amount_of_credits_assigned(self):
        for actual, expected in self.validation_credits_list:
            with self.subTest():
                self.studentas.credits = actual
                self.assertEqual(self.studentas.credits, expected)

    def test_if_returned_credits_are_equal_to_zero(self):
        for actual in self.zero_credits_list:
            with self.subTest():
                self.studentas.credits = actual
                self.assertGreaterEqual(self.studentas.credits, 0)

    def test_if_credits_are_equal_to_30(self):
        for actual in self.thirty_credits_list:
            with self.subTest():
                self.studentas.credits = actual
                self.assertLessEqual(self.studentas.credits, 30)

if __name__ == '__main__':
    unittest.main()