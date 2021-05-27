from PyQt5.Qt import *
import sys

class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.QObject()

    def setup_ui(self):
        pass

    def destroy_cao(self):
        print("释放对象")

    def QObject(self):
        self.obj = QObject()
        self.obj.destroyed.connect(self.destroy_cao)

        del self.obj


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())