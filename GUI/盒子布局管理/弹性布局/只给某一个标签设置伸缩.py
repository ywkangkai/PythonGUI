from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
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

        v_layout.addWidget(label2)

        v_layout.addWidget(label3)

        v_layout.setStretchFactor(label2, 1) # 拖动窗口时，只有label2会变大/变小，其他的不会变化
        self.setLayout(v_layout)
        ###########









app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
