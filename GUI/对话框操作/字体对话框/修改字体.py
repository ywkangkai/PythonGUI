from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton(self)
        btn.setText('设置字体')


        label = QLabel(self)
        label.move(100,100)
        label.setText('萨达是否')

        def cfc():
            result = QFontDialog.getFont(self)     # result得到的是一个元祖，第一个元素是选择的字体样式font，第二个元素是下方的ok和cnale，ok为True
            if result[1]:
                label.setFont(result[0])
                label.adjustSize()
        btn.clicked.connect(cfc)

app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
