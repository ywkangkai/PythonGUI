from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
line = QLineEdit(window)

completer = QCompleter(["sz","shuinzi",'wangzha'],line)
line.setCompleter(completer)

window.show()
sys.exit(app.exec_())
