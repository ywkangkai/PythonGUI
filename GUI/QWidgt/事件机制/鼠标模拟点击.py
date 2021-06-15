from PyQt5.Qt import *
import sys



app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)

btn = QPushButton(window)
btn.setText("按钮")
def cao():
    print('鼠标被点击了')

btn.pressed.connect(cao)
btn.click()  #这句话的意思是不需要用户手动点直接模拟触发点击





window.show()
sys.exit(app.exec())