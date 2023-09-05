from PyQt5.Qt import *



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSpinBox的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        sb = QSpinBox(self)
        self.sb = sb
        sb.resize(100, 25)
        sb.move(100, 100)
        self.前缀和后缀()

    def 前缀和后缀(self):
        # self.sb.setRange(1, 12)
        # self.sb.setSuffix("月") # 设置后缀
        self.sb.setRange(0, 6)
        self.sb.setPrefix("周") # 设置前缀
        self.sb.setSpecialValueText("周日") # 设置最小值特殊值的文本




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())