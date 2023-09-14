from PyQt5.Qt import *
import sys



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        box1 = QWidget(self)
        box2 = QWidget(self)
        v_layout = QVBoxLayout(self)
        self.setLayout(v_layout)
        v_layout.addWidget(box1)
        v_layout.addWidget(box2)
        box1.setStyleSheet('QPushButton {background-color: cyan;}') # 在box1中的所有QPushButton都会被设置为cyan颜色
        # box2.setStyleSheet('background-color: red;')

        label1 = QLabel('标签1', box1)
        label1.setObjectName('l1')
        label1.move(50,50)
        btn1 = QPushButton('按钮1', box1)
        btn1.move(150, 50)

        label2 = QLabel('标签2', box2)
        label2.move(50, 50)
        btn2 = QPushButton('按钮2', box2)
        btn2.setObjectName('l2')
        btn2.move(150, 50)

        # self.setStyleSheet('QPushButton {background-color: red;}') # 在整个窗口中的所有QPushButton都会被设置为red颜色,相当于body中的设置

app = QApplication(sys.argv)
window = Window()
from QSSTool import QSSTool
# with open('test.qss', 'r') as f:
#     content = f.read()
#     app.setStyleSheet(content)
QSSTool.setQssToObj('test.qss', app)
window.show()
sys.exit(app.exec_())

