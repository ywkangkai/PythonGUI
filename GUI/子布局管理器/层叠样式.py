from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        #1.首先创建一个布局管理器对象
        s1 = QStackedLayout()


        #2.把布局对象设置给需要布局的父控件 父布局
        self.setLayout(s1)

        #3. 通过不对象，管理布局一些子控件
        label1 = QLabel('x1', self)
        label1.setStyleSheet('background-color:cyan')
        label2 = QLabel('x2', self)
        label2.setStyleSheet('background-color:yellow')
        label3 = QLabel('x3', self)
        label3.setStyleSheet('background-color:red')


        #层叠样式，当前只会显示标签1
        s1.addWidget(label1)
        s1.addWidget(label2)
        s1.addWidget(label3)


        #可通过索引改变要显示的控件
        s1.setCurrentIndex(1)

app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
