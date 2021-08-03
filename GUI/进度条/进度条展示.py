from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        pb = QProgressBar(self)
        pb.resize(300,10)
        pb.setRange(0,100)
        pb.setValue(75)

app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
