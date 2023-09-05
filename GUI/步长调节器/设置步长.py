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
        self.步长设置()

    def 步长设置(self):
        self.sb.setSingleStep(3)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())