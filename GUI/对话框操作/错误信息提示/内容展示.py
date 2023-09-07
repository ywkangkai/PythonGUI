from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        em = QMessageBox(self)
        em.setWindowTitle('消息提示')
        em.setIconPixmap(QPixmap('xxx.png').scaled(50, 50))
        em.setText('具体提示的内容')
        em.setInformativeText('详细的提示内容')
        em.setCheckBox(QCheckBox('不再提示', em))
        em.setDetailedText('详细的描述信息') # 详细的描述信息
        em.addButton(QPushButton('yes', em), QMessageBox.YesRole) # 添加按钮 QMessageBox.YesRole: 代表是yes按钮
        em.addButton(QPushButton('no', em), QMessageBox.NoRole) # 添加按钮 QMessageBox.NoRole: 代表是no按钮
        # em.removeButton(em.button(QMessageBox.NoRole)) # 移除按钮

        em.open()
        def btn_button(btn):
            role = em.buttonRole(btn)
            if role == QMessageBox.YesRole:
                print('yes')
            elif role == QMessageBox.NoRole:
                print('no')

        em.buttonClicked.connect(btn_button)
        # 点击YesRole按钮时触发
        # em.buttonClicked.connect(lambda btn: print(btn.text()))
        # 点击NoRole按钮时触发
        # em.buttonClicked.connect(lambda btn: print(no.text()))

app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
