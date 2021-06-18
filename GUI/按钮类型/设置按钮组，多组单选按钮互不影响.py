from PyQt5.Qt import *
import sys




app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
man = QRadioButton('男', window)
man.move(0, 30)
women = QRadioButton('女', window)

yes = QRadioButton('yes', window)
yes.move(50,0)
no = QRadioButton('no', window)
no.move(50,30)

'''
设置按钮组，将man与women放入同一个按钮组中，就不会与yes与no互斥
'''
sex_group = QButtonGroup(window)
sex_group.addButton(man)
sex_group.addButton(women)

'''
设置按钮组，将yes与wno放入同一个按钮组中，就不会与man与women互斥
'''
answer_group = QButtonGroup(window)
answer_group.addButton(yes)
answer_group.addButton(no)

window.show()
sys.exit(app.exec())