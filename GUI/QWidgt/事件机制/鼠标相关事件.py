from PyQt5.Qt import *
import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('事件消息')


    def enterEvent(self, QShowEvent):
        print("鼠标进来了") #当鼠标移动到窗口中触发
        self.setStyleSheet("background-color: yellow;")

    def leaveEvent(self, QShowEvent):
        print("鼠标移动出来了")  # 当鼠标移动出窗口中触发
        self.setStyleSheet("background-color: green;")

    def mousePressEvent(self, QMouseEvent) -> None:
        print('鼠标按下了')

    def mouseReleaseEvent(self, QMouseEvent) -> None:
        print('鼠标释放了')

    def mouseDoubleClickEvent(self, QMouseEvent) -> None:
        print('鼠标双击')

    def mouseMoveEvent(self, QMouseEvent):
        print('鼠标移动了')



app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec())