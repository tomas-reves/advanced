from kursas import Course
import unittest
from unittest import TestCase
import datetime

class TestCourse(unittest.TestCase):
    validation_names = [("C++", "C++"), ("Javascript", "Javascript")]
    validation_for_days_count = [(10, 5, 2), (100, 4, 25)]

    def setUp(self):
        cancelled_dates = [datetime.date(2022, 5, 4), datetime.date(2022, 5, 11)]
        self.c = Course("Python", 12, 3, datetime.date(2022, 4, 28), cancelled_dates)

    def test_if_returns_correct_name(self):
        for actual, expected in self.validation_names:
            with self.subTest():
                self.c.name = actual
                self.assertEqual(self.c.name, expected)

    def test_if_day_count_is_correct(self):
        expected_dienu_skaicius = 4
        self.assertEqual(expected_dienu_skaicius, self.c.days_count)


    def test_if_day_count_is_longer_than_0(self):
        self.assertGreater(self.c.days_count, 0)

    def test_if_date_moving_year_forward_works(self):
        expected_date = datetime.date(2022, 4, 28)
        self.assertEqual(expected_date, self.c._start_date)

    def test_if_second_date_calculated_correctly(self):
        expected_data = datetime.date(2022, 5, 2)
        actual_data = self.c.calculate_dates()[1]
        self.assertEqual(expected_data, actual_data)

    def test_if_second_date_calculated_correctly_when_2nd_may_cancelled(self):
        self.c.cancelled_dates = [datetime.date(2022, 5, 2)]
        expected_data = datetime.date(2022, 5, 2)
        actual_data = self.c.calculate_dates()[1]
        self.assertEqual(expected_data, actual_data)

#
# def test_if_second_day_is_calculated_correct(self):


if __name__ == '__main__':
    unittest.main()