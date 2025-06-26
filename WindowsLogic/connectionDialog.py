from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

class ConnectionDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI/connectionDialogBox.ui", self)

    def get_values(self):
        return self.ip_input.text(), self.port_input.text()