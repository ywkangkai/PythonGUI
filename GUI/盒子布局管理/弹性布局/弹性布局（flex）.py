from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        ###########
        #
        # label1 = QLabel('x1',self)
        # label1.setStyleSheet('background-color:cyan')
        # label2 = QLabel('x1', self)
        # label2.setStyleSheet('background-color:yellow')
        # label3 = QLabel('x1', self)
        # label3.setStyleSheet('background-color:red')
        # v_layout = QBoxLayout(QBoxLayout.LeftToRight)  #垂直布局对象
        # v_layout.addWidget(label1, 1) # 1表示伸缩因子占一份的比例
        # v_layout.addStretch(2) # 表示伸缩因子占两份的比例，空白占比是上面的2倍
        # v_layout.addWidget(label2, 2) # 2表示伸缩因子占两份的比例
        # v_layout.addWidget(label3, 3) # 3表示伸缩因子占三份的比例
        # self.setLayout(v_layout)
        ###########



        ###########
        # 平均分配
        label1 = QLabel('x1', self)
        label1.setStyleSheet('background-color:cyan')
        label2 = QLabel('x1', self)
        label2.setStyleSheet('background-color:yellow')
        label3 = QLabel('x1', self)
        label3.setStyleSheet('background-color:red')
        v_layout = QBoxLayout(QBoxLayout.LeftToRight)
        v_layout.addWidget(label1)
        v_layout.addStretch()
        v_layout.addWidget(label2)
        v_layout.addStretch()
        v_layout.addWidget(label3)
        self.setLayout(v_layout)
        ###########









app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
