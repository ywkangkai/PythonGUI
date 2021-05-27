from PyQt5.Qt import *
import sys

class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.QObject()

    def setup_ui(self):
        pass

    # def change_name(self, name):
    #     print("对象名字被改变%s" %name)

    def QObject(self):
        self.obj = QObject()

        def change_name(name):
            print("对象名字被改变%s" % name)
        self.obj.objectNameChanged.connect(change_name)

        self.obj.setObjectName('xxx')

        self.obj.objectNameChanged.disconnect()

        self.obj.setObjectName('ooo')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())