from PyQt5.Qt import *

class SB(QSpinBox):
    def textFromValue(self, p_int):
        print("xx2", p_int)
        # 1 * 1
        return str(p_int) + "*" + str(p_int)

    def valueFromText(self, p_str):
        print("xxxx", p_str)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSpinBox的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        sb = SB(self)
        self.sb = sb
        sb.resize(100, 25)
        sb.move(100, 100)
        sb.valueChanged[str].connect(lambda val: print(type(val), val)) # [str]表示传递的是字符串类型的参数

        btn = QPushButton(self)
        btn.setText("测试按钮")
        btn.move(150, 150)
        btn.clicked.connect(lambda :sb.lineEdit().setText("30*30"))



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())