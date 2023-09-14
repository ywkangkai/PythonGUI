from PyQt5.Qt import *
import sys

class Lable(QLabel):
    def minimumSizeHint(self):
        return QSize(200, 200)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 标签1使用自定义的，标签2和标签3使用默认的，注意看尺寸
        label1 = Lable('x1')
        label1.setStyleSheet('background-color:cyan')
        label2 = QLabel('x1')
        label2.setStyleSheet('background-color:yellow')
        label3 = QLabel('x1')
        label3.setStyleSheet('background-color:red')

        v_layout = QVBoxLayout()
        self.setLayout(v_layout)
        v_layout.addWidget(label1)
        v_layout.addWidget(label2)
        v_layout.addWidget(label3)







app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
