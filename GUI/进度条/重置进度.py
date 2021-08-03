from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton(self)
        btn.setText('重置进度')
        btn.move(100,100)

        pb = QProgressBar(self)
        pb.setRange(0,100)
        pb.setValue(75)

        def test():
            pb.reset()
        btn.clicked.connect(test)




app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
