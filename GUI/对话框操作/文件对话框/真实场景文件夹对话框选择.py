from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton(self)
        btn.setText('选择文件夹')
        def openfile():
            fd = QFileDialog(self, '选择一个文件夹', './', 'All(*.*);;Images(*.png*.jpg);;Python文件(*.py)')
            fd.fileSelected.connect(lambda file:print(file))
            fd.setFileMode(QFileDialog.Directory)  # 设置选择模式，设置为选择文件夹
            fd.directoryEntered.connect(lambda path: print(path))  #  选择文件夹时触发
            fd.open()
        btn.clicked.connect(openfile)



app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
