from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton(self)
        btn.setText('选择颜色')
        def open_color_window():
            cd = QColorDialog(self)
            cd.setOption(QColorDialog.NoButtons)  #  会取消掉颜色对话的确定和取消按钮
            cd.setWindowTitle('选择背景颜色')

            def sel_color(color):
                palette = QPalette()
                palette.setColor(QPalette.Background, color)
                self.setPalette(palette)

            #cd.colorSelected.connect(sel_color)  # 用它就不要用cd.setOption(QColorDialog.NoButtons)
            cd.currentColorChanged.connect(sel_color)  # 选择颜色后会实时展示，需要与上方的cd.setOption(QColorDialog.NoButtons)一起用
            cd.show()

        btn.clicked.connect(open_color_window)




app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
