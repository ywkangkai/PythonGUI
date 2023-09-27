from PyQt5.Qt import *
from login_ui import Ui_Form

class Login_Pane(QWidget, Ui_Form):
    show_register_pane_signal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True) #写了这句话背景图片才能显示
        self.setupUi(self)

    def show_register_pane(self):
        self.show_register_pane_signal.emit()

    def open_link(self):
        url = 'https://docs.qq.com/doc/DV1NoWG1RdFd2V1Jo'
        QDesktopServices.openUrl(QUrl(url))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Login_Pane()
    window.show()
    sys.exit(app.exec_())
