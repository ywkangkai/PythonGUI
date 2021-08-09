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

        timer = QTimer(self)
        timer.timeout.connect(lambda :label1.setText(label1.text()+'kkkk\n'))
        timer.start(1000)

        v_layout = QHBoxLayout()  #水平布局对象
        v_layout.addWidget(label1)
        v_layout.addWidget(label2)
        v_layout.addWidget(label3)
        self.setLayout(v_layout)
        v_layout.setSpacing(60)  #设置间距




app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
