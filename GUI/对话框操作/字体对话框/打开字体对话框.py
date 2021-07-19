from PyQt5.Qt import *
import sys





class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        fb = QFontDialog(self)
        btn = QPushButton(self)
        btn.setText('设置字体')
        btn.clicked.connect(lambda : fb.open())

app = QApplication(sys.argv)
window = Window()









window.show()
sys.exit(app.exec_())
