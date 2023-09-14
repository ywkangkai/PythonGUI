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
        label2 = QLabel('x1', self)
        label2.setStyleSheet('background-color:yellow')
        label3 = QLabel('x1', self)
        label3.setStyleSheet('background-color:red')

        v_layout = QGridLayout()
        v_layout.addWidget(label1, 0, 0) # 0,0表示行列索引 （第一行第一个列）
        v_layout.addWidget(label2, 0, 1) # 0,1表示行列索引 （第一行第二列）
        v_layout.addWidget(label3, 1, 0, 1, 2) # 1,0表示行列索引，1,2表示占用的行列数 (第二行第一列，占用了1，2两列， 可以理解为合并了12列单元格)
        self.setLayout(v_layout)
        v_layout.setColumnMinimumWidth(0, 100)  # 设置第0列的最小宽度e为100像素，在拖动窗口变小时，不会小于100
        v_layout.setRowMinimumHeight(0, 100)  # 设置第0行的最小高度为100像素，在拖动窗口变小时，不会小于100







app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
