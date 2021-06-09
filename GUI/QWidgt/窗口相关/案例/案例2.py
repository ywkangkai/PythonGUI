# 要求：有3个控件分别为标签，文本框，登录按钮，标签默认隐藏，当文本框没有内容的时候，按钮不能点击
# 当文本框输入Sz时，标签显示并将标签内容修改为登录成功，否则内容为登录失败

from PyQt5.Qt import *
import sys


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup()

    def setup(self):
        lable = QLabel(self)
        lable.move(200,200)
        lable.setText('标签')
        lable.setVisible(False)

        text = QLineEdit(self)
        text.move(200, 300)


        btn = QPushButton(self)
        btn.setText('登录')
        btn.move(200, 400)
        btn.setEnabled(False) #设置按钮不可点击


        def checkout_text(text): #text参数是从文本框传入得到
            print('查看文本框是否有内容')  #通过判断文件内容长度来控制按钮是否可点击
            if len(text) > 0:
                btn.setEnabled(True)
            else:
                btn.setEnabled(False)
        #文本内容修改后的信号
        text.textChanged.connect(checkout_text)

        def change_label():
            if text.text() == 'Sz':
                lable.setVisible(True)
                lable.setText('登录成功')
                lable.adjustSize()  #加这一句是为了自适用长度，因为上面lable默认给了一个‘登录’，长度固定死为2个字符了
            else:
                lable.setVisible(True)
                lable.setText('登录失败')
                lable.adjustSize()
        btn.pressed.connect(change_label)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())



