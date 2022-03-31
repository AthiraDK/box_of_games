from tkinter import LEFT
import pygame
import numpy as np
from utils import get_colormap
# drawing the grid


class GameGrid:
    def __init__(self, n_rows=10, n_cols=10, width=20, height=20, margin=5):

        self.width = width
        self.height = height
        self.margin = margin

        self.n_rows = n_rows
        self.n_cols = n_cols

        self.initialize()
        self.display_grid()

    def initialize(self, type='empty'):
        self.data_array = np.zeros((self.n_rows, self.n_cols))

    def update_state(self):
        # program logic here
        pass

    def mouse_to_grid(self, mouse_pos):
        i_row = (mouse_pos[0] - self.margin)//(self.margin + self.height)
        i_col = (mouse_pos[1] - self.margin)//(self.margin + self.width)
        grid_pos = [i_row, i_col]
        return grid_pos

    def draw_grid(self):
        for i_row in range(self.n_rows):
            for i_col in range(self.n_cols):
                x0 = i_row * (self.margin + self.height) + self.margin
                y0 = i_col * (self.margin + self.width) + self.margin
                rect = [x0, y0, self.width, self.height]
                if self.data_array[i_row, i_col] == 0:
                    rect_color = (255, 255, 255)
                elif self.data_array[i_row, i_col] == 1:
                    rect_color = (0, 255, 0)
                else:
                    rect_color = (255, 0, 0)
                pygame.draw.rect(self.window, rect_color, rect)
        return self

    def display_grid(self, window_size=(255, 255), caption="My Game", fps=60):
        pygame.init()
        self.window = pygame.display.set_mode(window_size)
        pygame.display.set_caption(caption)
        clock = pygame.time.Clock()
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        flag = True
        while flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    grid_pos_x, grid_pos_y = self.mouse_to_grid(mouse_pos)
                    self.data_array[grid_pos_x, grid_pos_y] = event.button

            # Game Logic

            # Screen-clearning

            # Draw
            self.window.fill(BLACK)
            self.draw_grid()
            pygame.display.update()
            clock.tick(fps)

        pygame.quit()
