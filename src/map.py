import pygame
import math
import settings as Settings


H = 1
V = 2
D = 4
BD = 8
TR = 16
TL = 32
BL = 64
BR = 128
G = 256
LP = 512
RP = 1024

PI = math.pi


class Map():
    def __init__(self):
        self.maze = [
            [TL, H, H, H, H, H, H, H, H, H, H, H, H, H, H, H,H, H, H, H, H, H, H, H, H, H, H, H, H, TR],
            [V, TL, H, H, H, H, H, H, H, H, H, H, H, H, TR, TL, H, H, H, H, H, H, H, H, H, H, H, H, TR, V],
            [V, V, D, D, D, D, D, D, D, D, D, D, D, D, V, V, D, D, D, D, D, D, D, D, D, D, D, D, V, V],
            [V, V, D, TL, H, H, TR, D, TL, H, H, H, TR, D, V, V, D, TL, H, H, H, TR, D, TL, H, H, TR, D, V, V],
            [V, V, BD, V, 0, 0, V, D, V, 0, 0, 0, V, D, V, V, D, V, 0, 0, 0, V, D, V, 0, 0, V, BD, V, V],
            [V, V, D, BL, H, H, BR, D, BL, H, H, H, BR, D, BL, BR, D, BL, H, H, H, BR, D, BL, H, H, BR, D, V, V],
            [V, V, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, V, V],
            [V, V, D, TL, H, H, TR, D, TL, TR, D, TL, H, H, H, H, H, H, TR, D, TL, TR, D, TL, H, H, TR, D, V, V],
            [V, V, D, BL, H, H, BR, D, V, V, D, BL, H, H, TR, TL, H, H, BR, D, V, V, D, BL, H, H, BR, D, V, V],
            [V, V, D, D, D, D, D, D, V, V, D, D, D, D, V, V, D, D, D, D, V, V, D, D, D, D, D, D, V, V],
            [V, BL, H, H, H, H, TR, D, V, BL, H, H, TR, 0, V, V, 0, TL, H, H, BR, V, D, TL, H, H, H, H, BR, V],
            [V, 0, 0, 0, 0, 0, V, D, V, TL, H, H, BR, 0, BL, BR, 0, BL, H, H, TR, V, D, V, 0, 0, 0, 0, 0, V],
            [V, 0, 0, 0, 0, 0, V, D, V, V, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, V, V, D, V, 0, 0, 0, 0, 0, V],
            [BR, 0, 0, 0, 0, 0, V, D, V, V, 0, TL, H, H, G, G, H, H, TR, 0, V, V, D, V, 0, 0, 0, 0, 0, BL],
            [H, H, H, H, H, H, BR, D, BL, BR, 0, V, 0, 0, 0, 0, 0, 0, V, 0, BL, BR, D, BL, H, H, H, H, H, H],
            [0, 0, 0, 0, 0, 0, 0, D, 0, 0, 0, V, 0, 0, 0, 0, 0, 0, V, 0, 0, 0, D, 0, 0, 0, 0, 0, 0, 0],
            [H, H, H, H, H, H, TR, D, TL, TR, 0, V, 0, 0, 0, 0, 0, 0, V, 0, TL, TR, D, TL, H, H, H, H, H, H],
            [TR, 0, 0, 0, 0, 0, V, D, V, V, 0, BL, H, H, H, H, H, H, BR, 0, V, V, D, V, 0, 0, 0, 0, 0, TL],
            [V, 0, 0, 0, 0, 0, V, D, V, V, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, V, V, D, V, 0, 0, 0, 0, 0, V],
            [V, 0, 0, 0, 0, 0, V, D, V, V, 0, TL, H, H, H, H, H, H, TR, 0, V, V, D, V, 0, 0, 0, 0, 0, V],
            [V, TL, H, H, H, H, BR, D, BL, BR, 0, BL, H, H, TR, TL, H, H, BR, 0, BL, BR, D, BL, H, H, H, H, TR, V],
            [V, V, D, D, D, D, D, D, D, D, D, D, D, D, V, V, D, D, D, D, D, D, D, D, D, D, D, D, V, V],
            [V, V, D, TL, H, H, TR, D, TL, H, H, H, TR, D, V, V, D, TL, H, H, H, TR, D, TL, H, H, TR, D, V, V],
            [V, V, D, BL, H, TR, V, D, BL, H, H, H, BR, D, BL, BR, D, BL, H, H, H, BR, D, V, TL, H, BR, D, V, V],
            [V, V, BD, D, D, V, V, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, V, V, D, D, BD, V, V],
            [V, BL, H, TR, D, V, V, D, TL, TR, D, TL, H, H, H, H, H, H, TR, D, TL, TR, D, V, V, D, TL, H, BR, V],
            [V, TL, H, BR, D, BL, BR, D, V, V, D, BL, H, H, TR, TL, H, H, BR, D, V, V, D, BL, BR, D, BL, H, TR, V],
            [V, V, D, D, D, D, D, D, V, V, D, D, D, D, V, V, D, D, D, D, V, V, D, D, D, D, D, D, V, V],
            [V, V, D, TL, H, H, H, H, BR, BL, H, H, TR, D, V, V, D, TL, H, H, BR, BL, H, H, H, H, TR, D, V, V],
            [V, V, D, BL, H, H, H, H, H, H, H, H, BR, D, BL, BR, D, BL, H, H, H, H, H, H, H, H, BR, D, V, V],
            [V, V, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, V, V],
            [V, BL, H, H, H, H, H, H, H, H, H, H, H, H, H, H, H, H, H, H, H, H, H, H, H, H, H, H, BR, V],
            [BL, H, H, H, H, H, H, H, H, H, H, H, H, H, H, H, H, H, H, H, H, H, H, H, H, H, H, H, H, BR]
        ] 
        self.dot_color = (255, 255, 255)  # white
        self.small_dot_radius = 4
        self.big_dot_radius = 8
        self.line_color = (0, 0, 255)  # Blue
        self.line_vertical = Settings.settings.height // len(self.maze)
        self.line_horizontal = Settings.settings.width // len(self.maze[0])
        self.line_stroke = 1

    def consturct_map(self):
        pass

    def draw_wall(self, screen, flag, pos):
        if flag & V:
            pos1 = (pos[0] + self.line_vertical * 0.5, pos[1])
            pos2 = (pos1[0], pos1[1] + self.line_horizontal)
            pygame.draw.line(screen, self.line_color,
                             pos1, pos2, self.line_stroke)
        if flag & H:
            pos1 = (pos[0], pos[1] + self.line_vertical * 0.5)
            pos2 = (pos1[0] + self.line_horizontal, pos1[1])
            pygame.draw.line(screen, self.line_color,
                             pos1, pos2, self.line_stroke)
        if flag & D:
            pos1 = (pos[0] + self.line_vertical * 0.5,
                    pos[1] + self.line_horizontal * 0.5)
            pygame.draw.circle(screen, self.dot_color,
                               pos1, self.small_dot_radius)
        if flag & BD:
            pos1 = (pos[0] + self.line_vertical * 0.5,
                    pos[1] + self.line_horizontal * 0.5)
            pygame.draw.circle(screen, self.dot_color,
                               pos1, self.big_dot_radius)
        if flag & TR:
            pos1 = (pos[0] - self.line_vertical * 0.5,
                    pos[1] + self.line_horizontal * 0.5)
            arc_rect = pygame.Rect(
                pos1[0], pos1[1], self.line_vertical, self.line_horizontal)
            pygame.draw.arc(screen, self.line_color, arc_rect,
                            0, PI / 2, self.line_stroke)
        if flag & TL:
            pos1 = (pos[0] + self.line_vertical * 0.5,
                    pos[1] + self.line_horizontal * 0.5)
            arc_rect = pygame.Rect(
                pos1[0], pos1[1], self.line_vertical, self.line_horizontal)
            pygame.draw.arc(screen, self.line_color, arc_rect,
                            PI / 2, PI, self.line_stroke)
        if flag & BL:
            pos1 = (pos[0] + self.line_vertical * 0.5,
                    pos[1] - self.line_horizontal * 0.5)
            arc_rect = pygame.Rect(
                pos1[0], pos1[1], self.line_vertical, self.line_horizontal)
            pygame.draw.arc(screen, self.line_color, arc_rect,
                            PI, 3*PI / 2, self.line_stroke)
        if flag & BR:
            pos1 = (pos[0] - self.line_vertical * 0.5,
                    pos[1] - self.line_horizontal * 0.5)
            arc_rect = pygame.Rect(
                pos1[0], pos1[1], self.line_vertical, self.line_horizontal)
            pygame.draw.arc(screen, self.line_color, arc_rect,
                            3*PI / 2, PI * 2, self.line_stroke)

    def draw_map(self, screen):
        rows = len(self.maze)
        cols = len(self.maze[0])
        for i in range(0, rows):
            for j in range(cols):
                pos = (j * self.line_horizontal, i * self.line_vertical)
                self.draw_wall(screen, self.maze[i][j], pos)
                # pygame.draw.rect(screen, 'red', (pos[0], pos[1], 32, 32), 2)
