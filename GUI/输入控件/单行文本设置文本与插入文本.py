from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
line = QLineEdit(window)
line.setText('xxx')
#line.insert('yyyy')  在光标处插入文本
btn = QPushButton('按钮',window)
btn.move(50 ,50)

def cao():
    line.insert('yyy')
btn.pressed.connect(cao)

window.show()
sys.exit(app.exec_())
