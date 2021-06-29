from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
line = QLineEdit(window)
line.setMaxLength(3)    #设置最大长度

line2 = QLineEdit(window)
line2.move(100,100)
line2.setReadOnly(True)   #只读模式1
line2.setText("无法编辑")
window.show()


sys.exit(app.exec_())
