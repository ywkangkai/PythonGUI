from PyQt5.Qt import *
import sys





class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        asb = QComboBox(self)
        asb.addItem(QIcon('D:\PythonGUI\open.png'),'xx1')
        asb.insertItem(1, QIcon('D:\PythonGUI\open.png'),'xx2')   #  第一关参数为索引

app = QApplication(sys.argv)
window = Window()









window.show()
sys.exit(app.exec_())
