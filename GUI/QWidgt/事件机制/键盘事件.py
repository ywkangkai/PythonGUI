from PyQt5.Qt import *
import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('事件消息')


    def keyPressEvent(self, QKeyEvent):
        print("键盘上某一个按钮被敲下")

    def keyReleaseEvent(self, a0: QKeyEvent):
        print("键盘上某一个按钮被释放")





app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec())