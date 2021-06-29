from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
line = QLineEdit(window)

def cao():
    print(123)

def cao1():
    print(1)

line.textEdited.connect(cao)
line.textChanged.connect(cao1)

window.show()
sys.exit(app.exec_())
