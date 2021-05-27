from PyQt5.Qt import *
import sys

class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.QObject()

    def setup_ui(self):
        pass

    def change_name(self, name):
        print("窗口名字被改变", name)
        self.windowTitleChanged.disconnect()
        self.setWindowTitle('PYthon'+ name)
        self.windowTitleChanged.connect(self.change_name)

    def QObject(self):
        self.windowTitleChanged.connect(self.change_name)
        self.setWindowTitle('xxx')
        self.setWindowTitle('ooo')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())