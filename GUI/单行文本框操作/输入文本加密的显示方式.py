from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
line = QLineEdit(window)
#Passwprd:输入时显示*  NoEcho:输入的时候不显示    PasswordEchoOnEdit:编辑时显示明文，结束后显示密文    Normal:普通模式输入时能看见密码
line.setEchoMode(QLineEdit.Password)
window.show()
sys.exit(app.exec_())
