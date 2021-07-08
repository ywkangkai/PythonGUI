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
    tcf = QTextCharFormat()
    tcf.setFontFamily('宋体')
    tcf.setFontPointSize(10)
    tcf.setFontCapitalization(QFont.Capitalize)
    text.setCurrentCharFormat(tcf)  # 当前光标




btn.pressed.connect(cao)


window.show()
sys.exit(app.exec_())
