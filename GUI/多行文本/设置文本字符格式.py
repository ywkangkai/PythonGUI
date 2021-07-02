from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)

text = QTextEdit(window)
tcf = QTextCharFormat()
tcf.setToolTip('鼠标停留到文字上才会显示')
tcf.setFontFamily('隶书')  # 文本格式
tcf.setFontPointSize(66)  # 文字大小
tc = text.textCursor()
tc.insertText('asdads',tcf)


window.show()
sys.exit(app.exec_())
