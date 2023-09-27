from PyQt5.Qt import *
from register_ui import Ui_Form

class Register_Pane(QWidget, Ui_Form):
    exit_signal = pyqtSignal()
    register_account_signal = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True) # 写了这句话背景图片才能显示
        self.setupUi(self)
        self.animation_targets = [self.about_menue_btn, self.reset_menue_btn, self.exit_menue_btn]
        self.animation_targets_pos = [target.pos() for target in self.animation_targets]

    def show_hide_menue(self, checked):

        # 动画组
        animation_group = QSequentialAnimationGroup(self)
        for idx, target in enumerate(self.animation_targets):
            anition =QPropertyAnimation()
            anition.setTargetObject(target)
            anition.setPropertyName(b'pos')
            if not checked:
                anition.setStartValue(self.main_menue_btn.pos())
                anition.setEndValue(self.animation_targets_pos[idx])
            else:
                anition.setEndValue(self.main_menue_btn.pos())
                anition.setStartValue(self.animation_targets_pos[idx])
            anition.setDuration(500)
            # anition.setEasingCurve(QEasingCurve.OutInBounce) # 弹簧效果
            animation_group.addAnimation(anition)
        animation_group.start(QAbstractAnimation.DeleteWhenStopped)


    def about(self):
        pass

    def reset(self):
        self.account.clear()
        self.password.clear()
        self.confim_pwd.clear()

    def exit_pane(self):
        self.exit_signal.emit()

    def check_register(self):
        self.register_account_signal.emit(self.account.text(), self.password.text())

    def enable_gister_btn(self):
        account = self.account.text()
        password = self.password.text()
        confirm_pwd = self.confim_pwd.text()
        if len(account) > 0 and len(password) > 0 and len(confirm_pwd) > 0:
            if password == confirm_pwd:
                self.register_btn.setEnabled(True)
            else:
                self.register_btn.setEnabled(False)
        else:
            self.register_btn.setEnabled(False)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Register_Pane()
    window.exit_signal.connect(lambda: print('exit'))
    window.register_account_signal.connect(lambda account, password: print(account, password))
    window.show()
    sys.exit(app.exec_())
