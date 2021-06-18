from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)

tb =  QToolButton(window)
tb.setText('工具')   # 当贡酒既设置了文本又设置了图片，不会显示文本
tb.setIcon(QIcon(r'D:\PythonGUI\GUI\QWidgt\改变鼠标形状\xxx.png'))
tb.setIconSize(QSize(60,60))   # 设置图片大小
tb.setToolTip('这是一个工具按钮')  # 对图片做说明，鼠标移动到该图片上会显示这句话





window.show()
sys.exit(app.exec()) 