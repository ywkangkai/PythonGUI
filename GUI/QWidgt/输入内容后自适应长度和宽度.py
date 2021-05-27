from PyQt5.Qt import *
import sys




app = QApplication(sys.argv)
window = QWidget()
lable = QLabel(window)
lable.move(100,100)
lable.setText('xxx')

def clickcao():
    new_content = lable.text() + "xxx"
    lable.setText(new_content)
    lable.adjustSize()

bin = QPushButton(window)
bin.move(300,300)
bin.setText("增加内容")
bin.clicked.connect(clickcao)

window.show()
sys.exit(app.exec())