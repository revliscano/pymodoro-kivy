import os
from collections import namedtuple

from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import ScreenManager

from app.settings import setup, ASSETS_PATH
from app.ui.main_screen import MainScreen, Root
from app.ui.title_screen import TitleScreen
from app.app.pomodoro_counter import (
    PomodoroCounter, DEFAULT_CONFIGURATION
)


class PymodoroApp(App):
    def __init__(self):
        super().__init__()
        self.screen_manager = ScreenManager()

    def build(self):
        self.switch_to_title_screen()
        return self.screen_manager

    def switch_to_title_screen(self):
        self.screen_manager.switch_to(
            TitleScreen(name='title_screen')
        )

    def switch_to_main_screen(self):
        root_widget = RootWidgetSetUp.prepare()
        self.screen_manager.switch_to(
            MainScreen(name='main_screen', root=root_widget)
        )


class RootWidgetSetUp:
    @classmethod
    def prepare(class_):
        tictoc_sound, beep_sound = class_.load_sounds()
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
