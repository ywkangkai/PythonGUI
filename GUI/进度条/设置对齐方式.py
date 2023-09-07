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
        pb.resize(300,40)
        pb.setRange(0,100)
        pb.setValue(75)
        pb.setFormat(f'当前人数{pb.value()-20}/总人数m')

        def test():
            pb.setAlignment(Qt.AlignCenter)
        btn.clicked.connect(test)




app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
