from PyQt5.Qt import *
import sys


class MyLable(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText("10")   #传参进来这里的10被直接替换
        self.move(300, 300)
        self.time_id = self.startTimer(1000)  # 毫秒

    def setSec(self, ms):
        self.setText(str(ms))


    def timerEvent(self, *args, **kwargs):
        print('xx')
        current_time = int(self.text())
        current_time = current_time - 1
        self.setText(str(current_time))
        if current_time == 0:
            print("停止")
            self.killTimer(self.time_id)


app = QApplication(sys.argv)
window = QWidget()

lable = MyLable(window)
lable.setSec(5)

window.show()
sys.exit(app.exec())