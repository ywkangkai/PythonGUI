
from PyQt5.Qt import *
import sys
app = QApplication(sys.argv)
window = QWidget(flags=Qt.FramelessWindowHint)
window.resize(500, 500)

window.show()
sys.exit(app.exec())