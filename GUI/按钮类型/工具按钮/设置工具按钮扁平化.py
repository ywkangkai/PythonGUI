from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)

tb = QToolButton(window)
tb.setArrowType(Qt.UpArrow)   # DownArrow向下箭头，LeftArrow向左箭头，RightArrow向右箭头
tb.setToolTip('这是一个工具按钮')  # 对图片做说明，鼠标移动到该图片上会显示这句话
tb.setAutoRaise(True)  # 此属性设置后，鼠标移动至该按钮才会显示3D效果





window.show()
sys.exit(app.exec())