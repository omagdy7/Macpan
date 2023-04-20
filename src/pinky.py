import pygame
from typing_extensions import override
from direction import DIRECTION
import math
from ghost import Ghost

class Pinky(Ghost):
    def __init__(self, sprite_sheet, x, y):
        super().__init__(sprite_sheet,"pink", x, y)


    def get_four_tiles_ahead_of_pacman(self, pacman):
        if pacman.direction == DIRECTION.UP:
            new_target = (pacman.x - 30 * 4, pacman.y - 30 * 4)
            if self.in_bounds(new_target):
                return new_target
            else:
                return (pacman.x, pacman.y)
        elif pacman.direction == DIRECTION.DOWN:
            new_target = (pacman.x, pacman.y + 30 * 4)
            if self.in_bounds(new_target):
                return new_target
            else:
                return (pacman.x, pacman.y)
        elif pacman.direction == DIRECTION.RIGHT:
            new_target = (pacman.x + 30 * 4, pacman.y)
            if self.in_bounds(new_target):
                return new_target
            else:
                return (pacman.x, pacman.y)
        elif pacman.direction == DIRECTION.LEFT:
            new_target = (pacman.x - 30 * 4, pacman.y)
            if self.in_bounds(new_target):
                return new_target
            else:
                return (pacman.x, pacman.y)

    @override
    def get_next_move(self, target, maze, screen):
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

        new_target = self.get_four_tiles_ahead_of_pacman(target)
        pygame.draw.circle(screen, self.color, (new_target[0], new_target[1]), 15)
        
        for i in range(len(dx)):
            if i != forbidden:
                nx = self.x + dx[i] * self.speed
                ny = self.y + dy[i] * self.speed
                if self.check_collision(nx, ny, 30, 30, maze):
                    ret[i] = self.heuristic((nx, ny), new_target[0], new_target[1])

        min_idx = ret.index(min(ret))
        return min_idx






