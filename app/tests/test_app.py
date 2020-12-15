import unittest

from app.app.pomodoro_counter import (
    PomodoroCounter, PomodoroCounterConfiguration
)


class PomodoroCounterTestCase(unittest.TestCase):
    def setUp(self):
        configuration = PomodoroCounterConfiguration(
            pomodoro_duration=2,
            break_duration=1,
            long_break_duration=3,
            long_break_after=2
        )
        self.pomodoro_counter = PomodoroCounter(configuration)

    def test_break_after_one_pomodoro(self):
        self._perform_pomodoros(1)
        self.assertEqual(self.pomodoro_counter.next_lapse, 1)

    def test_long_break_after_two_pomodoros(self):
        self._perform_pomodoros(2)
        self.assertEqual(self.pomodoro_counter.next_lapse, 3)

    def test_pomodoro_after_long_break(self):
        self._perform_pomodoros(2)
        self.pomodoro_counter.update_after_lapse_ends()
        self.assertEqual(self.pomodoro_counter.next_lapse, 2)

    def test_pomodoros_count(self):
        self._perform_pomodoros(10)
        self.assertEqual(self.pomodoro_counter.get_count(), 10)

    def _perform_pomodoros(self, n):
        number_of_lapses = (n * 2) - 1
        for lapse in range(1, number_of_lapses + 1):
            self.pomodoro_counter.update_after_lapse_ends()
