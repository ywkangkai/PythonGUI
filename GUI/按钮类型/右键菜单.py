from PyQt5.Qt import *
import sys

class Window(QWidget):

    def contextMenuEvent(self, QContextMenuEvent):   #点击鼠标右键后会自动触发该事件

        menu = QMenu(self)  # 获取菜单

        open_recent_menu = QMenu(menu)
        open_recent_menu.setTitle('最近打开')

        '''
        可以添加多个下拉菜单
        '''
        new_action = QAction()
        new_action.setText("新建")
        new_action.setIcon(QIcon(r'D:\PythonGUI\GUI\QWidgt\改变鼠标形状\xxx.png'))  # 子菜单按钮增加图标标识
        new_action.triggered.connect(lambda: print('子菜单按钮触发'))  # 子菜单按钮触发槽与信号需要用到triggered
        file_action = QAction()
        file_action.setText('pythonGUI')

        menu.addAction(new_action)
        menu.addMenu(open_recent_menu)  # 添加子菜单
        open_recent_menu.addAction(file_action)  # 添加2级子按钮

        menu.exec_(QContextMenuEvent.globalPos())   # exec_可以将菜单显示在窗口中，QContextMenuEvent.globalPos()是设置菜单相对于整个屏幕的位置


app = QApplication(sys.argv)
window = Window()
window.resize(500, 500)
btn = QPushButton('file',window)





window.show()
sys.exit(app.exec())