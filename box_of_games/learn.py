import pygame
import numpy as np

# drawing the grid
class GameGrid:
    def __init__(self, n_rows = 10, n_cols=10, width=20, height=20, margin=5):

        self.width = width
        self.height = height
        self.margin = margin

        self.n_rows = n_rows
        self.n_cols = n_cols

        self.initialize()

    def initialize(self, type='empty'):
        self.data_array = np.zeros(self.n_rows, self.n_cols)

    def update_state(self):
        # program logic here
        pass

    def display_grid(self, window_size=(255,255), caption="My Game"):
        pygame.init()
        window = pygame.display.set_mode(window_size)
        pygame.display.set_caption(caption)
        clock = pygame.time.Clock()

        flag = True
        while flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag = False
                else:
                    print('Testing ! ')
