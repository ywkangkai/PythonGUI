from PyQt5.Qt import *
import sys


'''
文本编辑器没有click，press槽与信号的点击事件
所以需要重写内置的点击事件
'''

class ASB(QAbstractSpinBox):
    def stepEnabled(self):
        current_num = int(self.text())
        print(current_num)
        if current_num == 0:
            return QAbstractSpinBox.StepUpEnabled
        elif current_num == 9:
            return QAbstractSpinBox.SetpDownEnabled
        elif current_num < 0 or current_num > 9:
            return QAbstractSpinBox.StepNone
        else:
            return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.SetpDownEnabled

    def stepBy(self, p_int):
        print(p_int)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        asb = ASB(self)
        asb.move(100,100)
        asb.resize(100,30)


app = QApplication(sys.argv)
window = Window()









window.show()
sys.exit(app.exec_())
