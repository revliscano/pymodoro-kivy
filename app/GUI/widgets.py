from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, NumericProperty
from kivy.clock import Clock
from .seconds_formatter import SecondsFormatter


EVERY_SECOND = 1


class Root(Widget):
    pomodoro_counter = ObjectProperty()
    timer = ObjectProperty()
    seconds_elapsed = NumericProperty(defaultvalue=0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def start_pomodoro(self, event):
        self.restart()
        self.switch_buttons()
        self.timer = Clock.schedule_interval(
            self.run_timer,
            EVERY_SECOND
        )

    def restart(self):
        self.seconds_elapsed = 0
        self.ids.timer_label.bring_back_to_zero()
        self.ids.up_to_label.update(self.pomodoro_counter.next_lapse)

    def switch_buttons(self):
        self.ids.start_next_lapse_button.switch()
        self.ids.abort_lapse_button.switch()

    def run_timer(self, event):
        self.seconds_elapsed += 1
        self.ids.timer_label.refresh_text(self.seconds_elapsed)
        if self.is_lapse_done():
            self.finish_pomodoro()

    def is_lapse_done(self):
        return self.seconds_elapsed == self.pomodoro_counter.next_lapse

    def finish_pomodoro(self):
        self.pomodoro_counter.update_after_lapse_ends()
        self.tear_down()

    def tear_down(self):
        Clock.unschedule(self.timer)
        self.switch_buttons()

    def abort_lapse(self, event):
        self.tear_down()
        self.restart()


class UpToLabel(Label):
    def on_parent(self, obj, parent):
        pomodoro_length = self.parent.parent.pomodoro_counter.next_lapse
        self.update(pomodoro_length)

    def update(self, next_lapse):
        self.text = str(SecondsFormatter(next_lapse))


class TimerLabel(Label):
    def on_parent(self, obj, parent):
        self.bring_back_to_zero()

    def bring_back_to_zero(self):
        self.text = str(SecondsFormatter(0))

    def refresh_text(self, seconds):
        self.text = str(SecondsFormatter(seconds))


class Switchable:
    def switch(self):
        self.disabled = not self.disabled


class StartNextLapse(Button, Switchable):
    def on_parent(self, obj, parent):
        self.bind(on_press=parent.start_pomodoro)


class AbortLapse(Button, Switchable):
    def on_parent(self, obj, parent):
        self.bind(on_press=parent.abort_lapse)
