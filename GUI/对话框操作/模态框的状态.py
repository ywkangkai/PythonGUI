from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)
window = QWidget()
window.resize(500,500)
d = QDialog()

btn1 = QPushButton(d)
btn1.setText('1')
btn1.clicked.connect(lambda :d.accept())   # 相当于打开一个上传文件窗口选择文件点击确定 返回值为0


btn2 = QPushButton(d)
btn2.setText('2')
btn2.clicked.connect(lambda :d.reject())  # 相当于打开一个上传文件窗口，点击取消  返回值为1
btn2.move(60, 60)



btn3 = QPushButton(d)
btn3.setText('3')
btn3.clicked.connect(lambda :d.done(8))   # 关闭窗口
btn3.move(60, 160)

d.exec()  #  展示窗口的方法  还有：show()   open()


window.show()
sys.exit(app.exec_())