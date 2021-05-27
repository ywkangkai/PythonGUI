from PyQt5.Qt import *
import sys

class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.QObject()

    def QObject(self):
        self.obj = QObject()
        self.setWindowTitle('xxx')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())