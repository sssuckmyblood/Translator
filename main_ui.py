# -*- coding: utf-8 -*-
'''
Главный файл программы - главная форма, отсюда подключается модуль работы с google translate api и базы данных sqlite3
'''


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QHeaderView

import main


class Ui_MainWindow(object):
    data = {
        "РУССКИЙ": "ru",
        "БЕЛОРУССКИЙ": "be",
        "УКРАИНСКИЙ": "uk",
        "АНГЛИЙСКИЙ": "en",
        "НЕМЕЦКИЙ": "de",
        "ФРАНЦУЗСКИЙ": "fr",

    }

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(567, 167)
        MainWindow.setMinimumSize(567, 167)
        MainWindow.setMaximumSize(567, 167)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 567, 167))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.dest_lan = QtWidgets.QComboBox(self.tab)
        self.dest_lan.setGeometry(QtCore.QRect(338, 10, 184, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dest_lan.setFont(font)
        self.dest_lan.setObjectName("dest_lan")
        self.dest = QtWidgets.QLineEdit(self.tab)
        self.dest.setGeometry(QtCore.QRect(338, 40, 184, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dest.setFont(font)
        self.dest.setReadOnly(True)
        self.dest.setObjectName("dest")
        self.dest.setPlaceholderText("ПЕРЕВОД")
        self.origin_lan = QtWidgets.QComboBox(self.tab)
        self.origin_lan.setGeometry(QtCore.QRect(30, 10, 184, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.origin_lan.setFont(font)
        self.origin_lan.setObjectName("origin_lan")
        self.switch_lan = QtWidgets.QPushButton(self.tab)
        self.switch_lan.setGeometry(QtCore.QRect(239, 10, 80, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.switch_lan.setFont(font)
        self.switch_lan.setObjectName("switch_lan")
        self.origin = QtWidgets.QLineEdit(self.tab)
        self.origin.setGeometry(QtCore.QRect(30, 40, 184, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.origin.setFont(font)
        self.origin.setObjectName("origin")
        self.translate = QtWidgets.QPushButton(self.tab)
        self.translate.setGeometry(QtCore.QRect(202, 89, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.translate.setFont(font)
        self.translate.setObjectName("translate")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.db_combo = QtWidgets.QComboBox(self.tab_2)
        self.db_combo.setGeometry(QtCore.QRect(10, 10, 391, 28))
        self.db_combo.setObjectName("db_combo")
        font = QtGui.QFont()
        font.setPointSize(13)
        self.db_combo.setFont(font)
        self.search = QtWidgets.QPushButton(self.tab_2)
        self.search.setGeometry(QtCore.QRect(440, 10, 91, 28))
        self.search.setObjectName("search")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 391, 81))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setFont(font)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        for key, value in self.data.items():
            self.origin_lan.addItem(key, value)
            self.dest_lan.addItem(key, value)
        self.dest_lan.setCurrentIndex(1)

        self.translate.clicked.connect(self.translate_clicked)
        self.origin_lan.activated.connect(self.origin_lan_activated)
        self.dest_lan.activated.connect(self.dest_lan_activated)
        self.switch_lan.clicked.connect(self.switch_lan_clicked)
        self.tabWidget.currentChanged.connect(self.tab_change)
        self.search.clicked.connect(self.search_clicked)

    def tab_change(self, index):
        if index == 1:
            MainWindow.setMaximumSize(767, 367)
            MainWindow.resize(767, 367)
            self.tabWidget.setGeometry(QtCore.QRect(0, 0, 767, 367))
            self.db_combo.setGeometry(QtCore.QRect(70, 10, 391, 28))
            self.search.setGeometry(QtCore.QRect(500, 11, 201, 28))
            self.tableWidget.setGeometry(QtCore.QRect(20, 60, 701, 261))
            list = main.get_word_list()
            temp = []
            for x in list:
                if x not in temp: temp.append(x)
            self.db_combo.clear()
            for row in temp:
                self.db_combo.addItem(row[0])
        else:
            MainWindow.resize(567, 167)
            MainWindow.setMinimumSize(567, 167)
            MainWindow.setMaximumSize(567, 167)

    def search_clicked(self):
        list_d = main.get_translation(self.db_combo.currentText())
        numRows = len(list_d)
        numColumns = 2
        self.tableWidget.setRowCount(numRows)
        self.tableWidget.setColumnCount(numColumns)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setHorizontalHeaderLabels(['Язык', 'Перевод'])
        for r in range(numRows):
            list_d[r] = list(list_d[r])
            list_d[r][0] = next(ch for ch, code in self.data.items() if code == list_d[r][0])
            for c in range(numColumns):
                    self.tableWidget.setItem(r, c, QTableWidgetItem(list_d[r][c]))
        self.tableWidget.resizeRowsToContents()


    def origin_lan_activated(self, index):
        self.origin.clear()
        self.dest.clear()
        if self.origin_lan.itemData(index) == self.dest_lan.currentData():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Выберите разные языки')
            msg.setWindowTitle("Error")
            msg.exec_()

    def dest_lan_activated(self, index):
        self.origin.clear()
        self.dest.clear()
        if self.origin_lan.currentData() == self.dest_lan.itemData(index):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Выберите разные языки')
            msg.setWindowTitle("Error")
            msg.exec_()

    def switch_lan_clicked(self):
        tmp = self.origin_lan.currentText()
        self.origin_lan.setCurrentText(self.dest_lan.currentText())
        self.dest_lan.setCurrentText(tmp)
        tmp_text = self.origin.text()
        self.origin.setText(self.dest.text())
        self.dest.setText(tmp_text)

    def translate_clicked(self):
        if self.origin_lan.currentData() == self.dest_lan.currentData():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Выберите разные языки')
            msg.setWindowTitle("Error")
            msg.exec_()

        else:
            if self.origin.text():
                origin = self.origin_lan.currentData()
                dest = self.dest_lan.currentData()
                text = self.origin.text().lower().strip()
                self.dest.setText(main.translate_action(text,
                                                        origin,
                                                        dest
                                                        ))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Словарь"))
        self.switch_lan.setText(_translate("MainWindow", "<---->"))
        self.translate.setText(_translate("MainWindow", "Перевести"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Перевод"))
        self.search.setText(_translate("MainWindow", "Поиск"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Словарь"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
