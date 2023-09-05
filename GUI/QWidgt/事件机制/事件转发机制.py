from PyQt5.Qt import *
import sys

class Window(QWidget):

    def mousePressEvent(self, QMouseEvent):
        print('顶层控件被按下')

class MidWindow(QWidget):

    def mousePressEvent(self, QMouseEvent):
        print('中间控件被按下')

class Lable(QLabel):

    def mousePressEvent(self, QMouseEvent):
        print('标签控件被按下')

app = QApplication(sys.argv)
window = Window()
window.resize(500,500)
minwindow = MidWindow(window)
minwindow.resize(300, 300)
minwindow.setAttribute(Qt.WA_StyledBackground, True)
minwindow.setStyleSheet("background-color: yellow")
lable = Lable(minwindow)
lable.setText("标签")


window.show()
sys.exit(app.exec())