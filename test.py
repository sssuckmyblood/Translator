
from googletrans import Translator




translator = Translator()

o_text = input("Введите слово: ")

result = translator.translate(o_text, src="ru", dest="en")

print(result.text)