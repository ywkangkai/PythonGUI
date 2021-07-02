from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)

text = QTextEdit(window)
text.setPlaceholderText("请输入个人简介")

window.show()
sys.exit(app.exec_())
