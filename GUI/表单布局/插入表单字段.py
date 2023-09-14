from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        name_label = QLabel('姓名')
        age_label = QLabel('年龄')
        sex_label = QLabel('性别')

        name_le = QLineEdit()
        age_le = QSpinBox()
        man_radio = QRadioButton('男')
        flmale_radio = QRadioButton('女')

        h_layout = QBoxLayout(QBoxLayout.LeftToRight)
        h_layout.addWidget(man_radio)
        h_layout.addWidget(flmale_radio)

        btn = QPushButton('提交')

        # 创建布局管理器
        layout = QFormLayout()
        # 把布局管理器赋值给需要布局的父控件
        self.setLayout(layout)
        # 把需要布局的子控件添加到布局管理器中
        layout.addRow(name_label, name_le)
        # layout.addRow(age_label, age_le)
        # layout.addRow(sex_label, h_layout)
        layout.addRow(btn)
        layout.insertRow(1, age_label, age_le)
        layout.insertRow(2, sex_label, h_layout)



app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
