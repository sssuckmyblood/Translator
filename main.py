import main_ui

from googletrans import Translator

translator = Translator()


def translate_action(text):
    return translator.translate(text, src="ru", dest="en").text