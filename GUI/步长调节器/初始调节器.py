from PyQt5.Qt import *
import sys


'''
文本编辑器没有click，press槽与信号的点击事件
所以需要重写内置的点击事件
'''


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        asb = QAbstractSpinBox(self)
        asb.move(100,100)
        asb.resize(100,30)


app = QApplication(sys.argv)
window = Window()









window.show()
sys.exit(app.exec_())
