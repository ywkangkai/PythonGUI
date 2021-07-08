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
    '''
    设置宽度，当达到100宽度时换行
    '''
    text.setLineWrapMode(QTextEdit.FixedPixelWidth)
    text.setLineWrapColumnOrWidth(100)




btn.pressed.connect(cao)


window.show()
sys.exit(app.exec_())
