import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QMainWindow, QPushButton, QFileDialog,
    QLabel, QLineEdit, QComboBox, QVBoxLayout, QHBoxLayout, QRadioButton,
    QTextEdit, QStackedWidget, QSpinBox, QDoubleSpinBox, QGroupBox, QGridLayout
)
from PyQt5 import uic
from enum import Enum
 
class Gear(Enum):
    p=0
    r=1
    n=2
    d=3
    m=4
 
# === Signal Class ===
class Signal:
    def __init__(self, name, data_type):
        self.name = name
        self.data_type = data_type
 
 
# === All Signal Instances ===
signal_list = [
    Signal("speed", "integer"),
    Signal("tour", "bool"),
    Signal("temperature", "double"),
    Signal("gear", "enum"),
    Signal("high beam", "bool"),
    Signal("fuel range", "integer"),
    Signal("sport", "bool"),
    Signal("eco", "enum"),
    Signal("rpm", "integer"),
    Signal("ac_status", "bool")
]
 
# Convert to dictionary for easy access
SIGNALS = {signal.name: signal for signal in signal_list}
 
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI/mainWindow.ui",self)

        self.file_selector_btn.clicked.connect(self.open_file_dialog) #when clicked on folder select button

        self.signal_list_dropdown.addItems(SIGNALS.keys()) #adding all items to dropdown 

        self.signal_list_dropdown.currentTextChanged.connect(self.on_signal_selected) #when clicked on any item in dropdown

        #adding gear enum values  to dropdown
        for gear in Gear:
            self.signal_value_enum.addItem(gear.name)

    # function to open file dialog box
    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)")
        if file_path:
            self.file_name_container.setText(file_path)
 
    #function when an signal item is clicked:based on signal signal info 
    def on_signal_selected(self, signal_name):
        signal = SIGNALS.get(signal_name)
        if not signal:
            return
 
        self.signal_info_name.setText(signal.name)
        self.signal_info_type.setText(signal.data_type)
 
        # Switch stacked widget page based on type
        type_map = {
            "bool": 0,
            "integer": 1,
            "enum": 2,
            "double": 3
        }
        self.stackedWidget.setCurrentIndex(type_map.get(signal.data_type, 0))
    
    # def signal_dropdown_list(self,items):
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) 