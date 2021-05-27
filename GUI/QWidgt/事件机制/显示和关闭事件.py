from PyQt5.Qt import *
import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('事件消息')


    def showEvent(self, QShowEvent):
        print("窗口显示")

    def closeEvent(self, QCloseEvent):
        print("窗口关闭")

    def moveEvent(self, QMoveEvent):
        print('窗口移动了')

    def resizeEvent(self, QMoveEvent):
        print('窗口大小已改变')


app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec())