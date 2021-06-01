from PyQt5.Qt import *
import sys



app = QApplication(sys.argv)
window = QWidget()
window.resize(500 ,500)
pixmao = QPixmap('xxx.png')
new_pixmao = pixmao.scaled(50, 50)  #如果不传参数，图片就是原图大小
cursor = QCursor(new_pixmao)
window.setCursor(cursor)



window.show()
sys.exit(app.exec())