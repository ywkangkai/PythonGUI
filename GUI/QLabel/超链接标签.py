from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.setText('<a href=www.baidu.com>百度</a>')
        #label.setStyleSheet('background-color:yellow')
        label.move(100, 100)
        label.resize(150, 150)
        label.adjustSize()
        label.setOpenExternalLinks(True)  #设置超链接


app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
