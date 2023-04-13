import sys
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication, QVBoxLayout, QHBoxLayout, QDialog, QComboBox, QLabel)

class Form(QDialog):

    def __init__(self):
        super().__init__()

        # Window title and fixed size
        self.setWindowTitle("f2c")
        self.setFixedSize(400, 200)

        # Widgets
        self.edit = QLineEdit()
        self.edit.setFixedWidth(150)
        self.combobox = QComboBox()
        self.combobox.addItems(["\U000000B0F to \U000000B0C",
                                "inch to centimetre",
                                "foot to centimetre",
                                "yard to metre",
                                "mile to kilometre",
                                "ounce to gram",
                                "pound to kilogram",
                                "fluid ounce to millilitre",
                                "quart to litre",
                                "gallon to litre"])
        self.button = QPushButton("Convert")
        self.label = QLabel()
        
        # Layout
        layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.edit)
        top_layout.addWidget(self.combobox)
        top_layout.addWidget(self.button)
        layout.addLayout(top_layout)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Connecting Signals to Slot
        self.button.clicked.connect(self.convert)
        self.combobox.currentIndexChanged.connect(self.convert)

    # Convert from imperial units to metric units
    def convert(self):
        try:
            conversion_type = str(self.combobox.currentText())
            if conversion_type == "\U000000B0F to \U000000B0C":
                result = "{:.2f}".format((float(self.edit.text()) - 32) * (5 / 9)) + " \U000000B0C (2d.p.)"
                self.label.setText(result)
            elif conversion_type == "inch to centimetre":
                result = "{:.2f}".format(float(self.edit.text()) * 2.54) + " cm (2d.p.)"
                self.label.setText(result)
            elif conversion_type == "foot to centimetre":
                result = "{:.2f}".format(float(self.edit.text()) * 30.48) + " cm (2d.p.)"
                self.label.setText(result)
            elif conversion_type == "yard to metre":
                result = "{:.2f}".format(float(self.edit.text()) / 1.094) + " m (2d.p.)"
                self.label.setText(result)
            elif conversion_type == "mile to kilometre":
                result = "{:.2f}".format(float(self.edit.text()) * 1.609) + " km (2d.p.)"
                self.label.setText(result)
            elif conversion_type == "ounce to gram":
                result = "{:.2f}".format(float(self.edit.text()) * 28.35) + " g (2d.p.)"
                self.label.setText(result)
            elif conversion_type == "pound to kilogram":
                result = "{:.2f}".format(float(self.edit.text()) / 2.205) + " kg (2d.p.)"
                self.label.setText(result)
            elif conversion_type == "fluid ounce to millilitre":
                result = "{:.2f}".format(float(self.edit.text()) * 29.574) + " ml (2d.p.)"
                self.label.setText(result)
            elif conversion_type == "quart to litre":
                result = "{:.2f}".format(float(self.edit.text()) / 1.057) + " l (2d.p.)"
                self.label.setText(result)
            elif conversion_type == "gallon to litre":
                result = "{:.2f}".format(float(self.edit.text()) * 3.785) + " l (2d.p.)"
                self.label.setText(result)
        
        except ValueError:
            self.label.setText("Invalid input value! Enter a number!")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = Form()
    form.show()
    
    sys.exit(app.exec())
