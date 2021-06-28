from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
line = QLineEdit(window)
line.setEchoMode(QLineEdit.Password)

line.setPlaceholderText('请输入密码')
line.setClearButtonEnabled(True)

window.show()
sys.exit(app.exec_())
