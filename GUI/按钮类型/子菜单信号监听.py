from PyQt5.Qt import *
import sys




app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
btn = QPushButton('file',window)



menu = QMenu()  #获取菜单

'''
可以添加多个下拉菜单
'''
new_action = QAction()
new_action.setText("新建")
new_action.setIcon(QIcon(r'D:\PythonGUI\GUI\QWidgt\改变鼠标形状\xxx.png'))  #子菜单按钮增加图标标识
new_action.triggered.connect(lambda :print('子菜单按钮触发'))  #子菜单按钮触发槽与信号需要用到triggered

open = QAction()
open.setText("打开")

exit = QAction()
exit.setText("退出")

menu.addAction(new_action) #添加子按钮
menu.addAction(open)
menu.addSeparator() #添加分割线
menu.addAction(exit)
btn.setMenu(menu) #设置菜单

window.show()
sys.exit(app.exec())