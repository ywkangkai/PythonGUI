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

    text.find('xx')
    text.setFocus()  #  查找成功后获取焦点
    print(text.find('xx'))  # 查找成功返回True



btn.pressed.connect(cao)


window.show()
sys.exit(app.exec_())
