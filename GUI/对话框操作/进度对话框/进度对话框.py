from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        pd = QProgressDialog('下载进度','取消',1,100,self)
        pd.setWindowTitle('xxxx')
        print(pd.maximum())
        print(pd.minimum())
        pd.setValue(90)
        #pd.setAutoClose(False)  # 当进度满了后会自动关闭进度条
        #pd.setAutoReset(False)  #自动重置进度，一般给他关闭，否则进度满了后又会从0开始增加进度
        pd.open()  #open以模态对话框的方式打开，必须要关闭窗口后才能操作后面的窗口 show是非模态对话框

        # for i in range(1, 500):
        #     pd.setValue(i)

        timer = QTimer(pd)
        def cancle():
            if pd.value()+1 >= pd.maximum() or pd.wasCanceled():
                timer.stop()

            pd.setValue(pd.value() + 1)
        timer.timeout.connect(cancle)
        timer.start(1000)


app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
