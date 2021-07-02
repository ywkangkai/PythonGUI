from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
line = QLineEdit(window)
line.setInputMask(">AA-99")   # 一个A表示一个大写字母，一个9表示一个数字，

window.show()
sys.exit(app.exec_())
