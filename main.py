from kivy.app import App

from app.settings import setup
from app.GUI.widgets import Root
from app.app.pomodoro_counter import (
    PomodoroCounter, PomodoroCounterConfiguration, DEFAULT_CONFIGURATION
)


class PymodoroApp(App):
    def build(self):
        configuration = PomodoroCounterConfiguration(
            pomodoro_duration=2,
            break_duration=1,
            long_break_duration=3,
            long_break_after=2
        )
        pomodoro_counter = PomodoroCounter(configuration)
        return Root(pomodoro_counter=pomodoro_counter)


if __name__ == '__main__':
    setup()
    PymodoroApp().run()
