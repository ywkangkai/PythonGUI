from PyQt5.Qt import *

class MyTextEdit(QTextEdit):
    def mousePressEvent(self, me):
        print(me.pos())
        link_str = self.anchorAt(me.pos())
        if len(link_str) > 0:
            QDesktopServices.openUrl(QUrl(link_str)) # openUrl打开链接
        return super().mousePressEvent(me)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit的学习")
        self.resize(500, 500)
        self.setup_ui()

    def text_change(self):
        print("文本内容发生了改变")
    def selection_change(self):
        print("文本选中的内容发生了改变")
    def copy_a(self, yes):
        print("复制是否可用", yes)
    def setup_ui(self):
        te = MyTextEdit("xxx", self)
        self.te = te
        te.move(50, 50)
        te.resize(300, 300)
        te.setStyleSheet("background-color: cyan;")

        te.textChanged.connect(self.text_change)
        # te.selectionChanged.connect(self.selection_change)
        te.copyAvailable.connect(self.copy_a)

        test_btn = QPushButton(self)
        test_btn.move(10, 10)
        test_btn.setText("测试按钮")
        test_btn.pressed.connect(self.btn_test)

        # self.占位文本的提示()
        # self.文本内容的设置()
        # tlf = QTextListFormat()
        # tlf.setIndent(3)
        # tlf.setNumberPrefix("<<")
        # tlf.setNumberSuffix("<<")
        # tlf.setStyle(QTextListFormat.ListDecimal)
        # tl = te.textCursor().createList(tlf)
        te.textCursor().insertTable(5, 3)
        # te.insertHtml("xxx " * 300 + "<a name='lk' href='#itlike'>撩课</a>" + "aaa" * 200)
        te.insertHtml("xxx " * 300 + "<a href='http://www.itlike.com'>撩课</a>" + "aaa" * 200)

    def btn_test(self):
        # self.te.setText("")
        # self.te.clear()
        # QTextDocument
        # print(self.te.document())
        # QTextCursor
        # print(self.te.textCursor())
        self.打开超链接()

        pass
    def 打开超链接(self):
        pass
    def tab功能测试(self):
        # self.te.setTabChangesFocus(True)
        print(self.te.tabStopDistance())
        print(self.te.tabStopWidth())
        self.te.setTabStopDistance(100)
        pass
    def 只读设置(self):
        print(self.te.isReadOnly())
        self.te.setReadOnly(True)
        self.te.insertPlainText("itlike")
        print(self.te.isReadOnly())
        pass
    def 滚动到锚点(self):
        self.te.scrollToAnchor("lk")
        pass
    def 常用编辑操作(self):
        # self.te.copy()
        # self.te.paste()
        # self.te.selectAll()
        # self.te.setFocus()
        # QTextDocument.FindBackward
        print(self.te.find("xx", QTextDocument.FindBackward | QTextDocument.FindCaseSensitively | QTextDocument.FindWholeWords)) # find查找文本  findBackward从后往前查找  findCaseSensitively区分大小写  findWholeWords全词匹配
        self.te.setFocus()
        pass
    def 字符设置(self):
        tcf = QTextCharFormat()
        tcf.setFontFamily("宋体")
        tcf.setFontPointSize(20)
        tcf.setFontCapitalization(QFont.Capitalize)
        tcf.setForeground(QColor(100, 200, 150))
        self.te.setCurrentCharFormat(tcf)


        tcf2 = QTextCharFormat()
        tcf2.setFontOverline(True)
        # self.te.setCurrentCharFormat(tcf2)
        self.te.mergeCurrentCharFormat(tcf2)

        pass
    def 颜色设置(self):
        self.te.setTextBackgroundColor(QColor(200, 10, 10))
        self.te.setTextColor(QColor(10, 200, 10))
        pass
    def 字体设置(self):
        # QFontDialog.getFont()
        # self.te.setFontFamily("幼圆")
        # self.te.setFontWeight(QFont.Black)
        # self.te.setFontItalic(True)
        # self.te.setFontPointSize(30)
        # self.te.setFontUnderline(True)
        font = QFont()
        font.setStrikeOut(True)
        self.te.setCurrentFont(font)
    def 对齐方式(self):
        self.te.setAlignment(Qt.AlignCenter) # AlignLeft左对齐  AlignRight右对齐  AlignCenter居中对齐  AlignJustify两端对齐
        pass
    def 光标设置(self):
        # print(self.te.cursorWidth())
        print(self.te.cursorRect(self.te.textCursor()))
        if self.te.overwriteMode():
            self.te.setOverwriteMode(False) # setOverwriteMode设置覆盖模式
            self.te.setCursorWidth(1) # setCursorWidth设置光标的宽度
        else:
            self.te.setOverwriteMode(True)
            self.te.setCursorWidth(10)
    def 覆盖模式的设置(self):
        self.te.setOverwriteMode(True)
        print(self.te.overwriteMode())
    def 软换行模式(self):
        # self.te.setLineWrapMode(QTextEdit.NoWrap) # NoWrap不换行  WidgetWidth自动换行  FixedPixelWidth固定像素宽度换行  FixedColumnWidth固定列宽换行
        # self.te.setLineWrapMode(QTextEdit.FixedPixelWidth)
        self.te.setLineWrapMode(QTextEdit.FixedColumnWidth)
        self.te.setLineWrapColumnOrWidth(8) # setLineWrapColumnOrWidth设置换行的列数或者宽度

        self.te.setWordWrapMode(QTextOption.WordWrap) # WordWrap按照单词换行  NoWrap不换行  ManualWrap手动换行
        pass
    def 自动格式化(self):
        QTextEdit
        self.te.setAutoFormatting(QTextEdit.AutoBulletList)
    def 开始和结束操作(self):
        tc = self.te.textCursor()

        tc.beginEditBlock()
        tc.insertText("123")
        tc.insertBlock()
        tc.insertText("456")
        tc.insertBlock()
        tc.endEditBlock()

        tc.insertText("789")
        tc.insertBlock()


        pass
    def 位置相关(self):
        tc = self.te.textCursor()
        print("是否在段落的结尾:", tc.atBlockEnd())
        print("是否在段落的开始:", tc.atBlockStart())
        print("是否在文档的结尾:", tc.atEnd())
        print("是否在文档的开始:", tc.atStart())

        print("在第几列", tc.columnNumber())
        print("光标位置", tc.position())
        print("在文本块中的位置", tc.positionInBlock())

        pass
    def 文本字符的删除(self):
        tc = self.te.textCursor()
        # tc.deleteChar()
        tc.deletePreviousChar()
        self.te.setFocus()
        pass
    def 文本的其他操作(self):
        tc = self.te.textCursor()
        # print(tc.selectionStart())
        # print(tc.selectionEnd())
        # tc.clearSelection()
        # self.te.setTextCursor(tc)
        # print(tc.hasSelection())
        tc.removeSelectedText()
        self.te.setFocus()
        pass
    def 文本选中内容的获取(self):
        tc = self.te.textCursor()
        # print(tc.selectedText())
        QTextDocumentFragment
        # print(tc.selection().toPlainText())
        print(tc.selectedTableCells())
        pass
    def 文本选中和清空(self):
        tc = self.te.textCursor()
        # tc.setPosition(6, QTextCursor.KeepAnchor) # KeepAnchor保持锚点
        # tc.movePosition(QTextCursor.Up, QTextCursor.KeepAnchor, 1)
        tc.select(QTextCursor.WordUnderCursor)
        self.te.setTextCursor(tc)

        self.te.setFocus()
        pass
    def 内容和格式的获取(self):
        tc = self.te.textCursor()
        # QTextList
        # print(tc.block().text()) # block获取当前光标所在的文本块  blockNumber获取当前光标所在的文本块的编号  blockCount获取文本块的总数
        # print(tc.blockNumber())
        print(tc.currentList().count()) # currentList获取当前光标所在的列表  currentList获取当前光标所在的列表的编号  currentList获取当前光标所在的列表的总数
        pass
    def 格式设置和合并(self):
        tc = self.te.textCursor()
        tcf = QTextCharFormat() # QTextCharFormat 可以设置字体的样式
        tcf.setFontFamily("幼圆")
        tcf.setFontPointSize(30)
        tcf.setFontOverline(True) # setFontOverline设置字体上划线
        tcf.setFontUnderline(True) # setFontUnderline设置字体下划线
        tc.setCharFormat(tcf) # setCharFormat设置字符的格式  setBlockCharFormat设置块的格式

        tcf2 = QTextCharFormat()
        tcf2.setFontStrikeOut(True) # setFontStrikeOut设置字体删除线
        # tc.setCharFormat(tcf2)
        tc.mergeCharFormat(tcf2)

        return None
        tbf = QTextBlockFormat()
        tbf.setAlignment(Qt.AlignCenter)
        tbf.setIndent(2)
        tc.setBlockFormat(tbf)

        return None
        tcf = QTextCharFormat()
        tcf.setFontFamily("幼圆")
        tcf.setFontPointSize(30)
        tcf.setFontOverline(True)
        tcf.setFontUnderline(True)
        tc.setBlockCharFormat(tcf)


        pass
    def 光标插入内容(self):
        # 插入文本框架
        tc = self.te.textCursor()
        tff = QTextFrameFormat() # QTextFrameFormat 可以设置框架的样式
        tff.setBorder(10) # setBorder设置边框的宽度  setBorderStyle设置边框的样式  setBorderBrush设置边框的颜色
        tff.setBorderBrush(QColor(100, 50, 50)) # setPadding设置内边距  setMargin设置外边距  setWidth设置宽度  setHeight设置高度
        tff.setRightMargin(50)
        tc.insertFrame(tff)

        doc = self.te.document()
        #QTextFrame
        root_frame = doc.rootFrame()
        root_frame.setFrameFormat(tff)

        return None
        # 插入文本块
        tc = self.te.textCursor()
        tbf = QTextBlockFormat() # QTextBlockFormat 可以设置文本块的样式
        tcf = QTextCharFormat() # QTextCharFormat 可以设置字体的样式
        tcf.setFontFamily("隶书") # 设置字体 setFontFamily设置字体  setFontPointSize设置字体大小  setFontWeight设置字体粗细  setFontItalic设置字体斜体
        tcf.setFontItalic(True) # 设置字体斜体 setFontUnderline设置字体下划线  setFontOverline设置字体上划线  setFontStrikeOut设置字体删除线
        tcf.setFontPointSize(60) # 设置字体大小
        tbf.setAlignment(Qt.AlignRight) # 设置对齐方式  AlignRight右对齐  AlignLeft左对齐  AlignCenter居中对齐
        tbf.setRightMargin(100) # setRightMargin设置右侧的距离 setLeftMargin设置左侧的距离 setTopMargin设置上侧的距离 setBottomMargin设置下侧的距离
        # tbf.setIndent(3)
        tc.insertBlock(tbf, tcf) # insertBlock插入文本块  insertText插入文本  insertFragment插入文档片段  insertFrame插入框架  insertImage插入图片  insertTable插入表格
        self.te.setFocus()

        return None
        # 插入列表
        tc = self.te.textCursor()
        # tc.insertTable(5, 3)
        ttf = QTextTableFormat() # QTextTableFormat 可以设置表格的样式
        ttf.setAlignment(Qt.AlignRight) # 将表格放入最右侧
        ttf.setCellPadding(6) # 内边距距离
        ttf.setCellSpacing(13) # 外边距的距离
        # QTextLength
        ttf.setColumnWidthConstraints((QTextLength(QTextLength.PercentageLength, 50), QTextLength(QTextLength.PercentageLength, 40),
                                       QTextLength(QTextLength.PercentageLength, 10))) # 设置列宽
        # QTextTable
        # print(tc.insertTable(5, 3, ttf))
        table = tc.insertTable(5, 3, ttf) # 得到的是一个QTextTable的对象，该对象下能继续对列表进行操作
        # table.appendColumns(2)

        return None
        tc = self.te.textCursor()
        # tl = tc.insertList(QTextListFormat.ListCircle)
        # tl = tc.insertList(QTextListFormat.ListDecimal)
        # tl = tc.createList(QTextListFormat.ListDecimal)
        tlf = QTextListFormat()
        tlf.setIndent(3)
        tlf.setNumberPrefix("<<")
        tlf.setNumberSuffix("<<")
        tlf.setStyle(QTextListFormat.ListDecimal)
        tl = tc.createList(tlf)
        print(tl)
        QTextList
        return None
        tc = self.te.textCursor()
        # tdf = QTextDocumentFragment.fromHtml("<h1>xxx</h1>")
        tdf = QTextDocumentFragment.fromPlainText("<h1>xxx</h1>")
        tc.insertFragment(tdf)


        return None
        tc = self.te.textCursor()
        tif = QTextImageFormat()
        tif.setName("xxx.png")
        tif.setWidth(100)
        tif.setHeight(100)
        # tc.insertImage(tif)
        # tc.insertImage(tif, QTextFrameFormat.FloatRight)
        tc.insertImage("xx.jpg")

        return None
        QTextCursor
        tcf = QTextCharFormat()
        tcf.setToolTip("撩课学院网址")
        tcf.setFontFamily("隶书")
        tcf.setFontPointSize(66)
        tc = self.te.textCursor()
        tc.insertText("itlike.com", tcf)

        tc.insertHtml("<a href='http://www.itlike.com'> 撩课 </a>")


        pass
    def 文本内容的设置(self):
        # 设置普通文本内容
        # self.te.setPlainText("<h1>ooo</h1>")
        # self.te.insertPlainText("<h1>ooo</h1>")
        # print(self.te.toPlainText())

        # 富文本的操作
        # self.te.setHtml("<h1>ooo</h1>")
        # self.te.insertHtml("<h6>社会我顺哥</h6>")
        # print(self.te.toHtml())
        # self.te.setText("<h1xxx>ooo</h1xxx>")
        # self.te.append("<h3>ooo</h3>")

        pass
    def 占位文本的提示(self):
        self.te.setPlaceholderText("请输入你的个人简介")
        print(self.te.placeholderText())


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())