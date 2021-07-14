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

    def cao(self):
        print(self.asb.currentText())  #  获取当前值
        print(self.asb.currentIndex())  # 当前索引
        print(self.asb.currentData())  #  这个属性可以获取上面的字典{"name":"123"}，这是额外值，但是在下来项中只会显示这是data获取的

app = QApplication(sys.argv)
window = Window()









window.show()
sys.exit(app.exec_())
