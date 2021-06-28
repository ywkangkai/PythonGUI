#要求：用户名输入sz，密码输入123时登录成功

from PyQt5.Qt import *
import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup()

    def setup(self):
        self.account_line = QLineEdit(self)
        self.password_line = QLineEdit(self)
        self.btn = QPushButton('登录',self)
        self.account_line.move(100,0)
        self.password_line.move(100,100)
        self.password_line.setEchoMode(QLineEdit.Password)
        self.btn.move(100,300)

        self.btn.clicked.connect(self.cao)

    def cao(self):
        account = self.account_line.text()
        pwd = self.password_line.text()
        if account == 'sz':
            if pwd == '123':
                print('登录成功')
            else:
                print('用户名或密码错误')
                self.password_line.setText("")
                self.password_line.setFocus()  #当密码输入失败后，会将焦点定位到密码输入框，不设置的话需要手动将鼠标在密码框中点击才能输入
        else:
            print('用户名或密码错误')
            self.account_line.setText("")
            self.password_line.setText("")
            self.account_line.setFocus()

app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
