# PyQt imports
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Tile(QLabel):

    def __init__(self):
        super().__init__()

        self.real_value = 0.0
        self.q = 0.0

        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
            background-color: #6699ff;
            border-style: solid;
            border-color: #000066;
            border-width: 4px;

        """)

        self.repaint()

    def repaint(self):
        self.setText(str(self.real_value) + "\n" + "("+str(self.q)+")")

    def update_value(self, new_value):
        self.real_value = new_value
        self.repaint()

    def update_q(self, new_q):
        self.q = new_q
        self.repaint()

    def mousePressEvent(self, event):
        value, ok = QInputDialog.getDouble(self, "select", "list")

        if ok:
            self.update_value(value)


