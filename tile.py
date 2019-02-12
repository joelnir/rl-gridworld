# PyQt imports
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Constants
AGENT_HEIGHT = 120
AGENT_PIC = "robot.png"

class Tile(QLabel):

    def __init__(self):
        super().__init__()

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
            background-color: #ffdf80;
            border-style: solid;
            border-color: #cccccc;
            border-width: 4px;
            }
        """)

    def update_values(self, q, reward):
        self.bottom_label.setText("q = {}\nr = {}".format(q, reward))

    def mousePressEvent(self, event):
        value, ok = QInputDialog.getDouble(self, "select", "list")

    def show_agent(self, show):
        if show:
            agent = QPixmap(AGENT_PIC).scaledToHeight(AGENT_HEIGHT)
            self.top_label.setPixmap(agent)
        else:
            self.top_label.clear()



