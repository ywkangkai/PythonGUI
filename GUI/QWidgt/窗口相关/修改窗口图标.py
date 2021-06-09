
from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
icon = QIcon(r'D:\PythonGUI\GUI\QWidgt\改变鼠标形状\xxx.png')
window.setWindowIcon(icon)

window.show()
sys.exit(app.exec())