
from PyQt5.Qt import *
import sys




app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
QFrame = QFrame(window)
QFrame.resize(200,200)
QFrame.move(100,100)
QFrame.setFrameShape(QFrame.Box) # 设置边框样式 QFrame.Box | QFrame.Panel | QFrame.WinPanel | QFrame.HLine | QFrame.VLine | QFrame.StyledPanel | QFrame.Raised

window.show()
sys.exit(app.exec_())
