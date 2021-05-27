

from PyQt5.Qt import *
import sys

class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.QObject()

    def QObject(self):

        lable1 = QLabel(self)
        lable1.move(100,100)
        lable1.setText('第一关文本控件')
        lable2 = QLabel(self)
        lable2.move(200, 200)
        lable2.setText('第二个文本控件')
        bin = QPushButton(self)
        bin.move(300,300)
        bin.setText("点我")

        for i in self.children():
            if i.inherits("QLabel"):   #判定前一个控件是否继承后一个控件
                print("是")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())