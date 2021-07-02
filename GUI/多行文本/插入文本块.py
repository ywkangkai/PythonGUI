from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)

btn = QPushButton(window)
btn.move(300, 300)
btn.setText('按钮')

text = QTextEdit(window)
text.setText('xxx')


def cao():
    tc = text.textCursor()  # 此方法可以获取文本焦点，选择插入的位置
    #tc.insertBlock()  # 直接插入文本块
    tif = QTextBlockFormat()  # 文本块对象，如果要设置格式选择此
    tif.setRightMargin(100)  # 右侧间距
    tc.insertBlock(tif)
    print(tc.block().text())


def cao2():
    tc = text.textCursor()
    print(tc.block().text())  # 获取文本块内容


#btn.pressed.connect(cao)
btn.pressed.connect(cao2)

window.show()
sys.exit(app.exec_())
