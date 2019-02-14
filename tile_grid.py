# PyQt imports
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Project imports
from tile import Tile
from constants import *

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
                tile = Tile((lambda f=self.tile_click, y=y, x=x: f(y, x)))
                self.grid.addWidget(tile, y, x)
                row.append(tile)
            self.tiles.append(row)

        self.repaint()

    def tile_click(self, y, x):
        if self.grid_world.is_placing():
            self.grid_world.set_start_pos(y, x)
            self.grid_world.set_placing(False)

        else:
            value, ok = QInputDialog.getDouble(self, "Set Reward", "Set Reward",
                    self.grid_world.get_reward(y, x), MIN_REWARD, MAX_REWARD, DECIMALS)

            if ok:
                self.grid_world.update_reward(value, y, x)

    def repaint(self):
        agent_pos = self.grid_world.get_position()
        max_value = self.grid_world.get_max_value()
        min_value = self.grid_world.get_min_value()

        for y in range(self.grid_h):
            for x in range(self.grid_w):
                # Values
                value = self.grid_world.get_value(y, x)
                reward = self.grid_world.get_reward(y, x)
                self.tiles[y][x].update_values(value, reward)

                # Color
                if(value < 0):
                    if min_value == 0:
                        non_red = 255
                    else:
                        non_red = 255 * (1 - (value/min_value))

                    color = "rgb(255, {}, {})".format(non_red, non_red)
                else:
                    if max_value == 0:
                        non_green = 255
                    else:
                        non_green = 255 * (1 - (value/max_value))

                    color = "rgb({}, 255, {})".format(non_green, non_green)
                self.tiles[y][x].set_color(color)

                # Agent
                self.tiles[y][x].show_agent((agent_pos == (y, x)))

