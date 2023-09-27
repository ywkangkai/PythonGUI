from login_pane import Login_Pane
from Register_Pane import Register_Pane
from PyQt5.Qt import *


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    login_pane = Login_Pane()
    register_pane = Register_Pane(login_pane)
    register_pane.move(0, login_pane.height()) # 一开始就把注册窗口放在登录窗口下面
    register_pane.show()
    def show_register_pane():
        animation = QPropertyAnimation(register_pane)
        animation.setTargetObject(register_pane)
        animation.setPropertyName(b'pos')
        animation.setStartValue(register_pane.pos())
        animation.setEndValue(QPoint(0, 0))
        animation.setDuration(1000)
        animation.start(QAbstractAnimation.DeleteWhenStopped)
    def hide_register_pane():
        animation = QPropertyAnimation(register_pane)
        animation.setTargetObject(register_pane)
        animation.setPropertyName(b'pos')
        animation.setEndValue(QPoint(0, login_pane.height()))
        animation.setDuration(1000)
        animation.start(QAbstractAnimation.DeleteWhenStopped)


    login_pane.show_register_pane_signal.connect(show_register_pane)
    register_pane.exit_signal.connect(hide_register_pane)
    login_pane.show()
    sys.exit(app.exec_())
