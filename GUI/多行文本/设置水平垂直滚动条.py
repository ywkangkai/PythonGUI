from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)

text = QTextEdit(window)
text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)   # 垂直滚动条
text.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)  # 水平滚动条

window.show()
sys.exit(app.exec_())
