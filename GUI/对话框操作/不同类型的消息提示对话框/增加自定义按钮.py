from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        pd = QMessageBox(self)
        pd.setIcon(QMessageBox.Information)
        pd.setText('消息内容')
        btn_yes= QPushButton('确认',pd)
        btn_no = QPushButton('取消',pd)
        pd.addButton(btn_yes,QMessageBox.YesRole)
        pd.addButton(btn_no,QMessageBox.NoRole)

        def click(btn):
            if btn == btn_yes:
                print('确认')
            else:
                print('取消')
        pd.buttonClicked.connect(click)

        pd.show()


app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
