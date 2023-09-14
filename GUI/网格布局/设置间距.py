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
        v_layout.addWidget(label3, 1, 0, 1, 2) # 1,0表示行列索引，1,2表示占用的行列数 (位置在第二行第一列，占用一行两列)
        self.setLayout(v_layout)
        v_layout.setVerticalSpacing(60) # 设置行间距为0
        v_layout.setHorizontalSpacing(60) # 设置列间距为0









app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
