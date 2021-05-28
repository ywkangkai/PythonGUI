from PyQt5.Qt import *
import sys



app = QApplication(sys.argv)
window = QWidget()
window.resize(500 ,500)
window.setCursor(Qt.ForbiddenCursor)  #鼠标移动到控件中后，鼠标会改变样式



window.show()
sys.exit(app.exec())