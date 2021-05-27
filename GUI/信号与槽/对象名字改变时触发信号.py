from PyQt5.Qt import *
import sys

class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.QObject()

    def setup_ui(self):
        pass

    def change_name(self, name):
        print("对象名字被改变", name)

    def QObject(self):
        self.obj = QObject()
        self.obj.objectNameChanged.connect(self.change_name)

        self.obj.setObjectName('xxx')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())