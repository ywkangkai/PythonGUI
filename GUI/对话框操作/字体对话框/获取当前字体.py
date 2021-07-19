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
        def font_sel():
            print('获取当前字体',fb.selectedFont().family())

        btn.clicked.connect(lambda: fb.open(font_sel))

app = QApplication(sys.argv)
window = Window()









window.show()
sys.exit(app.exec_())
