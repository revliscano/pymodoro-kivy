import unittest
from app.app.timer import (
    Timer, PomodoroClock, PomodoroClockConfiguration
)


class TimerTestCase(unittest.TestCase):
    def setUp(self):
        self.timer = Timer()

    def test_timer_runs(self):
        seconds_to_wait = 1
        self.timer.run(seconds_to_wait)
        self.assertEqual(self.timer.get_current_time(), seconds_to_wait)


class PomodoroClockTestCase(unittest.TestCase):
    def setUp(self):
        timer = Timer()
        configuration = PomodoroClockConfiguration(
            pomodoro_duration=2,
            break_duration=1,
            long_break_duration=3,
            long_break_after=2
        )
        self.pomodoro_clock = PomodoroClock(timer, configuration)

    def test_break_after_pomodoro(self):
        self.pomodoro_clock.start()
        next_lapse = self.pomodoro_clock.get_next_lapse()
        self.assertEqual(next_lapse, 1)

    def test_long_break_after_2_pomodoros(self):
        # 1st pomodoro
        self.pomodoro_clock.start()
        # break
        self.pomodoro_clock.start()
        # 2nd pomodoro
        self.pomodoro_clock.start()

        next_lapse = self.pomodoro_clock.get_next_lapse()

        self.assertEqual(next_lapse, 3)

    def test_pomodoro_after_long_break(self):
        # 1st pomodoro
        self.pomodoro_clock.start()
        # break
        self.pomodoro_clock.start()
        # 2nd pomodoro
        self.pomodoro_clock.start()
        # long break
        self.pomodoro_clock.start()

        next_lapse = self.pomodoro_clock.get_next_lapse()

        self.assertEqual(next_lapse, 2)
