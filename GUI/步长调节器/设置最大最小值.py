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
        self.最大值最小值()


    def 最大值最小值(self):
        # self.sb.setMaximum(180) # 设置最大值
        # print(self.sb.maximum()) # 获取最大值
        #
        # self.sb.setMinimum(18)
        # print(self.sb.minimum()) # 获取最小值
        self.sb.setRange(18, 180) # 设置最大值和最小值

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())