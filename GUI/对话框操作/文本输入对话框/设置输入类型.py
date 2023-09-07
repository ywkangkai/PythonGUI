from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        input = QInputDialog(self,Qt.FramelessWindowHint)
        input.setComboBoxItems(['18','19','20'])
        # input.setInputMode(QInputDialog.DoubleInput)  #表示只能输入浮点型
        #input.setInputMode(QInputDialog.InputMode)  #表示只能输入整数
        input.setInputMode(QInputDialog.TextInput) #表示只能输入文本
        input.setLabelText('请输入你的姓名')
        input.setOkButtonText('好的')
        input.setCancelButtonText('我想取消')

        input.textValueChanged.connect(lambda val:print(val))
        input.show()





app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
