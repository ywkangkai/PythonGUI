from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        em = QErrorMessage(self)
        em.setWindowTitle('错误提示')
        em.showMessage('具体提示的内容')
        em.open()

app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
