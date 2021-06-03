##要求：用户可以通过拖拽控件中任意地方实现改变控件位置


from PyQt5.Qt import *
import sys


class window(QWidget):
    def __init__(self):
        super().__init__()
        self.move_flage = False


    def mousePressEvent(self, QMouseEvent) :
        '''
        确定鼠标第一次按下的点
        确定窗口当前所在的原始点
        '''

        #确定控件相对于当前窗口的原始点
        if QMouseEvent.button() == Qt.LeftButton:
            self.move_flage = True
            self.mouse_x = QMouseEvent.globalX()
            self.mouse_y = QMouseEvent.globalY()

            #确定鼠标第一次按下的点
            self.origin_x = self.x()
            self.origin_y = self.y()

    def mouseMoveEvent(self, QMouseEvent):
        if self.move_flage:
            #计算移动向量
            move_x = QMouseEvent.globalX() - self.mouse_x
            move_y = QMouseEvent.globalY() - self.mouse_y

            #最后的目标位置
            dest_x = self.origin_x + move_x
            dest_y = self.origin_y + move_y
            self.move(dest_x, dest_y)


    def mouseReleaseEvent(self, QMouseEvent) :
        #释放鼠标按键
        self.move_flage = False


app = QApplication(sys.argv)
window = window()
window.resize(500, 500)
window.setMouseTracking(True)
window.show()
sys.exit(app.exec())


