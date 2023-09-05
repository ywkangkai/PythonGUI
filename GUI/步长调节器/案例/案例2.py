from PyQt5.Qt import *


# 长按加减按钮
class MyASB(QAbstractSpinBox):
    def __init__(self, parent=None, num ="0", *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.lineEdit().setText(num)

    def stepEnabled(self):

        return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled # StepUpEnabled | StepDownEnabled表示步长调节器的上下按钮都可用

    def stepBy(self, p_int): #stepBy()方法用于设置步长调节器的步长
        print(p_int) #如果stepEnabled()方法返回的是StepUpEnabled，那么p_int就是1，如果返回的是StepDownEnabled，那么p_int就是-1
        current_num = int(self.text()) + p_int
        self.lineEdit().setText(str(current_num))


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAbstractSpinBox的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        asb = MyASB(self, "6")
        self.asb = asb
        asb.resize(100, 30)
        asb.move(100, 100)

        # self.asb.editingFinished.connect(lambda :print("结束编辑"))
        # test_btn = QPushButton(self)
        # test_btn.move(200, 200)
        # test_btn.setText("测试按钮")
        # test_btn.clicked.connect(self.btn_test)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
