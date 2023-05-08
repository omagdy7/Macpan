import math
import random
from typing_extensions import override
from direction import DIRECTION
from mode import MODE
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

    @override
    def get_default_tile(self):
        return (27 * 30 + 15, 2 * 30 + 15)

    @override
    def get_intial_tile(self):
        return (13 * 30 + 15, 12 * 30 + 15)

    def get_target(self, inter_tile, blinky):
        target = (max(inter_tile[0] - (blinky.x - inter_tile[0]) % 900, 0),
                  max(inter_tile[1] - (blinky.y - inter_tile[1]) % 990, 0))
        return target

    @override
    def get_next_move(self, game_state, screen):
        default_tile = self.get_default_tile()

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

        inter_tile = self.get_intermediate_tile(game_state.pacman)
        target = self.get_target(inter_tile, game_state.blinky)

        rand_pos = (0, 0)

        if game_state.pacman.powerup:
            self.mode = MODE.FRIGHETENED
            rand_pos = random.randint(0, 900), random.randint(0, 990)

        if game_state.pacman.powerup is False and self.mode == MODE.FRIGHETENED:
            self.mode = MODE.CHASING

        if settings.debug:
            pygame.draw.line(screen, self.color, (target),
                             (self.x, self.y), 1)

        for i in range(len(dx)):
            if i != forbidden:
                nx = self.x + dx[i] * self.speed
                ny = self.y + dy[i] * self.speed
                if self.check_collision(nx, ny, 30, 30, game_state.map.maze):
                    if self.mode == MODE.SCATTERED:
                        ret[i] = self.heuristic(
                            (nx, ny), default_tile[0], default_tile[1])
                    elif self.mode == MODE.FRIGHETENED:
                        ret[i] = self.heuristic(
                            (nx, ny), rand_pos[0], rand_pos[1])
                    elif self.mode == MODE.CHASING:
                        ret[i] = self.heuristic(
                            (nx, ny), target[0], target[1])

        min_h = min(ret)

        # Favour going up when there is a conflict
        if min_h == ret[3] and min_h != math.inf:
            return 3
        # Favour going down than sideways when there is a conflict
        if min_h == ret[1] and min_h != math.inf:
            return 1
        min_idx = ret.index(min_h)
        return min_idx
