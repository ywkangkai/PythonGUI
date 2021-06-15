from PyQt5.Qt import *
import sys

class Window(QWidget):

    def mouseMoveEvent(self, QMouseEvent):
        print('局部：鼠标移动', QMouseEvent.localPos()) #鼠标相对于控件中的位置
        print('全局：鼠标移动', QMouseEvent.globalPos())  # 鼠标相对于整个屏幕的位置

app = QApplication(sys.argv)
window = Window()
window.resize(500, 500)
window.setMouseTracking(False) #如果不加这句话或者为False，需要鼠标左键移动至控件内然后一直点住再移动才会触发上面的事件




window.show()
sys.exit(app.exec())