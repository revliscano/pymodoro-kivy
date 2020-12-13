import time


class Timer:
    def __init__(self):
        self._current_time = 0

    def run(self, seconds):
        while self._current_time < seconds:
            time.sleep(1)
            self._current_time += 1

    def get_current_time(self):
        return self._current_time


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
        if lapse == self.configuration['pomodoro_duration']:
            self.pomodoros_count += 1

    def get_next_lapse(self):
        if self._just_finished_a_pomodoro():
            return (
                self.configuration['long_break_duration']
                if self._its_time_for_long_break()
                else self.configuration['break_duration']
            )
        return self.configuration['pomodoro_duration']

    def _just_finished_a_pomodoro(self):
        return (
            self.previous_lapse == self.configuration['pomodoro_duration']
        )

    def _its_time_for_long_break(self):
        return (
            self.pomodoros_count % self.configuration['long_break_after'] == 0
        )
