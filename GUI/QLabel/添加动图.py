from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.setText('xxxxx')
        label.setStyleSheet('background-color:yellow')
        label.move(50, 100)
        label.resize(400,300)
        #label.adjustSize()
        label.setScaledContents(True)  # 内容自适应

        movie = QMovie('11.gif')
        label.setMovie(movie)
        movie.start()



app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
