import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
 
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("sample2.ui", self)
 
        # self.pushButton.clicked.connect(self.function_Sample)
   
    def function_Sample():
        print("HI")
   
 
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())