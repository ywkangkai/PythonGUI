# 要求：一个文本框只能输入18到180之间的数字，如果不符合不会显示，当从该文本框移动出另外一个文本框时，如果不符合要求会默认给他一个返回值，

from PyQt5.Qt import *
import sys


class AgeVadidator(QValidator):

    # input_str是指你输入的文本框的内容，pos_int是指你输入几个字符光标就停留在第几个字符后，这个可以用于用户输入了多少就能判断目前输入的是否符合条件

    def validate(self, input_str, pos_int):  # validate是内置时间，当在文本框输入就会自动触发这个函数
        print(input_str,pos_int)
        try:
            if 18 <= int(input_str) <= 180:
                return (QValidator.Acceptable,input_str,pos_int)   # 符合这个范围就会显示在文本内容中
            elif 1 <= int(input_str) <= 17:
                # 当输入的小于18，但是这个时候还能在输入比如123，加上这句话就能实现中间值等待
                return (QValidator.Intermediate, input_str, pos_int)
            else:
                return (
                    QValidator.Invalid,
                    input_str,
                    pos_int)  # 不符合的在输入不会显示数字

        except BaseException:
            if len(input_str) == 0:
                return (QValidator.Invalid, input_str, pos_int)
            return (QValidator.Invalid, input_str, pos_int)

    def fixup(self, str):  # 结尾处理函数，输入完毕后，鼠标移动出输入框后，如果输入的内容不符合条件会走此函数逻辑
        print(str)   #p_str是上方的input_str
        try:
            if int(str) < 18:
                return 18
            else:
                return 180
        except BaseException:
            return 18


class MyAgeVadidator(QIntValidator):
    def fixup(self, p_str):
        if int(p_str) < 18 or len(p_str) == 0:
            return 18

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setup()

    def setup(self):
        password_line = QLineEdit(self)
        #validate = AgeVadidator()
        validate = MyAgeVadidator(18, 180)    # QIntValidator实现了控制范围的内置方法 实现过程参考上述类中的逻辑
        password_line.setValidator(validate)
        line = QLineEdit(self)
        line.move(100, 100)


app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec_())
