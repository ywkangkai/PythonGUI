from PyQt5.Qt import *
import sys


'''
文本编辑器没有click，press槽与信号的点击事件
所以需要重写内置的点击事件
'''
class mytext(QTextEdit):
    def mousePressEvent(self, me):
        print(me.pos())  #  点击文本内容可以获取到位置
        link_url = self.anchorAt(me.pos())   # 此方法只针对超链接，只有超链接才能打印出具体内容，上面只能打印内容的位置
        print(link_url)
        if len(link_url) > 0:
            QDesktopServices.openUrl(QUrl(link_url))  #  此方法可以打开链接
        return super().mousePressEvent(me)   #  重点：此处如果不返回父类的这个方法，在文本框中点击了其他位置光标不会发生改变

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.btn = QPushButton(self)
        self.btn.move(300, 300)
        self.btn.setText('按钮')
        self.setup_ui()

    def setup_ui(self):
        self.text = mytext(self)
        self.text.textCursor()
        self.text.setText('XXXX')
        self.text.textChanged.connect(self.textChange)
        self.btn.pressed.connect(self.cao)

    def cao(self):
        self.text.insertHtml('<a href="www.baidu.com">百度</a>')

    def textChange(self):
        print('文本发生改变')


app = QApplication(sys.argv)
window = Window()









window.show()
sys.exit(app.exec_())
