from PyQt5.Qt import *
import sys
app = QApplication(sys.argv)
window = QMainWindow()
window.statusBar()
window.setStatusTip('鼠标移到窗口中才能看到')
window.resize(500, 500)
window.setWindowFlags(Qt.WindowContextHelpButtonHint) #窗口右上角会多一个问号

labl = QLabel(window)
labl.setText('xxxxx')
labl.setStatusTip('鼠标移动到标签上才能看到')

labl.setToolTip('鼠标移动到此标签上会有现实两秒')
labl.setToolTipDuration(2000)

labl.setWhatsThis("先点击问号，在点击该标签就能现实这段信息")

window.show()
sys.exit(app.exec())







