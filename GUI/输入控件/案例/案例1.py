# 两个输入文本框，一个按钮，在第一个文本框中输入字符串，点击按钮复制到第二个文本框中


from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
line = QLineEdit(window)
line2 = QLineEdit(window)
line2.move(0, 50)
btn = QPushButton('复制',window)
btn.move(0, 100)

def copy_cao():
    content = line.text()
    line2.setText("")
    line2.insert(content)
btn.clicked.connect(copy_cao)        #补充pressed与clicked的区别：前者是按下鼠标后立马触发，后者是按下鼠标在松开的时候触发

window.show()
sys.exit(app.exec_())
