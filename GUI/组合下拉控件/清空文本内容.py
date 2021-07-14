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
        self.asb.setEditable(True)   #  此属性可以使选项框变为可编辑
        btn.clicked.connect(self.cao)

    def cao(self):
        self.asb.clearEditText()  #  清空当前已选的内容

app = QApplication(sys.argv)
window = Window()









window.show()
sys.exit(app.exec_())
