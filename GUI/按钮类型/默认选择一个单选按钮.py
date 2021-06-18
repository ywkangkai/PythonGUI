from PyQt5.Qt import *
import sys




app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
man = QRadioButton('男', window)
man.move(100, 100)
women = QRadioButton('女', window)
man.setChecked(True)  # 打开程序默认选择男




window.show()
sys.exit(app.exec())