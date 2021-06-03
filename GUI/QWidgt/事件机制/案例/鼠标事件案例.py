#要求：当鼠标移动至标签内时设置欢迎光临，移出时显示谢谢惠顾


from PyQt5.Qt import *
import sys


class Mylable(QLabel):
    def enterEvent(self, QEvent):
        self.setText("欢迎光临")

    def leaveEvent(self, QEvent):
        self.setText("谢谢惠顾")


app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
lable = Mylable(window)
lable.resize(200, 200)
lable.setStyleSheet("background-color: yellow")
window.show()
sys.exit(app.exec())


