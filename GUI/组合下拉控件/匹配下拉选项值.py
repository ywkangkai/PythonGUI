from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        cb = QComboBox(self)
        cb.addItems(["abc", "123", "456"])
        cb.addItem(QIcon("xxx.png"), "撩课", {"name": "itlike"})
        cb.setMaxCount(6)
        cb.setEditable(True)
        cb.setDuplicatesEnabled(True)
        cb.setCompleter(QCompleter(["123", "abc", "aaa", "bbb"]))




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())