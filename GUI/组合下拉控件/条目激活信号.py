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
        # 可编辑
        self.asb.setEditable(True)   #  此属性可以使选项框变为可编辑
        self.asb.activated[str].connect(self.actived)   #  可在页面输入内容，按下回车，会自动打印出输入的内容
        #self.asb.activated.connect(self.actived)  #  此信号是当选择了下拉中的值，会自动打印值的索引


    def actived(self,val):
        print('条目激活',val)


app = QApplication(sys.argv)
window = Window()









window.show()
sys.exit(app.exec_())
