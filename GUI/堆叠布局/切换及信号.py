from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label1 = QLabel('x1')
        label1.setStyleSheet('background-color:cyan')
        label2 = QLabel('x2')
        label2.setStyleSheet('background-color:yellow')
        label3 = QLabel('x3')
        label3.setStyleSheet('background-color:red')

        label4 = QLabel('x4')
        label4.setStyleSheet('background-color:cyan')
        label5 = QLabel('x5')
        label5.setStyleSheet('background-color:yellow')
        label6 = QLabel('x6')
        label6.setStyleSheet('background-color:red')

        v_layout = QBoxLayout(QBoxLayout.TopToBottom)
        v_layout.addWidget(label4)
        v_layout.addWidget(label5)
        v_layout.addWidget(label6)

        # 创建堆叠布局对象
        s1 = QStackedLayout()
        # 把布局对象给需要布局的父控件
        self.setLayout(s1)
        # 通过布局对象，把需要布局的控件添加到布局中
        s1.addWidget(label1)
        s1.addWidget(label2)
        s1.addWidget(label3)
        # print(s1.widget(1).text())
        # s1.setCurrentIndex(1) # 切换到第二个标签

        timer = QTimer(self)
        timer.timeout.connect(lambda :s1.setCurrentIndex((s1.currentIndex() + 1) % s1.count()))
        timer.start(1000)

        s1.currentChanged.connect(lambda val:print(val)) # 打印当前索引值









app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
