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
        asb.removeItem(0)

app = QApplication(sys.argv)
window = Window()









window.show()
sys.exit(app.exec_())
