import pygame
import numpy as np
from utils import print_layout


class TicTacToe:
    def __init__(self, grid_size=3, n_dim=2):

        self.game_name = "TIC-TAC-TOE"
        self.grid_size = grid_size
        self.state = np.zeros((self.grid_size, self.grid_size))
        self.grid = np.empty_like(self.state, dtype='object')
        self.grid[:, :] = ' '
        self.grid[0, :] = 'X'
        self.grid[1, :] = 'O'

        print_layout(self.grid_size, self.grid, self.game_name)

    def update(self):
        pass


if __name__ == "__main__":
    ttt = TicTacToe(grid_size=5)
