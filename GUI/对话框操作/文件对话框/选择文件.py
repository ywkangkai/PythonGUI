from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        '''
        ./ 表示从当前目录打开文件选择对话框
        All(*.*);;Images(*.png*.jpg);;Python文件(*.py)  表示需要过滤哪些类型的文件, 只会这些后缀的文件
        result 选择文件后会返回文件路径
        '''
        # 选择一个文件
        result = QFileDialog.getOpenFileName(self, '选择一个py文件', './', 'All(*.*);;Images(*.png*.jpg);;Python文件(*.py)')
        # 选择多个文件
        # result = QFileDialog.getOpenFileNames(self, '选择一个py文件', './', 'All(*.*);;Images(*.png*.jpg);;Python文件(*.py)')
        # 保存文件，可以将文件保存为下面指定的后缀类型
        # result = QFileDialog.getSaveFileName(self, '选择一个py文件', './', 'All(*.*);;Images(*.png*.jpg);;Python文件(*.py)')
        print(result)



app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
