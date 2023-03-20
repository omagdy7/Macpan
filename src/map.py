# the map is 2d array of with size (160, 120)
# 0 -> free
# 1 -> vertical line
# 2 -> 

import pygame
import settings as Settings


U = 1
D = 4
L = 8
R = 2

LU = L | U
LD = L | D
RU = R | U
RD = R | D


class Map():
    """
    0 -> free
    1 -> vertical line
    2 -> horizontal line
    3 -> right, down

    """
    def __init__(self):
        self.map = [
            [LU, U, U, U, U, U, U, RU],
            [L, 0, 0, 0, 0, 0, 0,  R],
            [L, 0, LU, 0, RU, 0, 0,R],
            [L, 0, 0, 0, 0, 0, 0,  R],
            [L, 0, 0, 0, 0, 0, 0,  R],
            [LD, D, D, D, D, D, D, RD],
        ]
        self.line_length = Settings.settings.width // len(self.map)
        self.line_color = (0, 0, 150)
        self.line_stroke = 6

    def consturct_map(self):
        pass


    def draw_wall(self, screen, flag , pos):
        if flag & U:
            pos1 = pos
            pos2 = (pos[0] + self.line_length, pos[1])
            pygame.draw.line(screen, self.line_color, pos1, pos2, self.line_stroke)
        if flag & D:
            pos1 = (pos[0], pos[1] + self.line_length)
            pos2 = (pos[0] + self.line_length, pos[1] + self.line_length)
            pygame.draw.line(screen, self.line_color, pos1, pos2, self.line_stroke)
        if flag & R:
            pos1 = (pos[0] + self.line_length, pos[1])
            pos2 = (pos[0] + self.line_length, pos[1] + self.line_length)
            pygame.draw.line(screen, self.line_color, pos1, pos2, self.line_stroke)
        if flag & L:
            pos1 = pos
            pos2 = (pos[0], pos[1] + self.line_length)
            pygame.draw.line(screen, self.line_color, pos1, pos2, self.line_stroke)

            
            
        

    def draw_map(self, screen):
        rows = len(self.map)
        cols = len(self.map[0])
        # ofs = Settings.settings.width // cols
        # line_color = (0, 0, 150)
        # line_stroke = 6
        for i in range(0, rows):
            for j in range(cols):
                pos = (j * self.line_length, i * self.line_length)
                self.draw_wall(screen, self.map[i][j], pos)
                # if self.map[i][j] == 1:
                #     if i == rows - 1:
                #         p1 = (j * ofs, (i + 1) * ofs)
                #         p2 = ((j + 1) * ofs, (i + 1) * ofs)
                #     else:
                #         p1 = (j * ofs, i * ofs)
                #         p2 = ((j + 1) * ofs, i * ofs)
                #     pygame.draw.line(screen, line_color, p1, p2, line_stroke)
                # if self.map[i][j] == 2:
                #     if j == cols - 1:
                #         p1 = ((j + 1) * ofs, i * ofs)
                #         p2 = ((j + 1) * ofs, (i + 1) * ofs)
                #     else:
                #         p1 = (j * ofs, i * ofs)
                #         p2 = (j * ofs, (i + 1) * ofs)
                #     pygame.draw.line(screen, line_color, p1, p2, line_stroke)
                # if self.map[i][j] == 3:
                #     p1_vertical = (j * ofs, i * ofs)
                #     p2_vertical = ((j + 1) * ofs, i * ofs)
                #     p1_horizontal = (j * ofs, i * ofs)
                #     p2_horizontal = (j * ofs, (i + 1) * ofs)
                #     pygame.draw.line(screen, line_color, p1_horizontal, p2_horizontal, line_stroke)
                #     pygame.draw.line(screen, line_color, p1_vertical, p2_vertical, line_stroke)
                # if self.map[i][j] == 4:
                #     p1_vertical = (j * ofs, (i + 1) * ofs)
                #     p2_vertical = ((j + 1) * ofs, (i + 1) * ofs)
                #     p1_horizontal = (j * ofs, i * ofs)
                #     p2_horizontal = (j * ofs, (i + 1) * ofs)
                #     pygame.draw.line(screen, line_color, p1_horizontal, p2_horizontal, line_stroke)
                #     pygame.draw.line(screen, line_color, p1_vertical, p2_vertical, line_stroke)
                # if self.map[i][j] == 5:
                #     p1_vertical = (j * ofs, (i + 1) * ofs)
                #     p2_vertical = ((j + 1) * ofs, (i + 1) * ofs)
                #     p1_horizontal = ((j + 1) * ofs, i * ofs)
                #     p2_horizontal = ((j + 1) * ofs, (i + 1) * ofs)
                #     pygame.draw.line(screen, line_color, p1_horizontal, p2_horizontal, line_stroke)
                #     pygame.draw.line(screen, line_color, p1_vertical, p2_vertical, line_stroke)
                # if self.map[i][j] == 6:
                #     p1_vertical = (j * ofs, i * ofs)
                #     p2_vertical = ((j + 1) * ofs, i * ofs)
                #     p1_horizontal = ((j + 1) * ofs, i * ofs)
                #     p2_horizontal = ((j + 1) * ofs, (i + 1) * ofs)
                #     pygame.draw.line(screen, line_color, p1_horizontal, p2_horizontal, line_stroke)
                #     pygame.draw.line(screen, line_color, p1_vertical, p2_vertical, line_stroke)
