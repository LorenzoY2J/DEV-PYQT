from PySide2 import QtWidgets, QtCore
from datetime import datetime
import lesson3
import time
import requests


class MyEventHandler(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.UrlThread = Url()

        self.ui = lesson3.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.countWidgets)
        self.ui.pushButton_2.clicked.connect(self.start_url)
        self.UrlThread.mysignal.connect(self.plainTextEdit, QtCore.Qt.QueuedConnection)

    @QtCore.Slot()
    def countWidgets(self):
        a = self.ui.spinBox.value()

        for i in range(a, -1, -1):
            time.sleep(1)
            self.ui.lineEdit.setText(str(i))
            QtWidgets.QApplication.processEvents()

    @QtCore.Slot()
    def start_url(self):
        self.UrlThread.setparametres(self.ui.lineEdit_2.text(), self.ui.spinBox_2.value())
        self.UrlThread.start()

    def stop_url(self):
        self.t.status = False

    def plainTextEdit(self, text):
        self.ui.plainTextEdit.appendPlainText(str(text))


class Url(QtCore.QThread):
    mysignal = QtCore.Signal(str)

    def run(self):
        while True:
            time.sleep(self.timeout)
            current_datetime = datetime.now()
            r = requests.get(self.url)
            self.mysignal.emit(str(f"{current_datetime} Статус {r.status_code}"))

    def setparametres(self, url, timeout):
        self.url = url
        self.timeout = timeout


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = MyEventHandler()
    window.show()

    app.exec_()
