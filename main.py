# PyQt imports
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Project imports
from tile_grid import TileGrid
from grid_world import GridWorld
from rl_menu import RLMenu
from constants import *

class RLWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui(DEFAULT_H, DEFAULT_W)

    def init_ui(self, height, width):
        self.setWindowTitle(WINDOW_TITLE)

        component_layout = QGridLayout()
        central_widget = QWidget()
        central_widget.setLayout(component_layout)
        self.setCentralWidget(central_widget)

        # World
        grid_world = GridWorld(height, width)
        tile_grid = TileGrid(grid_world)
        component_layout.addWidget(tile_grid, 0,1,1,3)

        # Menu
        menu = RLMenu(grid_world, (lambda h, w, f=self.init_ui: f(h,w)))
        menu.setFixedSize(MENU_WIDTH, QWIDGETSIZE_MAX)
        component_layout.addWidget(menu,0,0,1,1)

        self.show()

def main():
    app = QApplication([])
    w = RLWidget()
    app.exec_()

if __name__=="__main__":
    main()

