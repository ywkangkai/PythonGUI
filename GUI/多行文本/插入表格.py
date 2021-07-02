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


def cao():
    tc = text.textCursor()  # 此方法可以哦获取文本焦点，选择插入的位置
    # tif = tc.insertTable(5, 3)  # 此方法可以直接插入表格，5行3列
    tif = QTextTableFormat()  # 创建表格对象，可以进行表格格式设置
    tif.setAlignment(Qt.AlignRight)  # 将表格放入最右侧
    tif.setCellPadding(6)  # 内边距距离
    tif.setCellSpacing(13)  # 外边距的距离
    #tif.setColumnWidthConstraints(QTextLength(QTextLength.PercentageLength, 25))
    tc.insertTable(5, 4, tif)
    print(tc.insertTable(5, 3, tif))  # 得到的是一个QTextTable的对象，该对象下能继续对列表进行操作


btn.pressed.connect(cao)

window.show()
sys.exit(app.exec_())
