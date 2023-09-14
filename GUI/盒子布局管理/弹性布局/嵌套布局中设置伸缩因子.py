from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):

        # 平均分配
        label1 = QLabel('x1', self)
        label1.setStyleSheet('background-color:cyan')
        label2 = QLabel('x1', self)
        label2.setStyleSheet('background-color:yellow')
        label3 = QLabel('x1', self)
        label3.setStyleSheet('background-color:red')
        v_layout = QBoxLayout(QBoxLayout.LeftToRight)
        v_layout.addWidget(label1)
        v_layout.addWidget(label2)
        v_layout.addWidget(label3)

        self.setLayout(v_layout)

        label4 = QLabel('x1', self)
        label4.setStyleSheet('background-color:cyan')
        label5 = QLabel('x1', self)
        label5.setStyleSheet('background-color:yellow')
        label6 = QLabel('x1', self)
        label6.setStyleSheet('background-color:red')
        h_layout = QBoxLayout(QBoxLayout.TopToBottom)
        h_layout.addWidget(label4)
        h_layout.addWidget(label5, 1) # 1表示伸缩因子占一份的比例
        h_layout.addWidget(label6)
        v_layout.addLayout(h_layout, 1) # 1表示伸缩因子占一份的比例













app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
