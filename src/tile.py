# PyQt imports
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from constants import *

class Tile(QLabel):

    def __init__(self, click_callback):
        super().__init__()

        self.click_callback = click_callback

        grid = QGridLayout()
        self.setLayout(grid)

        self.top_label = QLabel()
        self.bottom_label = QLabel()
        grid.addWidget(self.top_label, 0, 0)
        grid.addWidget(self.bottom_label, 1, 0)

        self.top_label.setAlignment(Qt.AlignCenter)
        self.bottom_label.setAlignment(Qt.AlignCenter)

        self.setStyleSheet("""
            .Tile{
            background-color: #ffffff;
            border-style: solid;
            border-color: #cccccc;
            border-width: 4px;
            }
        """)

    def update_values(self, value, reward):
        self.bottom_label.setText("V = {:.4f}\nr = {:.4f}".format(value, reward))

    def set_color(self, color):
        self.setStyleSheet("background-color: {}".format(color))

    def mousePressEvent(self, event):
        self.click_callback()

    def show_agent(self, show):
        if show:
            agent = QPixmap(AGENT_PIC).scaledToHeight(AGENT_HEIGHT)
            self.top_label.setPixmap(agent)
        else:
            self.top_label.clear()



