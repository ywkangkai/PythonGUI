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
        label2 = QLabel('x1', self)
        label2.setStyleSheet('background-color:yellow')
        label3 = QLabel('x1', self)
        label3.setStyleSheet('background-color:red')

        #1.创建布局对象
        layout =  QBoxLayout(QBoxLayout.TopToBottom) #从左到右LeftToRight  从上到下TopToBottom  从右到左RightToLeft  从下到上BottomToTop

        #2.把布局管理器对象设置给需要布局的父控件
        self.setLayout(layout)

        #3.添加需要布局的子控件布局到管理器对象中
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)


        ###将下面的标签进行嵌套###
        label5 = QLabel('x5', self)
        label5.setStyleSheet('background-color:blue')
        label6 = QLabel('x6', self)
        label6.setStyleSheet('background-color:orange')
        label7 = QLabel('x7', self)
        label7.setStyleSheet('background-color:gray')

        h_layout = QBoxLayout(QBoxLayout.LeftToRight)
        h_layout.addWidget(label5)
        h_layout.addWidget(label6)
        h_layout.addWidget(label7)

        # 将这部分类容加再标签1和标签2之间
        layout.insertLayout(1,h_layout)




app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
