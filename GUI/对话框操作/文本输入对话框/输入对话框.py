from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # input = QInputDialog(self,Qt.FramelessWindowHint) # 最原始的输入对话框
        # reslut = QInputDialog.getInt(self,'xxx','请输入你的年龄',value=18,min=1,max=100,step=2) # int类型的输入对话框
        # reslut = QInputDialog.getDouble(self,'xxx','请输入你的年龄',value=18,min=1,max=100,decimals=2) # double类型的输入对话框
        #reslut = QInputDialog.getText(self,'xxx','请输入你的年龄',echo=QLineEdit.Password) # text类型的输入对话框 QLineEdit.Password表示输入的内容以密文的形式显示，其他的还有QLineEdit.Normal,QLineEdit.NoEcho,QLineEdit.PasswordEchoOnEdit分别表示正常显示，不显示，编辑时显示，密码显示
        reslut = QInputDialog.getItem(self,'xxx','请选择你的年龄',['18','19','20'], 18, True) # 选择类型的输入对话框
        # input.show()
        print(reslut)




app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
