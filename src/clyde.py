from ghost import Ghost
import random
import pygame
from settings import settings
from mode import MODE
from typing_extensions import override
import math


class Clyde(Ghost):
    def __init__(self, sprite_sheet, x, y):
        super().__init__(sprite_sheet, "cyan", x, y)

    def is_eight_tiles_away(self, pacman):
        tile_width = 30
        dx = self.x - pacman.x
        dy = self.y - pacman.y
        return math.sqrt(dx * dx + dy * dy) <= tile_width * 8

    @override
    def get_default_tile(self):
        return (27 * 30 + 15, 2 * 30 + 15)

    @override
    def get_next_move(self, game_state, screen):
        default_tile = self.get_default_tile()

        dx = [1, 0, -1, 0]  # right, down, left, up
        dy = [0, 1, 0, -1]

        inv_dir = [2, 3, 0, 1]

        ret = len(dx) * [math.inf]
        bottom_left_corner = (
            2.5 * 30, (len(game_state.map.maze) - 1 - 1 - 0.5) * 30)

        forbidden = inv_dir[self.last_move]

        rand_pos = (0, 0)

        if game_state.pacman.powerup:
            self.mode = MODE.FRIGHETENED
            rand_pos = random.randint(0, 900), random.randint(0, 990)

        if game_state.pacman.powerup is False and self.mode == MODE.FRIGHETENED:
            self.mode = MODE.CHASING

        for i in range(len(dx)):
            nx = self.x + dx[i] * self.speed
            ny = self.y + dy[i] * self.speed
            if self.check_collision(nx, ny, 30, 30, game_state.map.maze):
                if i != forbidden:
                    if self.mode == MODE.SCATTERED:
                        ret[i] = self.heuristic(
                            (nx, ny), default_tile[0], default_tile[1])
                    elif self.mode == MODE.FRIGHETENED:
                        ret[i] = self.heuristic(
                            (nx, ny), rand_pos[0], rand_pos[1])
                    elif self.mode == MODE.CHASING:
                        if self.is_eight_tiles_away(game_state.pacman):
                            ret[i] = self.heuristic(
                                (nx, ny), bottom_left_corner[0], bottom_left_corner[1])
                            if settings.debug:
                                pygame.draw.line(screen, self.color, (bottom_left_corner),
                                                 (self.x, self.y), 1)
                        else:
                            ret[i] = self.heuristic(
                                (nx, ny), game_state.pacman.x, game_state.pacman.y)
                            if settings.debug:
                                pygame.draw.line(screen, self.color, (game_state.pacman.x, game_state.pacman.y),
                                                 (self.x, self.y), 1)

        min_h = min(ret)

        # Favour going up when there is a conflict
        if min_h == ret[3] and min_h != math.inf:
            return 3
        # Favour going down than sideways when there is a conflict
        if min_h == ret[1] and min_h != math.inf:
            return 1
        min_idx = ret.index(min_h)
        return min_idx
