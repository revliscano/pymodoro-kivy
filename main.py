import os

from kivy.app import App
from kivy.core.audio import SoundLoader


from app.settings import setup, ASSETS_PATH
from app.ui.widgets import Root
from app.app.pomodoro_counter import (
    PomodoroCounter, DEFAULT_CONFIGURATION, PomodoroCounterConfiguration
)

configuration = PomodoroCounterConfiguration(
    pomodoro_duration=2,
    break_duration=1,
    long_break_duration=3,
    long_break_after=2
)


class PymodoroApp(App):
    def build(self):
        tictoc_sound, beep_sound = self.load_sounds()
        pomodoro_counter = PomodoroCounter(configuration)
        return Root(
            pomodoro_counter=pomodoro_counter,
            tictoc_sound=tictoc_sound,
            beep_sound=beep_sound
        )

    def load_sounds(self):
        files = ['sounds/tictoc.mp3', 'sounds/beep.mp3']
        for file in files:
            sound = SoundLoader.load(
                os.path.join(ASSETS_PATH, file)
            )
            yield sound


if __name__ == '__main__':
    setup()
    PymodoroApp().run()
