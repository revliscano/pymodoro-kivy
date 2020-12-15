from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, BooleanProperty
from kivy.clock import Clock


class Root(Widget):
    pomodoro_counter = ObjectProperty()
    running = BooleanProperty(defaultvalue=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def start_pomodoro(self, event):
        Clock.schedule_once(
            self.finish_pomodoro,
            self.pomodoro_counter.next_lapse
        )

    def finish_pomodoro(self, event):
        self.pomodoro_counter.update_after_lapse_ends()
        self.running = False


class UpToLabel(Label):
    pass


class TimerLabel(Label):
    pass


class StartNextLapse(Button):
    def on_parent(self, obj, parent):
        self.bind(on_press=parent.start_pomodoro)
