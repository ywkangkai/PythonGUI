from PyQt5.Qt import *
import sys









app = QApplication(sys.argv)
window = QWidget()
window.resize(500 ,500)



lable = QLabel(window)
lable.setText("标签")
lable.resize(300, 300)
lable.setStyleSheet("background-color: yellow")
lable.setCursor(Qt.ForbiddenCursor)  #鼠标移动到控件中后，鼠标会改变样式



window.show()
sys.exit(app.exec())