import os
from collections import namedtuple

from kivy.app import App
from kivy.core.audio import SoundLoader

from app.settings import setup, ASSETS_PATH
from app.ui.widgets import Root
from app.app.pomodoro_counter import (
    PomodoroCounter, DEFAULT_CONFIGURATION
)


class PymodoroApp(App):
    def build(self):
        tictoc_sound, beep_sound = self.load_sounds()
        pomodoro_counter = PomodoroCounter(DEFAULT_CONFIGURATION)
        return Root(
            pomodoro_counter=pomodoro_counter,
            tictoc_sound=tictoc_sound,
            beep_sound=beep_sound
        )

    @staticmethod
    def load_sounds():
        SoundConfiguration = namedtuple(
            typename='SoundConfiguration',
            field_names=['path', 'loop', 'volume']
        )
        sound_configurations = [
            SoundConfiguration('sounds/tictoc.mp3', True, 0.20),
            SoundConfiguration('sounds/beep.mp3', False, 1)
        ]
        for sound_configuration in sound_configurations:
            sound = SoundLoader.load(
                os.path.join(ASSETS_PATH, sound_configuration.path)
            )
            sound.volume = sound_configuration.volume
            sound.loop = sound_configuration.loop
            yield sound


if __name__ == '__main__':
    setup()
    PymodoroApp().run()
