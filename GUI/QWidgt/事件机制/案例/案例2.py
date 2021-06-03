#要求：用户按下tab键盘打印


from PyQt5.Qt import *
import sys


class Mylable(QLabel):

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key.Key_Tab:
            print('按下了tab键')



app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
lable = Mylable(window)
lable.resize(200, 200)
lable.setStyleSheet("background-color: yellow")
lable.grabKeyboard()    #这句话的作用是监听键盘，如果不加这句话，按下tab键后，不会触发上面的函数
window.show()
sys.exit(app.exec())


