from PyQt5.Qt import *
import sys





class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        asb = QComboBox(self)
        asb.addItem('1')
        asb.addItem(QIcon('D:\PythonGUI\open.png'),'xx1')
        asb.setItemText(0,'2')  # 修改1为2
        asb.setItemIcon(1, QIcon('D:\PythonGUI\close.png'))  # 修改图片

app = QApplication(sys.argv)
window = Window()









window.show()
sys.exit(app.exec_())
