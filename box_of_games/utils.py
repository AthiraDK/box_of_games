

def get_colormap(filepath='/home/athira/Code_Mania/Games/colors.yaml'):
    import yaml
    with open(filepath, 'r') as yaml_file:
        color_map = yaml.safe_load(yaml_file)
    return color_map['COLORS']


def clear_terminal():
    import os
    os.system('clear')
