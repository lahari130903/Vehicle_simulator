import sys
from PyQt5.QtWidgets import QApplication
from WindowsLogic.VehicleSimulatorWindow import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())