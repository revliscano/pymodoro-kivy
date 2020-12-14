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

    def test_break_after_pomodoro(self):
        self.pomodoro_counter.update_after_lapse_ends()
        next_lapse = self.pomodoro_counter.next_lapse
        self.assertEqual(next_lapse, 1)

    def test_long_break_after_2_pomodoros(self):
        self.pomodoro_counter.update_after_lapse_ends()
        self.pomodoro_counter.update_after_lapse_ends()
        self.pomodoro_counter.update_after_lapse_ends()
        self.assertEqual(self.pomodoro_counter.next_lapse, 3)

    def test_pomodoro_after_long_break(self):
        self.pomodoro_counter.update_after_lapse_ends()
        self.pomodoro_counter.update_after_lapse_ends()
        self.pomodoro_counter.update_after_lapse_ends()
        self.pomodoro_counter.update_after_lapse_ends()
        self.assertEqual(self.pomodoro_counter.next_lapse, 2)
