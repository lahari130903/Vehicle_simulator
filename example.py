import sys
import pandas as pd
from PyQt5 import QtWidgets,uic
# from sample2.ui import Ui_MainWindow  # this comes from main_ui.py

class SignalApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("sample2.ui", self)
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)

        # Load the signal data from CSV
        self.df = pd.read_csv("samples.csv")  # or use read_excel for .xlsx

        # Populate the list widget
        signal_names = self.df["Signalname"].tolist()
        self.Signallist.addItems(signal_names)

        # Hide radio buttons initially
        # self.radioTrue.setVisible(False)
        # self.radioFalse.setVisible(False)

        # Connect list selection event
        self.Signallist.currentItemChanged.connect(self.on_signal_selected)

    def on_signal_selected(self, current, previous):
        if not current:
            return

        signal_name = current.text()
        
        row = self.df[self.df["Signalname"] == signal_name].iloc[0]
        signal_type = row["Datatype"].strip().lower()
        
        

        if signal_type == "boolean":
            print(signal_name)
            print(signal_type)
            
            self.stackedWidget.setCurrentIndex(2)
            self.label.setText(signal_name)
            self.label_2.setText(signal_type)
            # self.label_4.setText(signal_name)
            # self.label_3.setText(signal_type)
            # self.labelDesc.setText(f"Description: {row['Signal Description']}")
            # self.radioTrue.setVisible(True)
            # self.radioFalse.setVisible(True)
        else:
            print("int")
            
            self.stackedWidget.setCurrentIndex(0)
            self.label_4.setText(signal_name)
            self.label_3.setText(signal_type)

            
            # self.labelDesc.setText(f"'{signal_name}' is not a boolean signal.")
            # self.radioTrue.setVisible(False)
            # self.radioFalse.setVisible(False)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SignalApp()
    window.show()
    sys.exit(app.exec_())
