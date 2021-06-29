from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
line = QLineEdit(window)

def cap():
    print('回车键按下')

line.returnPressed.connect(cap)


window.show()
sys.exit(app.exec_())
