from tabnanny import check
import pygame
import numpy as np
from utils import print_layout, clear_terminal


class TicTacToe:
    def __init__(self, grid_size=3, n_dim=2):

        self.game_name = "TIC-TAC-TOE"
        self.game_over = False
        self.win = False
        self.winner = None
        self.grid_size = grid_size
        self.state = np.zeros((self.grid_size, self.grid_size))
        self.moves = []
        self.players = {}
        # call functions to intialize the game
        self.setup_display_grid()
        self.print_instruct()

    def setup_display_grid(self):
        self.grid = np.empty_like(self.state, dtype='object')
        self.grid[:, :] = " "

    def handle_input(self, inp):

        def is_win(a_sum):
            if self.win != True:
                self.win = True if (a_sum == 3 or a_sum == -3) else False
                print(self.win)
                if self.win:
                    self.winner = "X" if a_sum == 3 else "O"
                print(self.winner)
            return self.win

        def handle_error(error='value_error', inp=[]):
            clear_terminal()
            print("Wrong input !")
            if error == 'invalid_input_length':
                print(f"Expected 3 entries ! Received {len(inp)} !")
            elif error == 'invalid_in':
                print("Invalid row or column number entered !")
            elif error == 'invalid_sym':
                print(f"{inp[2]} is an invalid symbol!")
            elif error == "already":
                print("Cell already occupied !")
            else:
                print(error)
            self.print_instruct()
            return None

        def handle_move(row_in, col_in, player):
            if self.state[row_in][col_in] != 0:  # Choosing already marked cell
                handle_error("Cell already marked !")
            else:
                self.moves.append(player)
                if self.moves == []:  # If first move
                    self.players['Player1'] = player
                    self.players['Player2'] = ["X" if player == "O" else "O"]

                self.state[row_in][col_in] = 1 if player == "X" else -1
                self.grid[row_in][col_in] = player

                # check rows
                for row in range(self.grid_size):
                    is_win(np.sum(self.state[row, :]))
                # check columns
                for col in range(self.grid_size):
                    is_win(np.sum(self.state[:, col]))
                # check diagonals
                is_win(sum([self.state[i, i] for i in range(self.grid_size)]))
                is_win(sum([self.state[i, ~i] for i in range(self.grid_size)]))
            return None

        if len(inp) == 3:
            try:
                val = list(map(int, inp[:2]))
                if val[0] > self.grid_size | val[0] < 1 | val[1] > self.grid_size | val[1] < 1:
                    handle_error(error='invalid_in')
                else:
                    row_in = val[0]-1
                    col_in = val[1]-1
                    if inp[2].upper() == 'X' or inp[2].upper() == 'O':
                        handle_move(row_in, col_in, inp[2].upper())
                    else:
                        handle_error(error='invalid_sym', inp=inp)
            except ValueError:
                handle_error()
        else:
            handle_error(error='invalid_input_length', inp=inp)

    def check_gameover(self):  # check if a player won or there is a draw
        if (self.win == True) | (np.sum(self.grid == " ") == 0):
            self.game_over = True
            return True

    def print_instruct(self):
        print(" ")
        print(
            "Instructions:\n"
            "1. Enter row and column number to select a cell, for example, '2 3' \n"
            "2. In order to flag a mine, enter F after row and column numbers, example '2 3 F'")
        print()


if __name__ == "__main__":
    game = TicTacToe()

    while not game.game_over:
        # clear_terminal()
        print_layout(game.grid_size, game.grid, game.game_name)
        inp = input(
            "Enter row number followed by space and column number= ").split()

        game.handle_input(inp)
        if(game.check_gameover()):
            clear_terminal()
            print_layout(game.grid_size, game.grid, game.game_name)
            if game.win == True:
                print(f"Congratulations Player {game.winner}!!!! YOU WON !!!!")
            else:  # draw
                print("GAME OVER !!! ENDED IN A DRAW !!!")
            continue
