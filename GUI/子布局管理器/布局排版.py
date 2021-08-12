from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label1 = QLabel('姓名', self)
        #label2 = QLabel('年龄', self)
        label3 = QLabel('性别', self)
        btn = QPushButton('提交', self)
        name_le = QLineEdit()
        age_le = QSpinBox()
        male = QRadioButton('男')
        fmale = QRadioButton('女')
        Hlayout = QHBoxLayout()
        Hlayout.addWidget(male)
        Hlayout.addWidget(fmale)
        layout = QFormLayout()

        self.setLayout(layout)
        layout.setWidget(0, QFormLayout.LabelRole, label1)  #0表示第一行 QFormLayout.LabelRole表示放第一行左边
        layout.setWidget(0, QFormLayout.FieldRole, name_le) #0表示第一行 QFormLayout.FieldRole表示放第一行左边
        layout.setWidget(1, QFormLayout.LabelRole, label3)
        layout.setLayout(1, QFormLayout.FieldRole, Hlayout)  #如果是布局管理器对象，使用setLayout
        layout.addRow(btn)

        def get_sex():
            print('xxx')
            if male.isChecked():
                print(male.text())
            else:
                print(fmale.text())

        def get_info():
            print(name_le.text())
            if male.isChecked():
                print(male.text())
            else:
                print(fmale.text())
        btn.clicked.connect(get_info)







app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
