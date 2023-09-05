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

        cb.setEditable(True)
        cb.setEditText("itlike")
        cb.resize(400, 30)
        print(QAbstractItemModel.__subclasses__())
        model = QStandardItemModel()

        item1 = QStandardItem("item1")
        item2 = QStandardItem("item2")
        item22 = QStandardItem("item22")
        item2.appendRow(item22)
        model.appendRow(item1)
        model.appendRow(item2)
        cb.setModel(model)

        cb.setView(QTreeView(cb))




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())