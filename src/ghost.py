import pygame
import random
import math
from util import get_sprites
from settings import settings
from mode import MODE
from direction import DIRECTION
import map as Map

dx = [1, 0, -1, 0]  # right, down, left, up
dy = [0, 1, 0, -1]

inv_dir = [2, 3, 0, 1]
sprite_sheet = [2, 0, 3, 1]


class Ghost():
    def __init__(self, sprite_sheet, color, x, y):
        self.x = x
        self.y = y
        self.sprite_sheet = sprite_sheet
        self.name = "blinky"
        self.sprite = get_sprites(sprite_sheet)
        self.color = color
        self.last_move = 3  # this represents the direction based on the dx, dy arrays
        self.speed = 3
        self.mode = MODE.SCATTERED

    def in_bounds(self, pos):
        (x, y) = pos
        return (x >= 0) and (y >= 0) and (x < settings.width - 30) and (y < settings.height)

    def heuristic(self, next_pos, tx, ty):
        return abs(next_pos[0] - tx) + abs(next_pos[1] - ty)

    # checks if the current position of pacman is either a dot, big dot or free

    def is_valid(self, maze, x, y):
        if x >= 0 and x < 30:  # Necessary to make portals work
            is_dot = maze[y][x] == Map.D
            is_big_dot = maze[y][x] == Map.BD
            is_free = maze[y][x] == 0
            return (is_dot or is_free or is_big_dot)
        return True

    def get_default_tile(self):
        return (75, 75)

    # checks collision with pacman and obstacles returns false if there is
    # a collision and true otherwise

    def check_collision(self, nx, ny, gx, gy, maze):
        direct_x = [1, 0, -1, 0, 1, 1, -1, -1]
        direct_y = [0, 1, 0, -1, -1, 1, -1, 1]

        for i in range(len(direct_x)):
            px = nx + direct_x[i] * 14
            py = ny + direct_y[i] * 14
            x = px // gx
            y = py // gy
            if not self.is_valid(maze, x, y):
                return False

        return True

    def get_next_move(self, pacman, maze, screen, blinky):

        default_tile = self.get_default_tile()

        ret = len(dx) * [math.inf]

        forbidden = inv_dir[self.last_move]

        rand_pos = (0, 0)

        if pacman.powerup:
            self.mode = MODE.FRIGHETENED
            rand_pos = random.randint(0, 900), random.randint(0, 990)

        if pacman.powerup is False and self.mode == MODE.FRIGHETENED:
            self.mode = MODE.CHASING

        for i in range(len(dx)):
            nx = self.x + dx[i] * self.speed
            ny = self.y + dy[i] * self.speed
            if self.check_collision(nx, ny, 30, 30, maze):
                if i != forbidden:
                    if self.mode == MODE.SCATTERED:
                        ret[i] = self.heuristic(
                            (nx, ny), default_tile[0], default_tile[1])
                    elif self.mode == MODE.CHASING:
                        ret[i] = self.heuristic((nx, ny), pacman.x, pacman.y)
                    elif self.mode == MODE.FRIGHETENED:
                        ret[i] = self.heuristic(
                            (nx, ny), rand_pos[0], rand_pos[1])
                    if settings.debug:
                        pygame.draw.line(screen, self.color, (pacman.x, pacman.y),
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

    def move(self, maze, pacman, screen, game_over, blinky):
        if abs(pacman.x - self.x) <= 15 and abs(pacman.y - self.y) <= 15:
            game_over[0] = True
        min_idx = self.get_next_move(pacman, maze, screen, blinky)
        new_dx = dx[min_idx] * self.speed
        new_dy = dy[min_idx] * self.speed
        self.x += new_dx
        self.y += new_dy
        self.x %= 900  # The logic of the portal
        self.last_move = min_idx

    def draw(self, screen, powerup, counter):
        print(f"{self.color} -> mode: {self.mode}")
        radius = 30 // 2
        pos = (self.x - radius, self.y - radius)
        if powerup:
            self.sprite = get_sprites(pygame.image.load(
                f'../assets/pacman_{self.color}.png').convert_alpha())
            image = pygame.transform.scale(self.sprite[counter // 5], (35, 35))
            if self.last_move == DIRECTION.UP.value:
                screen.blit(pygame.transform.rotate(image, 270), pos)
            elif self.last_move == DIRECTION.DOWN.value:
                screen.blit(pygame.transform.rotate(image, 90), pos)
            elif self.last_move == DIRECTION.RIGHT.value:
                screen.blit(pygame.transform.flip(image, True, False), pos)
            elif self.last_move == DIRECTION.LEFT.value:
                screen.blit(image, pos)
        else:
            self.sprite = get_sprites(self.sprite_sheet)
            image = pygame.transform.scale(
                self.sprite[sprite_sheet[self.last_move]], (40, 40))
            screen.blit(image, pos)
