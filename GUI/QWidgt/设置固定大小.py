from PyQt5.Qt import *
import sys




app = QApplication(sys.argv)
window = QWidget()
lable = QLabel(window)
lable.move(100,100)
lable.setText('xxx')
window.setFixedSize(500, 500) #此属性设置后，窗口无法最大化和最小化，也无拖动窗口变大变小





window.show()
sys.exit(app.exec())