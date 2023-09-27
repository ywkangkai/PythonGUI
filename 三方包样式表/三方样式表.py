from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label1 = QLabel('x1')
        label1.setStyleSheet('background-color:cyan')
        label2 = QLabel('x2')
        label2.setStyleSheet('background-color:yellow')
        label3 = QLabel('x3')
        label3.setStyleSheet('background-color:red')

        # 创建布局对象
        s1 = QVBoxLayout()

        self.setLayout(s1)
        # 通过布局对象，把需要布局的控件添加到布局中
        s1.addWidget(label1)
        s1.addWidget(label2)
        s1.addWidget(label3)



app = QApplication(sys.argv)
window = Window()
import qdarkgraystyle
app.setStyleSheet(qdarkgraystyle.load_stylesheet_pyqt5())
print(qdarkgraystyle.load_stylesheet_pyqt5())
window.show()
sys.exit(app.exec_())
