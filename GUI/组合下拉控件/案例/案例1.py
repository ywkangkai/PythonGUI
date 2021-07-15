from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.city_dict = {
            '北京':{
                '东城':'001',
                '西城':'002'
            },
            '上海':{
                '浦东':'003',
                '松江':'004'
            }
        }
        self.setup_ui()

    def setup_ui(self):
        pro = QComboBox(self)
        pro.move(100, 100)
        self.city = QComboBox(self)
        self.city.move(200, 100)
        #监听省下拉列表里面的当前值发生改变的信号
        pro.currentTextChanged[str].connect(self.pro_changed)

        #监听城市下拉列表里面的当前值发生改变的信号
        self.city.currentIndexChanged[int].connect(self.city_changed)

        pro.addItems(self.city_dict.keys())

    def pro_changed(self,pro_name):
        print(pro_name)
        citys = self.city_dict[pro_name]
        self.city.clear()  # 如果不加clear城市选项会被追加
        #self.city.addItems(citys.keys())
        for key,value in citys.items():
            self.city.addItem(key, value)

    def city_changed(self,city_index):
        #print(city_index)  值为-1
        if city_index != -1:  # 这里不做判断会打印none
            print(self.city.itemData(city_index))


app = QApplication(sys.argv)
window = Window()









window.show()
sys.exit(app.exec_())
