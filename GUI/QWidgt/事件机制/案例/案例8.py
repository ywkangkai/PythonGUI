
#实现全选和取消全选
import sys
from PyQt5.Qt import *

class App(QWidget):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle('select button')
        self.resize(250,250)
        self.btn()
    def btn(self):

        push_btn1=QPushButton(self)
        push_btn1.setText('select all')
        push_btn1.move(0,20)
        push_btn2 = QPushButton(self)
        push_btn2.setText('counter election')
        push_btn2.move(100,20)

        radio_btn1=QRadioButton(self)
        radio_btn1.move(0,50)
        radio_btn1.setText('male')
        radio_btn2 = QRadioButton(self)
        radio_btn2.move(50, 50)
        radio_btn2.setText('female')

        check_btn1=QCheckBox(self)
        check_btn1.move(20,100)
        check_btn1.setText('1')
        check_btn2 = QCheckBox(self)
        check_btn2.move(20, 120)
        check_btn2.setText('2')
        check_btn3 = QCheckBox(self)
        check_btn3.move(20, 140)
        check_btn3.setText('3')
        self.a = True
        def sec_all():
            if self.a:
                check_btn1.setChecked(True)   #设置按钮被选中
                check_btn2.setChecked(True)
                check_btn3.setChecked(True)
                self.a=False
            else:
                check_btn1.setChecked(False)
                check_btn2.setChecked(False)
                check_btn3.setChecked(False)
                self.a=True
        def con_elec():
            check_btn1.toggle()  #内置方法，直接切换选中与非选中状态
            check_btn2.toggle()
            check_btn3.toggle()
        push_btn1.clicked.connect(sec_all)
        push_btn2.clicked.connect(con_elec)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=App()
    window.show()
    sys.exit(app.exec_())
