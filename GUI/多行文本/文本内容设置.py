from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)

text = QTextEdit(window)
'''
text.setPlainText("<h1>ooo</h1>")   #设置普通文本
text.insertPlainText("adsads")  #插入普通文本
'''
'''
text.setHtml("<h1>ooo</h1>")  # 设置html文本
text.insertHtml("<h2>ooo</h2>")  # 插入html文本
text.insertHtml("<a>www.baidu.com</a>")  # 通过这种方式设置超链接
'''
text.setText("<h1>ooo</h1>")  # 既可设置html也可以设置普通   insertText插入文本同理
text.append("<h1>xxx</h1>")  # 会在文本下方追加，能自动识别格式
a = text.document()  # 获取文本内容
print(a)
window.show()
sys.exit(app.exec_())
