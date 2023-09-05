from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDateEdit的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        de = QDateEdit(self)
        de.setDisplayFormat("yy-MMMM-dddd") # MMMM代表月份的全称，MMMM代表星期的全称 dddd代表日期的全称
        print(de.date())

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    
    window = Window()
    window.show()
    
    
    sys.exit(app.exec_())