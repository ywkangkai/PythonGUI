from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        cw = QCalendarWidget(self)
        cw.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader) # 去掉最左边
        # 设置网格
        cw.setGridVisible(True)
        # 设置最小的年月日
        cw.setMinimumDate(QDate(2023, 1, 1)) # 表示2023年1月1日之前的日期都不可选
        # 设置最大的年月日
        cw.setMaximumDate(QDate(2023, 12, 1))# 表示2023年12月1日之后的日期都不可选
        cw.selectionChanged.connect(lambda :print('日期选择',cw.selectedDate()))  #打印年月日
        cw.selectionChanged.connect(lambda: print('年选择', cw.yearShown())) # 打印年
        cw.selectionChanged.connect(lambda: print('月选择', cw.monthShown())) # 打印月
        # 日期变化信号
        cw.currentPageChanged.connect(lambda y,m: print(y,m))



        btn = QPushButton(self)
        btn.setText('确定')
        btn.move(100,300)





app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
