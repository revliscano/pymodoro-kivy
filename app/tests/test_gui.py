import unittest

from app.GUI.seconds_formatter import SecondsFormatter


class NumberFormatterTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_formats_less_than_a_minute(self):
        seconds = 45
        formatted_seconds = SecondsFormatter(seconds)
        string_representation = str(formatted_seconds)
        self.assertEqual(string_representation, '00:45')

    def test_formats_minutes(self):
        two_minutes = SecondsFormatter(120)
        twenty_five_minutes = SecondsFormatter(1500)
        self.assertEqual(str(two_minutes), '02:00')
        self.assertEqual(str(twenty_five_minutes), '25:00')

    def test_secondsformatter_adding(self):
        five_seconds = SecondsFormatter(5)
        seven_seconds = five_seconds + 2
        self.assertEqual(str(seven_seconds), '00:07')
