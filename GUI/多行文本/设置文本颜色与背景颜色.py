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
    text.setTextBackgroundColor(QColor(200,10,10))
    text.setTextColor(QColor(10,200,10))




btn.pressed.connect(cao)


window.show()
sys.exit(app.exec_())
