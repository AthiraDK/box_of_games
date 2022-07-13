

def get_colormap(filepath='/home/athira/Code_Mania/Games/colors.yaml'):
    import yaml
    with open(filepath, 'r') as yaml_file:
        color_map = yaml.safe_load(yaml_file)
    return color_map['COLORS']


def clear_terminal():
    import os
    os.system('clear')


def logger():
    # log time, duration, metadata and results of games played for future reference
    pass


def print_layout(grid_size, grid, game_name):
    # printing minesweeper layout

    gap = int(((4 + 6*grid_size) - 12)/2)
    print()
    title = ""
    for i in range(gap*2):
        if i == gap+1:
            title += game_name
        else:
            title += " "
    print(title)
    print()

    cell_col = "    "
    for col in range(grid_size):
        if col < 9:
            cell_col += "  " + str(col+1) + "   "
        else:
            cell_col += " " + str(col+1) + "   "
    print(cell_col)

    cell_upp = "   "
    for col in range(grid_size):
        cell_upp += "______"
    print(cell_upp)

    cell_u = "   "
    for col in range(grid_size):
        cell_u += "|     "
    cell_u += '|'

    cell_d = "   "
    for col in range(grid_size):
        cell_d += "|_____"
    cell_d += '|'

    for row in range(grid_size):
        print(cell_u)
        if row < 9:
            cell_m = str(row + 1) + '  |'
        else:
            cell_m = str(row + 1) + ' |'
        for col in range(grid_size):
            # cell_m += "  " + str(state[row][col]) + "  |"
            cell_m += "  " + grid[row][col] + "  |"
        print(cell_m)
        print(cell_d)
    print()
