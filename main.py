# PyQt imports
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Project imports
from tile_grid import TileGrid
from grid_world import GridWorld

# Constants
WINDOW_TITLE = "RL Sandbox"

class RLWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(WINDOW_TITLE)

        # World
        world = GridWorld()
        tile_grid = TileGrid(world)
        self.setCentralWidget(tile_grid)

        # Toolbar
        self.toolbar = self.addToolBar("tb1")

        run_action = QAction("Run", self)
        self.toolbar.addAction(run_action)


        step_action = QAction("Step", self)
        step_action .triggered.connect(world.step)
        self.toolbar.addAction(step_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(qApp.quit)
        self.toolbar.addAction(exit_action)

        self.show()

def main():
    app = QApplication([])
    w = RLWidget()
    app.exec_()

if __name__=="__main__":
    main()

