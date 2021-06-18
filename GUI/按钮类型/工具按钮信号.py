from PyQt5.Qt import *
import sys




app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
btn = QToolButton(window)
btn.setText('工具')

menu = QMenu()  #获取菜单

open_recent_menu = QMenu(menu)
open_recent_menu.setTitle('最近打开')

'''
可以添加多个下拉菜单
'''
new_action = QAction()
new_action.setText("新建")
new_action.setIcon(QIcon(r'D:\PythonGUI\GUI\QWidgt\改变鼠标形状\xxx.png'))  #子菜单按钮增加图标标识
new_action.triggered.connect(lambda :print('子菜单按钮触发'))  #子菜单按钮触发槽与信号需要用到triggered

aciton1 = QAction("行为1", menu)
aciton1.setData('这是行为1')
aciton2 = QAction("行为2", menu)
aciton2.setData('这是行为2')

menu.addAction(new_action)
menu.addSeparator()
menu.addMenu(open_recent_menu) #添加子菜单
menu.addAction(aciton1)
menu.addAction(aciton2)

btn.setMenu(menu) #设置菜单

btn.setPopupMode(QToolButton.MenuButtonPopup)   #工具按钮与Qpushbotton不一样，需要设置弹出方式才会显示出来下拉菜单
#btn.setPopupMode(QToolButton.InstantPopup)    #工具按钮与Qpushbotton不一样，需要设置弹出方式才会显示出来下拉菜单

def do_action(action):     #工具按钮在定义槽函数时，需要传入一个action对象，这个action会根据上面设置的data来判断点的哪个按钮
    print(action.data())

btn.triggered.connect(do_action)

window.show()
sys.exit(app.exec())