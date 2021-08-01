from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.setText('<h1>xxxxx</h1>')
        #label.setStyleSheet('background-color:yellow')
        label.move(100, 100)
        label.resize(150,150)
        label.adjustSize()
        label.setTextFormat(Qt.RichText)   #能够读取html的语法   Qt.PlanText只能读取出纯文本
        label.setTextInteractionFlags(Qt.TextSelectableByMouse)  #这句话是可以对标签进行选中


app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
