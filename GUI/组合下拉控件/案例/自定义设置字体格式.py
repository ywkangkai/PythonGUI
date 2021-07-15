from PyQt5.Qt import *
import sys





class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        self.label = label
        label.setText('拉斯等放假啊')
        label.move(100,100)
        asb = QFontComboBox(self)
        asb.currentFontChanged.connect(self.font_change)
        asb.setEditable(False)

    def font_change(self, font):
        print(font)
        self.label.setFont(font)

app = QApplication(sys.argv)
window = Window()









window.show()
sys.exit(app.exec_())
