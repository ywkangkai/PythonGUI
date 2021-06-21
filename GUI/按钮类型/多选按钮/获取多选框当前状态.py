from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500 , 500)
check1 = QCheckBox('python',window)
check1.setIcon(QIcon(r'D:\PythonGUI\GUI\QWidgt\改变鼠标形状\xxx.png'))
check1.setTristate(True)   #此按钮的作用是设置按钮的三种状态，1.未被选中，2部分选中（方块），3全部选中（√）
check1.setCheckState(Qt.Checked) #设置按钮被选中的状态：Checked（全部选中），PartiallyCheacked(部分选中)，Unchecked(未被选中)
check1.toggled.connect(lambda isChecked: print(isChecked))  #多选按钮信号一般只用toggled

window.show()
sys.exit(app.exec_())
