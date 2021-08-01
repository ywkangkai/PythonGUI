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
        #label.setOpenExternalLinks(True)  #设置超链接

        #label.linkHovered.connect(lambda a:print(a))  #鼠标移动到超链接上后会打印地址

        label.linkActivated.connect(lambda a:print(a))  #鼠标点击超链接后打印地址


app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
