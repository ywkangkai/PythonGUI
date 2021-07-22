from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton(self)
        btn.setText('选择文件')
        def openfile():
            fd = QFileDialog(self, '选择一个py文件', './', 'All(*.*);;Images(*.png*.jpg);;Python文件(*.py)')
            fd.fileSelected.connect(lambda file:print(file))
            fd.setNameFilters(['(*.*)', '(*.png)', '(*.jpg)' , '(*.py)'])  #设置文件过滤形式
            fd.open()
        btn.clicked.connect(openfile)





app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
