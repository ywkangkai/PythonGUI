#####每隔一秒进度加1#####



from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        pb = QProgressBar(self)
        pb.resize(300,10)
        pb.setRange(0,100)   #pb.maximum()，pb.minimum()表示范围的最大与最小值
        pb.setValue(0)

        timer = QTimer(self)
        def change_process():
            if pb.value() == pb.maximum():   #pb.value()表示获取当前进度值
                timer.stop()
            pb.setValue(pb.value()+1)
        timer.timeout.connect(change_process)  #时间改变触发
        timer.start(1000) #表示每隔1秒会启动一次

        pb.valueChanged.connect(lambda val:print('当前进度值为',str(val)+'%')) # 进度改变时触发，打印当前进度值


app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
