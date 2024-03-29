from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        input = QInputDialog(self,Qt.FramelessWindowHint)
        input.setOption(QInputDialog.UseListViewForComboBoxItems)
        input.setLabelText('请输入你的姓名')
        input.setOkButtonText('好的')
        input.setCancelButtonText('我想取消')

        input.textValueChanged.connect(lambda val:print(val)) # textValueChanged，文本值发生改变时发出的信号，intValueChanged，整数值发生改变时发出的信号，doubleValueChanged，浮点数值发生改变时发出的信号
        input.show()





app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
