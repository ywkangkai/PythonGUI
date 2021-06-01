#要求：在空间内有一个标签，鼠标移动进去后标记跟随鼠标位置变化而变化，且鼠标图形要自定义

from PyQt5.Qt import *
import sys

# class Window(QWidget):
#     def mouseMoveEvent(self, QMouseEvent):
#         lable = self.findChild(QLabel)
#         lable.move(QMouseEvent.localPos().x(), QMouseEvent.localPos().y())
#
#
# app = QApplication(sys.argv)
# window = Window()
#
# window.resize(500, 500)
# window.move(300, 300)
# window.setMouseTracking(True)
#
# pixmip = QPixmap("xxx.png").scaled(50, 50)
# cursor = QCursor(pixmip)
# window.setCursor(cursor)
#
# lable = QLabel(window)
# lable.setText("这是一个标签")
# lable.move(200, 200)
#
#
# window.show()
# sys.exit(app.exec())



######################将上面代码进行封装#######################

class Windows2(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.move(300, 300)
        #self.setMouseTracking(True)   把这句话注释后可实现通过拖拽改变鼠标位置
        pixmip = QPixmap("xxx.png").scaled(50, 50)
        cursor = QCursor(pixmip)
        self.setCursor(cursor)
        self.lable = QLabel(self)
        self.lable.setText("这是一个标签")
        self.move(200, 200)

    def mouseMoveEvent(self, QMouseEvent):
        self.lable = self.findChild(QLabel)
        self.lable.move(QMouseEvent.localPos().x(), QMouseEvent.localPos().y())



app = QApplication(sys.argv)
window = Windows2()
window.show()
sys.exit(app.exec())