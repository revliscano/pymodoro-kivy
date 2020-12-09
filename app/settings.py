import os
from kivy.lang import Builder


OS_SETTINGS = {
    'KIVY_TEXT': 'pil'
}
KV_PATH = 'app/GUI/pymodoro.kv'


def setup():
    Builder.load_file(KV_PATH)
    os.environ.update(OS_SETTINGS)
