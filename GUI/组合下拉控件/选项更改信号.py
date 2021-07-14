from PyQt5.Qt import *
import sys





class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton(self)
        btn.move(100,120)
        btn.setText('按钮')
        self.asb = QComboBox(self)
        self.asb.addItems(['1','2','3'])
        self.asb.addItem('这是data获取的', {"name":"123"})
        self.asb.insertItem(1, 'xxx')   #  第一关参数为索引
        self.asb.insertSeparator(1) # 在索引1前插入分割线
        self.asb.currentTextChanged.connect(self.connent)  #  当更换了下拉选项后触发


    def connent(self,val):
        print('当前更换选项值为',val)


app = QApplication(sys.argv)
window = Window()









window.show()
sys.exit(app.exec_())
