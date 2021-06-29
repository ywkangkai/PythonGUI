# 要求：一个文本框只能输入18到180之间的数字，如果不符合不会显示，当从该文本框移动出另外一个文本框时，如果不符合要求会默认给他一个返回值1

from PyQt5.Qt import *
import sys




app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
line = QLineEdit(window)
def cao():
    print(123)
line.textChanged.connect(cao)

window.show()
sys.exit(app.exec_())
