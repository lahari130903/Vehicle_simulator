from enum import Enum

# class 
class Signal():
    pass


if __name__ == "__main__":
    s1=Signal()
    s1.data = 20
    s1.dataType = 30

    s2=Signal()
    s2.value="something"
    s2.units=Enum('drivemode',{'P':0})


    print(s1.data)
    print(s1.dataType)
    print(s2.value)
    print(type(s2.units))
    # app = QApplication(sys.argv)
    # win = MainWindow()
    # win.show()
    # sys.exit(app.exec_())