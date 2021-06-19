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
sex_group.setId(man,1)
sex_group.setId(women,2)
'''
设置按钮组，将yes与wno放入同一个按钮组中，就不会与man与women互斥
'''
answer_group = QButtonGroup(window)
answer_group.addButton(yes)
answer_group.addButton(no)

#给yes和no设置ID，场景是可以通过获取这个id来获取用户选择的哪一个选项
answer_group.setId(yes,1)
answer_group.setId(no,2)


#创建信号与槽获取选择的ID  （方式1）
def get_id(id):
    print(sex_group.id(id))
sex_group.buttonClicked.connect(get_id)


#创建信号与槽获取选择的ID  （方式2）
def get_id(id):
    print(id)
answer_group.buttonClicked[int].connect(get_id)

window.show()
sys.exit(app.exec())