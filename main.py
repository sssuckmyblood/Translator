import main_ui
import sqlite


db = sqlite.connect_db()

def translate_action(text, origin, dest):
        from googletrans import Translator
        translator = Translator()
        return translator.translate(text, src=origin, dest=dest).text