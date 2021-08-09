from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label1 = QLabel('x1', self)
        label1.setStyleSheet('background-color:cyan')
        label2 = QLabel('x2', self)
        label2.setStyleSheet('background-color:yellow')
        label3 = QLabel('x3', self)
        label3.setStyleSheet('background-color:red')

        #1.创建布局对象
        layout =  QBoxLayout(QBoxLayout.LeftToRight) #从左到右LeftToRight  从上到下TopToBottom

        #2.把布局管理器对象设置给需要布局的父控件
        self.setLayout(layout)

        #3.添加需要布局的子控件布局到管理器对象中
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)

        layout.removeWidget(label1)
        label1.setParent(None)





app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
