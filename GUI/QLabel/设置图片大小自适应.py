from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.move(100, 100)
        label.resize(150,150)
        label.setPixmap(QPixmap('D:\PythonGUI\qi.png'))
        label.setScaledContents(True)  #图片会根据窗口大小适应


app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
