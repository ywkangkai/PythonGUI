from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDateTimeEdit的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        dte = QDateTimeEdit(self)
        # dte = QDateTimeEdit(QDateTime.currentDateTime(), self) # 获取当前时间日期
        # dte = QDateTimeEdit(QDate.currentDate(), self) # 获取当前日期
        # dte = QDateTimeEdit(QTime.currentTime(), self) # 获取当前时间
        dte.move(100, 100)

        dte.setDisplayFormat("yyyy-MM-dd HH: mm: ss") # 设置显示格式

        btn = QPushButton(self)
        btn.move(200, 200)
        btn.setText("测试")
        # btn.clicked.connect(lambda :print(dte.currentSectionIndex()))
        def test():
            # print("xxx")
            # dte.setFocus()
            # dte.setCurrentSectionIndex(3) # 设置当前选中的部分
            # dte.setCurrentSection(QDateTimeEdit.DaySection) # 设置当前选中的部分
            # print(dte.sectionText(QDateTimeEdit.DaySection)) # 获取当前选中部分的文本
            # dte.setMaximumDateTime(QDateTime(2020, 8, 15, 12, 30)) # 设置最大时间
            #
            # dte.setMinimumDateTime(QDateTime.currentDateTime())

            # dte.setDateTimeRange(QDateTime.currentDateTime().addDays(-3), QDateTime.currentDateTime().addDays(3)) # 设置时间范围
            # print(dte.dateTime()) # 获取日期时间
            print(dte.date()) # 获取日期
            print(dte.time()) # 获取时间

        btn.clicked.connect(test)
        print(dte.sectionCount())
        dte.setCalendarPopup(True)  # 设置日历弹出

        dte.dateTimeChanged.connect(lambda val:print(val))
        dte.dateChanged.connect(lambda val: print("日期发生改变", val))
        dte.timeChanged.connect(lambda val: print("时间发生改变", val))



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())