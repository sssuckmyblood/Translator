
from ui import main_ui
from googletrans import Translator
import sqllite

if __name__ == "__main__":
    import sys
    app = main_ui.QtWidgets.QApplication(sys.argv)
    MainWindow = main_ui.QtWidgets.QMainWindow()
    ui = main_ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




translator = Translator()

o_text = input("Введите слово: ")

result = translator.translate(o_text, src="ru", dest="en")

print(result.text)