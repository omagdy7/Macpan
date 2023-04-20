import math
from direction import DIRECTION
from ghost import Ghost

class Inky(Ghost):
    def __init__(self, sprite_sheet, x, y):
        super().__init__(sprite_sheet, "cyan", x, y)


    # def get_intermediate_tile(self, pacman):
    #     if pacman.direction == DIRECTION.UP:
    #         new_target = (pacman.x - 30 * 2, pacman.y - 30 * 4)
    #         if self.in_bounds(new_target):
    #             return new_target
    #         else:
    #             return (pacman.x, pacman.y)
    #     elif pacman.direction == DIRECTION.DOWN:
    #         new_target = (pacman.x, pacman.y + 30 * 2)
    #         if self.in_bounds(new_target):
    #             return new_target
    #         else:
    #             return (pacman.x, pacman.y)
    #     elif pacman.direction == DIRECTION.RIGHT:
    #         new_target = (pacman.x + 30 * 2, pacman.y)
    #         if self.in_bounds(new_target):
    #             return new_target
    #         else:
    #             return (pacman.x, pacman.y)
    #     elif pacman.direction == DIRECTION.LEFT:
    #         new_target = (pacman.x - 30 * 2, pacman.y)
    #         if self.in_bounds(new_target):
    #             return new_target
    #         else:
    #             return (pacman.x, pacman.y)
    #
    # def get_vector_blinky_it(self, blinky, pacman):
    #     it = self.get_intermediate_tile(pacman)
    #     return (it[0] - blinky.x, it[1], blinky.y)
    #
    # @override
    # def get_next_move(self, target, maze, screen):
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
    #     new_target = self.get_intermediate_tile(target)
    #     pygame.draw.circle(screen, self.color, (new_target[0], new_target[1]), 15)
    #     
    #     for i in range(len(dx)):
    #         if i != forbidden:
    #             nx = self.x + dx[i] * self.speed
    #             ny = self.y + dy[i] * self.speed
    #             if self.check_collision(nx, ny, 30, 30, maze):
    #                 ret[i] = self.heuristic((nx, ny), new_target[0], new_target[1])
    #
    #     min_idx = ret.index(min(ret))
    #     return min_idx
    #
    #
    #
    #
