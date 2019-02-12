# PyQt imports
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Project imports
from tile import Tile

# Constants
WINDOW_TITLE = "RL Sandbox"

TILE_W = 6
TILE_H = 4

class RLWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(WINDOW_TITLE)

        # Toolbar
        self.toolbar = self.addToolBar("tb1")

        run_action = QAction("Run", self)
        self.toolbar.addAction(run_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(qApp.quit)
        self.toolbar.addAction(exit_action)

        # Layout
        tile_area = QWidget()
        self.setCentralWidget(tile_area)

        grid = QGridLayout()
        tile_area.setLayout(grid)

        for i in range(TILE_H):
            for j in range(TILE_W):
                tile = Tile()
                grid.addWidget(tile, i, j)

        self.show()

def main():
    app = QApplication([])
    w = RLWidget()
    app.exec_()

if __name__=="__main__":
    main()

