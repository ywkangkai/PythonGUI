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
new_action.setIcon(QIcon(r'D:\PythonGUI\GUI\QWidgt\改变鼠标形状\xxx.png'))
menu.addAction(new_action) #添加子菜单

new_action1 = QAction()
new_action1.setText("最近")
new_action1.setIcon(QIcon(r'D:\PythonGUI\GUI\QWidgt\改变鼠标形状\xxx.png'))

menu.addAction(new_action1) #添加子按钮
btn.setMenu(menu) #设置菜单


window.show()
sys.exit(app.exec())