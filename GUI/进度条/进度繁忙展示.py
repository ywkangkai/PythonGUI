from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        pb = QProgressBar(self)

        pb.setRange(0,0) #设置范围为0-0，表示进度条繁忙


app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
