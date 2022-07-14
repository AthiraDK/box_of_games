import pygame
import numpy as np
from utils import print_layout


class Chess:
    def __init__(self, grid_size=8):

        self.game_name = "Chess"
        self.grid_size = grid_size
        self.dict_pieces = self.get_pieces()
        self.initialize()
        print_layout(self.grid_size, self.grid, self.game_name)

    def initialize(self):
        self.state = np.zeros((self.grid_size, self.grid_size))
        self.grid = np.empty_like(self.state, dtype='object')
        self.grid[:, :] = " "
        self.grid[3, 1:2:8] = self.dict_pieces['b_checker']
        self.grid[1, :] = self.dict_pieces['b_pawn']
        self.grid[6, :] = self.dict_pieces['w_pawn']

    def get_pieces(self):
        chrs = {
            'b_checker': u'\u25FB',
            'b_pawn': u'\u265F',
            'b_rook': u'\u265C',
            'b_knight': u'\u265E',
            'b_bishop': u'\u265D',
            'b_king': u'\u265A',
            'b_queen': u'\u265B',
            'w_checker': u'\u25FC',
            'w_pawn': u'\u2659',
            'w_rook': u'\u2656',
            'w_knight': u'\u2658',
            'w_bishop': u'\u2657',
            'w_king': u'\u2654',
            'w_queen': u'\u2655'
        }
        return chrs

    def update(self):
        pass


if __name__ == "__main__":
    chess_game = Chess()
