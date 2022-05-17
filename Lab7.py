from functools import partial
import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QPixmap, QFont, QIcon)
from PyQt5.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QMainWindow,
        QProgressBar, QPushButton, QStackedWidget, QStyleFactory, QVBoxLayout, QWidget, QComboBox, QToolBar)

class ScoreTracker(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('ScoreKeeper(Lab7)')
        self.setFixedSize(500, 650)
        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)

        # shamelessly lifted from your code, then Keiths!
        current_dir = os.path.dirname(os.path.abspath(__file__))
        styles = os.path.join(current_dir, 'score_tracker.css')
        with open(styles, 'r') as f:
            # external stylesheet
            self.setStyleSheet(f.read())

        # score display box
        score = '0'
        self.score_display = QLineEdit(score)
        self.score_display.setReadOnly(True)
        self.score_display.setAlignment(Qt.AlignCenter)
        self.score_display.setFixedWidth(100)
        
        # create Combobox  
        

        # title screen widgets, layout and labels
        self.title_screen = QWidget()
        self.title_screen.setObjectName("title_screen")
        self.title_screen_layout = QVBoxLayout()
        self.title_screen.setLayout(self.title_screen_layout)
        self.label_display = QLabel('TRACK THOSE \nSCORES!')
        self.title_screen_layout.addWidget(self.label_display)
        self.title_button = QPushButton('Start New Score Board')
        self.title_screen_layout.addWidget(self.title_button)
        
        # creating buttons
        self.create_button_layout()
    
        # score screen widgets, layout and labels
        self.score_screen = QWidget()
        self.score_screen.setObjectName("score_screen")
        self.score_screen_layout = QVBoxLayout()
        self.score_screen.setLayout(self.score_screen_layout)
        self.label_display = QLabel('LOOK AT THOSE \nSCORES!')
        self.score_screen_layout.addWidget(self.label_display)
        self.score_screen_layout.addWidget(self.button_group)
    
        # button connections
        self.title_button.clicked.connect(self.score_screen_onClick)
        
        # adding widgets to the stack
        self.stack.addWidget(self.title_screen)
        self.stack.addWidget(self.score_screen)

    def create_button_layout(self):
        self.button_group = QGroupBox()
        button_layout = QGridLayout()
        
        # increase and decrease buttons
        increase_button = QPushButton('Increase by 1')
        decrease_button = QPushButton('Decrease by 1')

        # making button text bigger
        increase_button.setStyleSheet('font-size: 20px; border: 4px solid black;')
        decrease_button.setStyleSheet('font-size: 20px; border: 4px solid black;')

        # removing border from group
        self.button_group.setStyleSheet('border: 0px;')

        # adding to layout
        button_layout.addWidget(self.score_display)
        button_layout.addWidget(increase_button)
        button_layout.addWidget(decrease_button)
        
        # connections
        increase_button.clicked.connect(self.increase_score_onClick)
        decrease_button.clicked.connect(self.decrease_score_onClick)

        # setting layout
        self.button_group.setLayout(button_layout)

    # switch to the score page
    def score_screen_onClick(self):
        self.stack.setCurrentIndex(1)
    
    def title_screen_onClick(self):
        self.stack.setCurrentIndex(0)

    # increasing displayed number
    def increase_score_onClick(self):
        score = self.score_display.text()
        score = str(int(score) + 1)
        self.score_display.setText(score)

    # decreasing displayed number, won't go below 0
    def decrease_score_onClick(self):
        score = self.score_display.text()
        if int(score) > 0:
            score = str(int(score) - 1)
        else:
            score = '0'
        self.score_display.setText(score)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widgets = ScoreTracker()
    widgets.show()
    sys.exit(app.exec_()) 