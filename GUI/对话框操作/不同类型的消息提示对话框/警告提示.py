from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        pd = QMessageBox(QMessageBox.Warning,'窗口标题','内容',QMessageBox.Ok | QMessageBox.Discard,self)
        pd.show()


app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
