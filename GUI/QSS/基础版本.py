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
        box1.setStyleSheet('background-color: cyan;')
        box2.setStyleSheet('background-color: red;')

        label1 = QLabel('标签1', box1)
        label1.move(50,50)
        btn1 = QPushButton('按钮1', box1)
        btn1.move(150, 50)

        label2 = QLabel('标签1', box2)
        label2.move(50, 50)
        btn2 = QPushButton('按钮1', box2)
        btn2.move(150, 50)






app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
