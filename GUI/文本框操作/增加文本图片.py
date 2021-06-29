from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
line = QLineEdit(window)
line.setEchoMode(QLineEdit.Password)

line.setPlaceholderText('请输入密码')
line.setClearButtonEnabled(True)
action =QAction(line)
action.setIcon(QIcon(r'D:\PythonGUI\open.png'))
line.addAction(action, QLineEdit.TrailingPosition)

window.show()
sys.exit(app.exec_())
#