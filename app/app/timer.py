from time import time
from collections import namedtuple


class Timer:
    TIME_MODULE = 0.00001

    def __init__(self):
        self._current_time = 0

    def run(self, seconds):
        while self._current_time < seconds:
            self._update_current_time()

    def _update_current_time(self):
        if self._has_passed_one_second():
            self._current_time += 1

    def _has_passed_one_second(self):
        return self.TIME_MODULE > time() % 1

    def get_current_time(self):
        return self._current_time


PomodoroClockConfiguration = namedtuple(
    typename='PomodoroClockConfiguration',
    field_names=[
        'pomodoro_duration',
        'break_duration',
        'long_break_duration',
        'long_break_after'
    ]
)


class PomodoroClock:
    def __init__(self, timer, configuration):
        self.timer = timer
        self.configuration = configuration
        self.pomodoros_count = 0
        self.previous_lapse = 0

    def start(self):
        lapse = self.get_next_lapse()
        self.timer.run(lapse)
        self.previous_lapse = lapse
        if lapse == self.configuration.pomodoro_duration:
            self.pomodoros_count += 1

    def get_next_lapse(self):
        if self._just_finished_a_pomodoro():
            return (
                self.configuration.long_break_duration
                if self._its_time_for_long_break()
                else self.configuration.break_duration
            )
        return self.configuration.pomodoro_duration

    def _just_finished_a_pomodoro(self):
        return (
            self.previous_lapse == self.configuration.pomodoro_duration
        )

    def _its_time_for_long_break(self):
        return (
            self.pomodoros_count % self.configuration.long_break_after == 0
        )
