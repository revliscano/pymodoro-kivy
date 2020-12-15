from collections import namedtuple


PomodoroCounterConfiguration = namedtuple(
    typename='PomodoroCounterConfiguration',
    field_names=[
        'pomodoro_duration',
        'break_duration',
        'long_break_duration',
        'long_break_after'
    ]
)

DEFAULT_CONFIGURATION = PomodoroCounterConfiguration(
    pomodoro_duration=25,
    break_duration=5,
    long_break_duration=20,
    long_break_after=4
)


class PomodoroCounter:
    def __init__(self, configuration):
        self.configuration = configuration
        self.current_lapse = configuration.pomodoro_duration
        self.previous_lapse = 0
        self.pomodoros_count = 0

    @property
    def next_lapse(self):
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

    def update_after_lapse_ends(self):
        self.previous_lapse = self.current_lapse
        self.current_lapse = self.next_lapse
        if self._just_finished_a_pomodoro():
            self.pomodoros_count += 1

    def get_count(self):
        return self.pomodoros_count

