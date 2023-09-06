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

            #fd.setFileMode(QFileDialog.ExistingFile)  # 设置选择单个文件 setFileMode()方法有三种模式，分别是：ExistingFile、Directory、ExistingFiles表示选择单个文件、选择文件夹、选择多个文件
            fd.setFileMode(QFileDialog.ExistingFiles)  # 设置可以选择多个文件

            #fd.fileSelected.connect(lambda val:print(val))  # 选择单个文件触发
            fd.filesSelected.connect(lambda val: print(val))  # 选择多个个文件触发
            fd.open()
        btn.clicked.connect(openfile)





app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
