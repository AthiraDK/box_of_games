# https://www.askpython.com/python/examples/create-minesweeper-using-python

import numpy as np
from utils import clear_terminal


class MineSweeper:
    def __init__(self, grid_size=10, n_mines=8):
        # variables
        self.grid_size = grid_size
        if n_mines >= 1:
            self.n_mines = n_mines
        else:
            self.n_mines = int(n_mines * (self.grid_size**2))
        self.flags = []
        self.visited_cells = []
        self.game_over = False
        # call functions to intialize the game
        self.setup_mines()
        self.update_gridvals()
        self.setup_displaygrid()
        self.print_instruct()
        # self.print_layout()

    def setup_mines(self):
        import random
        # randomly setup mines in the grid
        self.state = np.zeros((self.grid_size, self.grid_size), dtype=int)
        row_ind, col_ind = np.indices((self.grid_size, self.grid_size))
        mine_rows = random.sample(list(row_ind.ravel()), self.n_mines)
        mine_cols = random.sample(list(col_ind.ravel()), self.n_mines)
        for x, y in zip(mine_rows, mine_cols):
            self.state[x][y] = -1

    def update_gridvals(self):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                if self.state[row][col] == -1:
                    continue
                # Check North
                if row > 0 and self.state[row-1][col] == -1:
                    self.state[row][col] += 1
                # Check NorthWest
                if row > 0 and col > 0 and self.state[row-1][col-1] == -1:
                    self.state[row][col] += 1
                # Check NorthEast
                if row > 0 and col < (self.grid_size-1) and self.state[row-1][col+1] == -1:
                    self.state[row][col] += 1
                # Check Left
                if col > 0 and self.state[row][col-1] == -1:
                    self.state[row][col] += 1
                # Check Right
                if col < (self.grid_size-1) and self.state[row][col+1] == -1:
                    self.state[row][col] += 1
                # Check South
                if row < (self.grid_size-1) and self.state[row+1][col] == -1:
                    self.state[row][col] += 1
                # Check SouthWest
                if row < (self.grid_size-1) and col > 0 and self.state[row+1][col-1] == -1:
                    self.state[row][col] += 1
                # Check SouthEast
                if row < (self.grid_size-1) and col < (self.grid_size-1) and self.state[row+1][col+1] == -1:
                    self.state[row][col] += 1
        return self

    def setup_displaygrid(self):
        self.grid = np.empty_like(self.state, dtype='object')
        # self.grid[self.state == 1] = "M"
        # self.grid[self.state == 0] = " "
        self.grid[:, :] = " "

    def check_gameover(self):
        count = np.sum(self.grid != " ") - np.sum(self.grid == "F")
        print(count, (self.grid_size)**2 - self.n_mines)
        if count == (self.grid_size)**2 - self.n_mines:
            return True
        else:
            return False

    def handle_input(self, inp):

        def handle_standard():
            if self.state[row_in][col_in] == -1:  # GAME OVER
                self.grid[row_in][col_in] = 'M'
                self.show_mines()
                self.print_layout()
                print("Landed on a mine ! GAME OVER !!!")
                self.game_over = True
            elif self.state[row_in][col_in] == 0:
                self.grid[row_in][col_in] = '0'
                self.expose_neighbours(row_in, col_in)
            else:
                self.grid[row_in][col_in] = str(self.state[row_in][col_in])
            return True

        def handle_flag():
            if [row_in, col_in] in self.flags:  # already flagged
                # clear_terminal()
                print("Flag already set!")
                return False
            if self.grid[row_in][col_in] != ' ':  # Cell value already displayed
                # clear_terminal()
                print("Value already known!")
                return False
            if len(self.flags) < self.n_mines:
                # clear_terminal()
                self.flags.append([row_in, col_in])
                self.grid[row_in][col_in] = 'F'
                print("Flag set")
                return True
            else:
                # clear_terminal()
                print("Flags finished !")
                return None

        def handle_error(error='value_error', inp=[]):
            clear_terminal()
            print("Wrong input !")
            if error == 'invalid_input_length':
                print(f"Expected 2 or 3 entries ! Received {len(inp)} !")
            elif error == 'invalid_in':
                print("Invalid row or column number entered !")
            self.print_instruct()
            return None

        isflag = False
        if (len(inp) == 2) | (len(inp) == 3):  # Valid input lengths
            if (len(inp) == 3):  # Flagging mine
                if inp[2].lower() != 'f':
                    handle_error()
                else:
                    isflag = True
            try:
                val = list(map(int, inp[:2]))
                if val[0] > self.grid_size | val[0] < 1 | val[1] > self.grid_size | val[1] < 1:
                    handle_error(error='invalid_in')
                else:
                    row_in = val[0]-1
                    col_in = val[1]-1
                if isflag:
                    handled = handle_flag()  # Handle flagging input
                else:
                    handled = handle_standard()  # Handle standard_input
            except ValueError:
                handle_error()
        else:
            handle_error(error='invalid_input_length', inp=inp)

    def expose_neighbours(self, row, col):
        if [row, col] not in self.visited_cells:  # cell not already visited
            self.visited_cells.append([row, col])  # Mark as visited

            if self.state[row, col] == 0:  # cell is zero-valued
                # display it, as string/int?
                self.grid[row, col] = str(self.state[row, col])
                # Now, do recursion until we find a non-zero cell in the neighbourhood

                # Check North
                if row > 0:
                    self.expose_neighbours(row-1, col)
                # Check Left
                if col > 0:
                    self.expose_neighbours(row, col-1)
                # Check Right
                if col < (self.grid_size-1):
                    self.expose_neighbours(row, col+1)
                # Check South
                if row < (self.grid_size-1):
                    self.expose_neighbours(row+1, col)
                # Check NorthWest
                if row > 0 and col > 0:
                    self.expose_neighbours(row-1, col-1)
                # Check NorthEast
                if row > 0 and col < (self.grid_size-1):
                    self.expose_neighbours(row-1, col+1)
                # Check SouthWest
                if row < (self.grid_size-1) and col > 0:
                    self.expose_neighbours(row+1, col-1)
                # Check SouthEast
                if row < (self.grid_size-1) and col < (self.grid_size-1):
                    self.expose_neighbours(row+1, col+1)

            elif self.state[row][col] != 0:
                self.grid[row][col] = str(self.state[row][col])

    def show_mines(self):
        self.grid[self.state == -1] = 'M'

    def print_instruct(self):
        print(" ")
        print(
            "Instructions:\n"
            "1. Enter row and column number to select a cell, for example, '2 3' \n"
            "2. In order to flag a mine, enter F after row and column numbers, example '2 3 F'")
        print()

    def print_layout(self):
        # printing minesweeper layout

        gap = int(((4 + 6*self.grid_size) - 12)/2)
        print()
        title = ""
        for i in range(gap*2):
            if i == gap+1:
                title += "MINESWEEPER"
            else:
                title += " "
        print(title)
        print()

        cell_col = "    "
        for col in range(self.grid_size):
            if col < 9:
                cell_col += "  " + str(col+1) + "   "
            else:
                cell_col += " " + str(col+1) + "   "
        print(cell_col)

        cell_upp = "   "
        for col in range(self.grid_size):
            cell_upp += "______"
        print(cell_upp)

        cell_u = "   "
        for col in range(self.grid_size):
            cell_u += "|     "
        cell_u += '|'

        cell_d = "   "
        for col in range(self.grid_size):
            cell_d += "|_____"
        cell_d += '|'

        for row in range(self.grid_size):
            print(cell_u)
            if row < 9:
                cell_m = str(row + 1) + '  |'
            else:
                cell_m = str(row + 1) + ' |'
            for col in range(self.grid_size):
                # cell_m += "  " + str(self.state[row][col]) + "  |"
                cell_m += "  " + self.grid[row][col] + "  |"
            print(cell_m)
            print(cell_d)
        print()

# class MineSweeperGUI:
#     def __init__(self):
#         pass


if __name__ == "__main__":
    ms_game = MineSweeper(grid_size=8, n_mines=0.2)

    # The Game Loop
    while not ms_game.game_over:
        clear_terminal()
        ms_game.print_layout()
        inp = input(
            "Enter row number followed by space and column number= ").split()

        ms_game.handle_input(inp)

        if(ms_game.check_gameover()):
            ms_game.show_mines()
            ms_game.print_layout()
            print("Congratulations !!!! YOU WIN !!!!")
            ms_game.game_over = True
            continue

        # else:
        #     clear_terminal()
