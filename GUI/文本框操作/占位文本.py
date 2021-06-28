from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
line = QLineEdit(window)
line.setPlaceholderText('请输入')
window.show()
sys.exit(app.exec_())
