from PyQt5.Qt import *
import sys




app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
man = QRadioButton('男', window)
man.move(100, 100)
women = QRadioButton('女', window)
man.toggled.connect(lambda isCheckd:print(man.text()))  #单选与多选的信号一般都是用toggled，isCheckd方法是判断是否选这个的按钮
print(man.isChecked())



window.show()
sys.exit(app.exec())