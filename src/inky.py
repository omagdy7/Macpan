import math
from typing_extensions import override
from direction import DIRECTION
from settings import settings
import pygame
from ghost import Ghost


class Inky(Ghost):
    def __init__(self, sprite_sheet, x, y):
        super().__init__(sprite_sheet, "orange", x, y)

    # @override
    # def get_next_move(self, target, maze, screen, blinky):
    #     dx = [1, 0, -1, 0]
    #     dy = [0, 1, 0, -1]
    #
    #     ret = len(dx) * [math.inf]
    #
    #     forbidden = 0
    #
    #     if self.last_move == 0:
    #         forbidden = 2
    #     if self.last_move == 1:
    #         forbidden = 3
    #     if self.last_move == 2:
    #         forbidden = 0
    #     if self.last_move == 3:
    #         forbidden = 1
    #
    #     new_target = self.get_target(target, blinky)
    #
    #     if settings.debug:
    #         pygame.draw.line(screen, self.color, (new_target),
    #                          (blinky.x, blinky.y), 1)
    #
    #     for i in range(len(dx)):
    #         if i != forbidden:
    #             nx = self.x + dx[i] * self.speed
    #             ny = self.y + dy[i] * self.speed
    #             if self.check_collision(nx, ny, 30, 30, maze):
    #                 ret[i] = self.heuristic(
    #                     (nx, ny), new_target[0], new_target[1])
    #
    #     min_idx = ret.index(min(ret))
    #     return min_idx
