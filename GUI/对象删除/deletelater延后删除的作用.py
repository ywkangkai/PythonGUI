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
        #del lable2  如果直接用del删除是无法删除的，因为主控件还引用着lable2这个控件
        lable2.deleteLater()  #延后删除是指主程序运行完成后才会删除，deleteLater后面有引用到lable2的地方也能使用，但是会在主程序
                               #调用完后删除掉
        print(lable2)

        bin = QPushButton(self)
        bin.move(300,300)
        bin.setText("点我")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())