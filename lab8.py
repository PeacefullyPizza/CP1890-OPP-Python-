from functools import partial
import lab8_resources
import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QPixmap, QFont, QIcon)
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QMainWindow,
        QProgressBar, QPushButton, QToolBar, QStatusBar, QStackedWidget, QStyleFactory, QFormLayout, QVBoxLayout, QWidget)

class ScoreTracker(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Lab8 - Score Keeper v.2')
        width = 550
        height = 700

        # setting  the fixed width of window
        self.setFixedWidth(width)

        # setting  the fixed width of window
        self.setFixedHeight(height)

        # creating stacked widgets
        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)

        # creating title
        self.create_titleScreen()
        self.create_scoreScreen()

        # shamelessly lifted from your code
        current_dir = os.path.dirname(os.path.abspath(__file__))
        styles = os.path.join(current_dir, 'score_tracker.css')
        with open(styles, 'r') as f:
            # external stylesheet
            self.setStyleSheet(f.read())

        # adding widgets to the stack
        self.stack.addWidget(self.title_screen)
        self.stack.addWidget(self.score_screen)

        # creating menu
        self._create_menu()

    def create_scoreScreen(self):
        # score screen picture
        self.score_header = QLabel()
        self.screen_image = QPixmap('pug2.png')
        self.screen_image.scaledToWidth(0)
        self.score_header.setPixmap(self.screen_image)

        # score screen widgets, layout and labels
        self.score_screen = QWidget()
        self.score_screen.setObjectName("score_screen")
        self.score_screen_layout = QFormLayout()
        self.score_screen.setLayout(self.score_screen_layout)
        self.score_screen_layout.addWidget(self.score_header)
        self.score_label = QLineEdit('*Enter players names*')
        self.score_screen_layout.addWidget(self.score_label)

    def create_titleScreen(self):
        # title screen picture
        self.header = QLabel()
        self.title_image = QPixmap('pug.png')
        self.title_image.scaledToWidth(15)
        self.header.setPixmap(self.title_image)

        # combo box
        self.player_no = QComboBox()
        self.players = ['1','2','3','4']
        self.player_no.addItems(self.players)
        self.player_boxLabel = QLabel('How many players are there?\nSelect Number of Players From Menu\n(1-4):')
        self.player_boxLabel.setObjectName('cbox_label')
        self.player_boxLabel.setBuddy(self.player_no)

        # title screen widgets, layout and labels
        self.title_screen = QWidget()
        self.title_screen.setObjectName("title_screen")
        self.title_screen_layout = QVBoxLayout()
        self.title_screen.setLayout(self.title_screen_layout)
        self.title_screen_layout.addWidget(self.header)
        self.title_screen_layout.addWidget(self.player_boxLabel)
        self.title_screen_layout.addWidget(self.player_no)
        self.title_button = QPushButton('Create New Score Board')
        self.title_screen_layout.addWidget(self.title_button)

        # button connections
        self.title_button.clicked.connect(self.score_screen_onClick)
        self.title_button.clicked.connect(self._create_players)
    
    def _create_players(self):
        number_of_players = self.player_no.currentText()
        self.holding_list = []

        for i in range(int(number_of_players)):
            self.holding_list.append(Player())
            
        for j in range(int(number_of_players)):
            self.score_screen_layout.addWidget(self.holding_list[j].button_group)
        
              
    # function to switch to the score page
    def score_screen_onClick(self):
        self.stack.setCurrentIndex(1)
    
    def _create_menu(self): 
        """ creating menu """
        self.menu = self.menuBar().addMenu('&Menu')
        self.help = self.menuBar().addMenu('&Help')
        
        self.menu.addAction('&Exit', self.close)
        self.help.addAction('&About', self.display_about)

    def display_about(self):
        """ about section in the menu"""
        about = QDialog(self) 
        layout = QVBoxLayout()
        about_label = QLabel('Score keeper for keeping...scores \n\n\n\n\t\t Dylan Owens - CNA OOP Python 1890 ')
        layout.addWidget(about_label)
        about.setLayout(layout)
        about.exec()

class Player:
    """ player class to create player score keeping objects within the scorekeeper app"""
    def __init__(self):
        self.create_playerboard()
          
    def create_playerboard(self):
        """ creating playerboard"""
        self.button_group = QGroupBox()
        self.button_layout = QHBoxLayout()

        # score display box
        score = '0'
        self.score_display = QLineEdit(score)
        self.score_display.setReadOnly(True)
        self.score_display.setAlignment(Qt.AlignCenter)
        self.score_display.setFixedWidth(75)

        # increase and decrease buttons
        self.increase_button = QPushButton('Increase Score')
        self.decrease_button = QPushButton('Decrease Score')

        # making button text bigger
        self.increase_button.setStyleSheet('font-size: 20px; border: 2px solid black;')
        self.decrease_button.setStyleSheet('font-size: 20px; border: 2px solid black;')

        # removing border from group
        self.button_group.setStyleSheet('border: 0px;')

        # connections
        self.increase_button.clicked.connect(self.increase_score_onClick)
        self.decrease_button.clicked.connect(self.decrease_score_onClick)

        # adding to layout
        self.button_layout.addWidget(self.decrease_button)
        self.button_layout.addWidget(self.score_display)
        self.button_layout.addWidget(self.increase_button)

        # setting layout
        self.button_group.setLayout(self.button_layout)

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
