
from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
window.setWindowOpacity(0.5)   #可以设置窗口透明度，取值范围为0.0-1.0，值越大越透明

window.show()
sys.exit(app.exec())