from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)

btn = QPushButton(window)
btn.move(300, 300)
btn.setText('按钮')

text = QTextEdit(window)
text.setText('xxx')
# tc = text.textCursor()
# tif = QTextImageFormat()
# tif.setName(r'D:\PythonGUI\close.png')  # 获取图片位置
# tif.setWidth(100)
# tif.setHeight(100)
# tc.insertImage(tif)

def cao():
    tc = text.textCursor()  # 此方法可以哦获取文本焦点，选择插入的位置
    tif = QTextImageFormat()
    tif.setName(r'D:\PythonGUI\close.png')  # 获取图片位置
    tif.setWidth(100)
    tif.setHeight(100)
    tc.insertImage(tif)

btn.pressed.connect(cao)

window.show()
sys.exit(app.exec_())
