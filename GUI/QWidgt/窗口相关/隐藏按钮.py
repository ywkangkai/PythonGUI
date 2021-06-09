
from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
btn = QPushButton(window)
btn.setText('按钮')
btn.setVisible(False)  #隐藏   isHdden()可判断是否是隐藏的状态
#btn.setVisible(True)  可见    isVisible() 可判断是否是可见的状态
window.show()
sys.exit(app.exec())