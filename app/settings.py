import os
from kivy.lang import Builder


OS_SETTINGS = {
    'KIVY_TEXT': 'pil'
}
ASSETS_PATH = 'app/assets'
KV_PATH = 'app/ui/pymodoro.kv'


def setup():
    Builder.load_file(KV_PATH)
    os.environ.update(OS_SETTINGS)
