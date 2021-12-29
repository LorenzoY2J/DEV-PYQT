import searching_ui
import sys, os, re, time, subprocess
<<<<<<< HEAD
from PySide2 import QtWidgets, QtGui, QtCore
=======
from PyQt5 import QtWidgets, QtGui, QtCore
>>>>>>> origin/master


class SearchingFile(QtWidgets.QWidget, searching_ui.Ui_Form):
    def __init__(self, parent=None):
        super(SearchingFile, self).__init__(parent)

        self.t = AllThread()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.startThread)
        self.pushButton_2.clicked.connect(self.onPushButtonOpenClicked)

        self.t.started.connect(lambda: print("Поток запущен"))
        self.t.finished.connect(lambda: print("Поток завершен"))
<<<<<<< HEAD
        self.t.mysignal.connect(lambda text: self.plainTextEdit.appendPlainText(text))


    # def plainTextEdit(self, text):
    #     self.t.plainTextEdit.appendPlainText(text)
=======
        self.t.current_count.connect(self.addTextPlainText, QtCore.Qt.QueuedConnection)
>>>>>>> origin/master

    def startThread(self):
        if self.lineEdit.text() is None:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Не введено содержимое файла')
            return
        elif self.lineEdit_2.text() is None:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Не введена директория для поиска')
            return

<<<<<<< HEAD
        self.t.set_folder_path(self.lineEdit_2.text())
=======
>>>>>>> origin/master
        self.t.start()

    def stopThread(self):
        self.t.status = False

    def onPushButtonOpenClicked(self):
        self.FilePath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выбор файла', '.')
        self.lineEdit_2.setText(self.FilePath)

<<<<<<< HEAD

class AllThread(QtCore.QThread):
    mysignal = QtCore.Signal(str)

    def set_folder_path(self, folder_path):
        self.folder_path = folder_path

    def run(self) -> None:
        files = os.listdir(self.folder_path)
        for file in files:
            self.mysignal.emit(file)
=======
    def addTextPlainText(self):
        text = self.lineEdit.text()
        files = os.listdir(self.FilePath)
        for file in files:
            print(file)
            with open(f'{self.FilePath}/{file}') as f:
                if text in f.read():
                    self.plainTextEdit.appendPlainText(file)


class AllThread(QtCore.QThread):
    current_count = QtCore.pyqtSignal(str)

    def run(self) -> None:
        self.status = True
        count = 1
        while self.status:
            count -= 1
            self.current_count.emit('')
            time.sleep(1)
            if count == 0:
                break
>>>>>>> origin/master


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_form = SearchingFile()
    my_form.show()
<<<<<<< HEAD
    sys.exit(app.exec_())
=======
    sys.exit(app.exec_())
>>>>>>> origin/master
