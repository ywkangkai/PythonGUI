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

        timer = QTimer(self)
        timer.timeout.connect(lambda :label1.setText(label1.text()+'kkkk\n'))
        timer.start(1000)

        label4 = QLabel('x4', self)
        label4.setStyleSheet('background-color:black')
        v_layout = QHBoxLayout()  #水平布局对象
        v_layout.addWidget(label1)
        v_layout.addWidget(label2)
        v_layout.addWidget(label3)
        v_layout.replaceWidget(label2, label4)

        label2.destroyed.connect(lambda :print('标签2倍释放'))
        label2.setParent(None)  #如果想让标签2被释放就直接设置父控件为None
        self.setLayout(v_layout)





app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
