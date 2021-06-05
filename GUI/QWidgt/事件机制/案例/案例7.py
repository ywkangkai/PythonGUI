
#当两个标签有部分重叠时，点击一个便签可使其完全展示
from PyQt5.Qt import *
import sys

# class Lable(QLabel):
#     def mousePressEvent(self, QMouseEvent):
#         self.raise_()
#
#
#
# app = QApplication(sys.argv)
# window = QWidget()
# label1 = Lable(window)
# label1.setText("标签1")
# label1.move(200, 200)
# label1.resize(200,200)
# label1.setStyleSheet('background-color:red')
#
# label2 = Lable(window)
# label2.setText("标签1")
# label2.move(300, 300)
# label2.resize(200,200)
# label2.setStyleSheet('background-color:blue')
#
# window.show()
# sys.exit(app.exec())



class Window(QWidget):
    def mousePressEvent(self, QMouseEvent):
        lable = self.findChild(QLabel)
        lable.raise_()



app = QApplication(sys.argv)
window = Window()
label1 = QLabel(window)
label1.setText("标签1")
label1.move(200, 200)
label1.resize(200,200)
label1.setStyleSheet('background-color:red')

label2 = QLabel(window)
label2.setText("标签1")
label2.move(300, 300)
label2.resize(200,200)
label2.setStyleSheet('background-color:blue')

window.show()
sys.exit(app.exec())