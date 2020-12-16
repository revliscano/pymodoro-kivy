from kivy.app import App

from app.settings import setup
from app.GUI.widgets import Root
from app.app.pomodoro_counter import (
    PomodoroCounter, DEFAULT_CONFIGURATION
)


class PymodoroApp(App):
    def build(self):
        pomodoro_counter = PomodoroCounter(DEFAULT_CONFIGURATION)
        return Root(pomodoro_counter=pomodoro_counter)


if __name__ == '__main__':
    setup()
    PymodoroApp().run()
