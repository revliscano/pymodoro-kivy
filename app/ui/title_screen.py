from kivy.uix.screenmanager import Screen
from kivy.uix.modalview import ModalView
from kivy.uix.button import Button
from kivy.app import App


class TitleScreen(Screen):
    pass


class NormalSession(Button):
    def on_parent(self, obj, parent):
        self.bind(on_press=self.start_session)

    def start_session(self, event):
        app = App.get_running_app()
        app.switch_to_main_screen()


class CustomSession(Button):
    def on_parent(self, obj, parent):
        self.bind(on_press=self.open_modal)

    def open_modal(self, event):
        modal = CustomSessionModal()
        modal.open()


class CustomSessionModal(ModalView):
    pass
