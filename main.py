from kivy.app import App

from app.settings import setup
from app.GUI.widgets import Root


class PymodoroApp(App):
    def build(self):
        return Root()


if __name__ == '__main__':
    setup()
    PymodoroApp().run()
