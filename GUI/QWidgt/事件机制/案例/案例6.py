
#要求：10个标签，随机点击一个标签将他背景色改为红色

from PyQt5.Qt import *
import sys

class Window(QWidget):

    def mousePressEvent(self, QMouseEvent):
        x = QMouseEvent.x()
        y = QMouseEvent.y()
        children = self.childAt(x, y)  #childAt表示获取QWidget控件中其他子控件的相对位置
        if children is not None: #这个判断是为了判定如果点击了标签之外的空白部分，就会得到None，不做这个判断点击标签之外的部分程序会崩溃
            children.setStyleSheet("background-color: red")


app = QApplication(sys.argv)
window = Window()
for i in range(1, 11):
    lable = QLabel(window)
    lable.move(i*40, i*40)
    lable.setText("标签" + str(i))

window.show()
sys.exit(app.exec())