#要求：窗口去掉原始标题栏，自己添加最大化，最小化，关闭按钮，点击任意按钮能触发相应事件,并且可通过拖拽改变位置

from PyQt5.Qt import *
import sys

# top_margin = 10
# btn_w = 80
# btn_h = 40
# app = QApplication(sys.argv)
# window = QWidget()
# window.resize(500, 500)
# window.setWindowOpacity(0.9)
# window.setWindowFlag(Qt.FramelessWindowHint)
# window_w = window.width()
#
# close_btn = QPushButton(window)
# close_btn.setText("关闭")
# close_w = window_w - btn_w
# close_btn.move(close_w, top_margin)
#
# max_btn = QPushButton(window)
# max_w = close_w - btn_w
# max_btn.setText("最大化")
# max_btn.move(max_w, top_margin)
#
# mini_btn = QPushButton(window)
# mini_w = max_w - btn_w
# mini_btn.setText("最小化")
# mini_btn.move(mini_w, top_margin)
#
# '''
# 注意：事件机制与信号槽不一样，事件机制最大化或者最小化或者关闭使用window.setWindowState(Qt.WindowMaximized)
# 信号与槽使用showMaximized，在开发中常使用信号与槽
# '''
#
# close_btn.pressed.connect(window.close)
#
# def max_normal():
#     if window.isMaximized():
#         window.showNormal()
#         max_btn.setText("最大化")
#     else:
#         window.showMaximized()
#         max_btn.setText('恢复')
# max_btn.pressed.connect(max_normal)
#
# mini_btn.pressed.connect(window.showMinimized)
#
# window.show()
# sys.exit(app.exec())




###############上方代码实现封装#################

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowOpacity(0.9)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setup()
        self.move_flage = False

    def setup(self):
        self.top_margin = 10
        self.btn_w = 80
        window_w = self.width()

        close_btn = QPushButton(self)
        self.close_btn = close_btn
        close_btn.setText("关闭")
        close_w = window_w - self.btn_w
        close_btn.move(close_w, self.top_margin)

        max_btn = QPushButton(self)
        self.max_btn = max_btn
        max_w = close_w - self.btn_w
        max_btn.setText("最大化")
        max_btn.move(max_w, self.top_margin)

        mini_btn = QPushButton(self)
        self.mini_btn = mini_btn
        mini_w = max_w - self.btn_w
        mini_btn.setText("最小化")
        mini_btn.move(mini_w, self.top_margin)

        close_btn.pressed.connect(self.close)

        def max_normal():
            if self.isMaximized():
                self.showNormal()
                max_btn.setText("最大化")
            else:
                self.showMaximized()
                max_btn.setText('恢复')
        max_btn.pressed.connect(max_normal)

        mini_btn.pressed.connect(self.showMinimized)


    #窗口尺寸监听，窗口尺寸改变大小时触发
    def resizeEvent(self, QResizeEvent):

        window_w = self.width()
        close_w = window_w - self.btn_w
        self.close_btn.move(close_w, self.top_margin)

        max_w = close_w - self.btn_w
        self.max_btn.move(max_w, self.top_margin)

        mini_w = max_w - self.btn_w

        self.mini_btn.move(mini_w, self.top_margin)

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



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())