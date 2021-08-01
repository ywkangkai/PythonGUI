from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        cw = QCalendarWidget(self)
        cw.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        cw.selectionChanged.connect(lambda :print('日期选择',cw.selectedDate()))  #选择日期后触发信号



        btn = QPushButton(self)
        btn.setText('确定')
        btn.move(100,300)





app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
