from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
line = QLineEdit(window)
line.setEchoMode(QLineEdit.Password)

line.setPlaceholderText('请输入密码')
line.setClearButtonEnabled(True)      #.clear()方法也可以清空文本内容，但是需要结合信号与槽函数

window.show()
sys.exit(app.exec_())
