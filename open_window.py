import sys
from PyQt5.QtWidgets import *
    
class MyWindow(QMainWindow):
         
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        self.setGeometry(1000, 100, 900, 900)
        
        btn1 = QPushButton("24시간 이내", self)
        btn1.move(30, 120)
        btn1.clicked.connect(self.btn_fun1)
        btn2 = QPushButton("24시간 이상", self)
        btn2.move(30, 240)
        btn2.clicked.connect(self.btn_fun2)

    def btn_fun1(self):
        print("button1 is clicked")
    def btn_fun2(self):
        print("button2 is clicked")
       
       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()

    app.exec_()