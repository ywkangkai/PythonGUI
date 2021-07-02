#要求：输入密码时，可对密码进行名为和密文的切换


#要求：用户名输入sz，密码输入123时登录成功

from PyQt5.Qt import *
import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup()

    def setup(self):

        self.password_line = QLineEdit(self)
        self.password_line.setPlaceholderText('输入密码')
        self.password_line.setEchoMode(QLineEdit.Password)
        self.aciton = QAction(self.password_line)
        self.aciton.setIcon(QIcon('D:\PythonGUI\open.png'))
        self.password_line.addAction(self.aciton, QLineEdit.TrailingPosition)
        self.aciton.triggered.connect(self.change_pwd)


    def change_pwd(self):
        if self.password_line.echoMode() == QLineEdit.Password:
            self.password_line.setEchoMode(QLineEdit.Normal)
            self.aciton.setIcon(QIcon('D:\PythonGUI\close.png'))
        else:
            self.password_line.setEchoMode(QLineEdit.Password)
            self.aciton.setIcon(QIcon('D:\PythonGUI\open.png'))



app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
