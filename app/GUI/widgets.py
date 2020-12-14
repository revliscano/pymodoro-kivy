from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.clock import Clock


class Root(Widget):
    pomodoro_counter = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def start_pomodoro(self, event):
        Clock.schedule_interval(lambda *x: print('.'), 1)


class UpToLabel(Label):
    pass


class TimerLabel(Label):
    pass


class StartNextLapse(Button):
    def on_parent(self, obj, parent):
        self.bind(on_press=parent.start_pomodoro)
