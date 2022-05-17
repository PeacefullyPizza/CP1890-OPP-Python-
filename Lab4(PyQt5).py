import sys

from PyQt5.QtWidgets import QApplication,QPushButton,QWidget,QLineEdit,QLabel,QGridLayout

def calculator():
    try:
        calc_number1 = int(Number1.text())
        calc_number2 = int(Number2.text())
        calc_result = calc_number1 % calc_number2
        calc_display.setText(str(calc_result))
        calc_display.setStyleSheet("font-size:30px;background-color: lightgreen;border: 1px solid black;")

    except ValueError:
        calc_display.setText('ERROR: you must enter 2 integers')
        calc_display.setStyleSheet("color: red;font-size:15px;background-color: black;border: 1px solid orange;")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Lab4')
window.resize(200,200)
# layout
layout = QGridLayout(window)
Number1 = (QLineEdit())
layout.addWidget(Number1)
Number2 = (QLineEdit())
layout.addWidget(Number2)
# Button
btn = QPushButton('Calculate')
layout.addWidget(btn)
# Results Label
result = QLabel("Result")
layout.addWidget(result)
calc_display = QLabel()
calc_display.setStyleSheet("background-color: lightgreen;border: 1px solid black;")
layout.addWidget(calc_display)
# Button Connection
btn.clicked.connect(calculator)
window.show()
#exit
sys.exit(app.exec_())