from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label1 = QLabel('姓名', self)
        label2 = QLabel('年龄', self)
        label3 = QLabel('性别', self)
        name_le = QLineEdit()
        age_le = QSpinBox()
        male = QRadioButton('男')
        fmale = QRadioButton('女')
        Hlayout = QHBoxLayout()
        Hlayout.addWidget(male)
        Hlayout.addWidget(fmale)
        #1.创建布局对象
        layout =  QFormLayout()

        #2.把布局管理器对象设置给需要布局的父控件
        self.setLayout(layout)

        #3.添加需要布局的子控件布局到管理器对象中
        layout.addRow(label1, name_le)
        layout.addRow(label2, age_le)
        layout.addRow(label3, Hlayout)







app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
