from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAbstractSlider的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):

        label = QLabel(self)
        label.setText("0")
        label.move(200, 200)
        label.resize(100, 30)
        # print(QAbstractSlider.__subclasses__())
        sd = QSlider(self)
        sd.move(100, 100)
        sd.valueChanged.connect(lambda val:label.setText(str(val)))
        # sd.valueChanged.connect(lambda :label.setText(str(sd.value()))) # sd.setValue(88) 会触发valueChanged信号，实际效果与上面一样

        # 设置最大值 最小值
        sd.setMaximum(100)
        sd.setMinimum(66)

        # 当前数值
        # sd.setValue(88)

        # 步长设置
        # sd.setSingleStep(5) # 按住上下键，每次变化5
        # sd.setPageStep(8) # 按住上下键，每次变化8

        # 倒立外观
        # sd.setOrientation(Qt.Horizontal)# 水平方向


        # sd.sliderMoved.connect(lambda val:print(val)) # 滑块移动时触发
        # sd.actionTriggered.connect(lambda val:print(val)) # 滑块移动时触发
        # sd.rangeChanged.connect(lambda min, max:print(min, max)) # 最大最小值变化时触发



        # 设置刻度线
        sd.setTickPosition(QSlider.TicksBothSides)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())