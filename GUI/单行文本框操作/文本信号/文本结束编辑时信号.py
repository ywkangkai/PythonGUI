from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
line = QLineEdit(window)
line2 = QLineEdit(window)
line2.move(100 , 100)
def cap():
    print('编辑结束')

line.editingFinished.connect(cap)


window.show()
sys.exit(app.exec_())
