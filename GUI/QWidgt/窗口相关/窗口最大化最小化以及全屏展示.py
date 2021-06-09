
from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
#window.setWindowState(Qt.WindowMinimized)  #窗口最小化
window.setWindowState(Qt.WindowMaximized)  #窗口最大化
#window.setWindowState(Qt.WindowFullScreen)  #窗口全屏
window.show()
sys.exit(app.exec())