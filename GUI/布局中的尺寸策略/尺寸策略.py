from PyQt5.Qt import *
import sys

class Lable(QLabel):
    def sizeHint(self): # sizeHint建议的尺寸大小
        return QSize(150, 60)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 200)
        self.setup_ui()

    def setup_ui(self):
        # 标签1使用自定义的，标签2和标签3使用默认的，注意看尺寸
        label1 = Lable('x1')
        label1.setStyleSheet('background-color:cyan')
        label2 = QLabel('x2')
        label2.setStyleSheet('background-color:yellow')
        label3 = QLabel('x3')
        label3.setStyleSheet('background-color:red')

        v_layout = QVBoxLayout()
        self.setLayout(v_layout)
        v_layout.addWidget(label1)
        v_layout.addWidget(label2)
        v_layout.addWidget(label3)

        # label1不会随着窗口大小变化而变化
        # label1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed) # QSizePolicy.Fixed第一个表示水平方向控制，第二个表示垂直方向控制，不会随着窗口变化而改变大小
        # label1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum) # QSizePolicy.Minimum，会参考Lable最小设置的值，可以变大，但最小不会小于设置的值
        label1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred) # QSizePolicy.Preferred可以伸展也可以收缩，垂直方向最小可以收缩到60
        label2.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding) # 可以获取额外的空间







app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
