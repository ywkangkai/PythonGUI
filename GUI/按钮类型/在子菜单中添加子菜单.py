from PyQt5.Qt import *
import sys




app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
btn = QPushButton('file',window)



menu = QMenu(btn)  #获取菜单

open_recent_menu = QMenu(menu)
open_recent_menu.setTitle('最近打开')

'''
可以添加多个下拉菜单
'''
new_action = QAction()
new_action.setText("新建")
new_action.setIcon(QIcon(r'D:\PythonGUI\GUI\QWidgt\改变鼠标形状\xxx.png'))  #子菜单按钮增加图标标识
new_action.triggered.connect(lambda :print('子菜单按钮触发'))  #子菜单按钮触发槽与信号需要用到triggered

file_action = QAction()
file_action.setText('pythonGUI')

menu.addAction(new_action)
menu.addMenu(open_recent_menu) #添加子菜单
open_recent_menu.addAction(file_action)  #添加2级子按钮

btn.setMenu(menu) #设置菜单

window.show()
sys.exit(app.exec())