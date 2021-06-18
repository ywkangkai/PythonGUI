from PyQt5.Qt import *
import sys




app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
btn = QPushButton(QIcon(r'D:\PythonGUI\GUI\QWidgt\改变鼠标形状\xxx.png'), 'xxx', window) #这样写可以一次性设置

def cao():
    print('aaa')

def release():
    print('bbb')

btn.pressed.connect(cao)
btn.released.connect(release)


window.show()
sys.exit(app.exec())