import math
from typing_extensions import override
from direction import DIRECTION
from settings import settings
import pygame
from ghost import Ghost


class Inky(Ghost):
    def __init__(self, sprite_sheet, x, y):
        super().__init__(sprite_sheet, "orange", x, y)

    def get_intermediate_tile(self, pacman):
        if pacman.direction == DIRECTION.UP:
            new_target = (pacman.x - 30 * 2, pacman.y - 30 * 2)
            if self.in_bounds(new_target):
                return new_target
            else:
                return (pacman.x, pacman.y)
        elif pacman.direction == DIRECTION.DOWN:
            new_target = (pacman.x, pacman.y + 30 * 2)
            if self.in_bounds(new_target):
                return new_target
            else:
                return (pacman.x, pacman.y)
        elif pacman.direction == DIRECTION.RIGHT:
            new_target = (pacman.x + 30 * 2, pacman.y)
            if self.in_bounds(new_target):
                return new_target
            else:
                return (pacman.x, pacman.y)
        elif pacman.direction == DIRECTION.LEFT:
            new_target = (pacman.x - 30 * 2, pacman.y)
            if self.in_bounds(new_target):
                return new_target
            else:
                return (pacman.x, pacman.y)

    def get_target(self, inter_tile, blinky):
        target = (inter_tile[0] - (blinky.x - inter_tile[0]),
                  inter_tile[1] - (blinky.y - inter_tile[1]))
        return target

    @override
    def get_next_move(self, target, maze, screen, blinky):
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        ret = len(dx) * [math.inf]

        forbidden = 0

        if self.last_move == 0:
            forbidden = 2
        if self.last_move == 1:
            forbidden = 3
        if self.last_move == 2:
            forbidden = 0
        if self.last_move == 3:
            forbidden = 1

        inter_tile = self.get_intermediate_tile(target)
        target = self.get_target(inter_tile, blinky)

        #  y = mx + c

        if settings.debug:
            pygame.draw.line(screen, self.color, (target),
                             (self.x, self.y), 1)

        for i in range(len(dx)):
            if i != forbidden:
                nx = self.x + dx[i] * self.speed
                ny = self.y + dy[i] * self.speed
                if self.check_collision(nx, ny, 30, 30, maze):
                    ret[i] = self.heuristic(
                        (nx, ny), target[0], target[1])

        min_idx = ret.index(min(ret))
        return min_idx
