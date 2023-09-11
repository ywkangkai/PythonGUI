from PyQt5.Qt import *
import sys


# 步骤
# 1.创建布局对象
# 2.把布局管理器对象设置给需要布局的父控件
# 3.添加需要布局的子控件布局到管理器对象中

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
        label4 = QLabel('x4', self)
        label4.setStyleSheet('background-color:green')

        #1.创建布局对象
        layout =  QBoxLayout(QBoxLayout.LeftToRight) #从左到右LeftToRight  从上到下TopToBottom  从右到左RightToLeft  从下到上BottomToTop

        #2.把布局管理器对象设置给需要布局的父控件
        self.setLayout(layout)

        #3.添加需要布局的子控件布局到管理器对象中
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)

        layout.replaceWidget(label2,label4)  #替换控件
        label2.hide()  #隐藏控件






app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
