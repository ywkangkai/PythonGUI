# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys

class Window(QWidget):
    def mousePressEvent(self, QMouseEvent):

        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = Window()
# 2.2 设置控件
window.resize(500, 500)
window.setWindowTitle("w1")

window.show()

sys.exit(app.exec_())