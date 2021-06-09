
from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
window.setWindowTitle('kkk[*]')   #此处的[*]是固定写法，当为编辑状态时，会显示*，但不会把[*]都显示出来
window.setWindowModified(True)  #设置为True表示当前为编辑状态


window.show()
sys.exit(app.exec())