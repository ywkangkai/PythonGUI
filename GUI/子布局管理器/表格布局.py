from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label1 = QLabel('x1',self)
        label1.setStyleSheet('background-color:cyan')
        label2 = QLabel('x2', self)
        label2.setStyleSheet('background-color:yellow')
        label3 = QLabel('x3', self)
        label3.setStyleSheet('background-color:red')
        label4 = QLabel('x4', self)
        label4.setStyleSheet('background-color:pink')

        v_layout = QGridLayout()  #表格布局对象
        v_layout.addWidget(label1, 0, 0)  # 表示显示在第一行的第一列
        v_layout.addWidget(label2, 0, 1)  #表示显示在第一行的第二列
        v_layout.addWidget(label3, 1, 1)  #表示显示在第二行的低二列
        v_layout.addWidget(label4, 2, 0, 2, 2) #表示显在第三行的一列， 并且夸两行两列
        self.setLayout(v_layout)




app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
