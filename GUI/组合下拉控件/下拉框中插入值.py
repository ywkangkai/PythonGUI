from PyQt5.Qt import *
import sys





class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        asb = QComboBox(self)
        asb.addItems(['1','2','3'])
        asb.insertItem(1, 'xxx')   #  第一关参数为索引
        asb.insertSeparator(1) # 在索引1前插入分割线
        print(asb.currentText())

app = QApplication(sys.argv)
window = Window()









window.show()
sys.exit(app.exec_())
