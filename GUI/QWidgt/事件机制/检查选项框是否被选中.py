from PyQt5.Qt import *
import sys



app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)

checkBox = QCheckBox(window)
checkBox.setText("多选框")
radio = QRadioButton(window)
radio.setText('单选框')
radio.move(0,100)
checkBox.setChecked(True)  #可以手动设置按钮是否要被选中，为True时执行代码就默认被选中
print(checkBox.isChecked())  #检查按钮是否被选中的状态
print(checkBox.isCheckable()) #判断按钮是否可以被选中，如果置灰就不能被选中




window.show()
sys.exit(app.exec())