# PyQt imports
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Project imports
from tile import Tile

class TileGrid(QWidget):

    def __init__(self, grid_world):
        super().__init__()
        self.grid_world = grid_world
        grid_world.add_observer(self)

        # Set up Qt elements
        self.grid_h, self.grid_w = grid_world.get_size()
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.tiles = []
        for y in range(self.grid_h):
            row = []
            for x in range(self.grid_w):
                tile = Tile()
                self.grid.addWidget(tile, y, x)
                row.append(tile)
            self.tiles.append(row)


        self.repaint()

    def repaint(self):
        agent_pos = self.grid_world.get_position()

        for y in range(self.grid_h):
            for x in range(self.grid_w):
                q = self.grid_world.get_q(x, y)
                reward = self.grid_world.get_reward(x, y)
                self.tiles[y][x].update_values(q, reward)
                self.tiles[y][x].show_agent((agent_pos == (y,x)))

