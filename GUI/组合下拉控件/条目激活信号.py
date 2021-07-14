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
        btn.pressed.connect(self.cao)
        self.asb.activated[str].connect(self.actived)   #  此信号是当选择了下拉中的值，会自动打印值的内容
        #self.asb.activated.connect(self.actived)  #  此信号是当选择了下拉中的值，会自动打印值的索引

    def cao(self):
        print(self.asb.currentText())  #  获取当前值
        print(self.asb.currentIndex())  # 当前索引
        print(self.asb.currentData())  #  这个属性可以获取上面的字典{"name":"123"}，这是额外值，但是在下来项中只会显示这是data获取的

    def actived(self,val):
        print('条目激活',val)


app = QApplication(sys.argv)
window = Window()









window.show()
sys.exit(app.exec_())
