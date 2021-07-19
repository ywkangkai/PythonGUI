from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        cd = QColorDialog(QColor(100, 200, 150), self)
        cd.setWindowTitle('选择背景颜色')
        def color(col):
            palette = QPalette()
            palette.setColor(QPalette.Background, col)
            self.setPalette(palette)
        cd.colorSelected.connect(color)
        cd.show()


app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
