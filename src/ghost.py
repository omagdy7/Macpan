import pygame
import time
import random
import math
from util import get_sprites
from timer import Timer
from settings import settings
from mode import MODE
from direction import DIRECTION
import map as Map

dx = [1, 0, -1, 0]  # right, down, left, up
dy = [0, 1, 0, -1]

inv_dir = [2, 3, 0, 1]
sprite_sheet = [2, 0, 3, 1]


class Ghost():
    def __init__(self, sprite_sheet, color, x, y ,lol):
        self.x = x
        self.y = y
        self.sprite_sheet = sprite_sheet
        self.name = "blinky"
        self.sprite = get_sprites(sprite_sheet)
        self.color = color
        self.last_move = 3  # this represents the direction based on the dx, dy arrays
        self.speed = 3
        self.timer = None
        self.mode = MODE.SCATTERED
        self.settings = lol

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

    def get_intial_tile(self):
        return (12 * 30 + 15, 12 * 30 + 15)

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

    def check_pacman_collision(self, game_state):
        voiceofdot2 = pygame.mixer.Channel(4)
        dotpickup = pygame.mixer.Sound('../assets/sfx/eat_ghost.wav')

        if game_state.pacman.powerup and abs(game_state.pacman.x - self.x) <= 30 and abs(game_state.pacman.y - self.y) <= 30:
            initial_position = self.get_intial_tile()
            self.mode = MODE.EATEN
            self.timer = Timer(2 * 1000)
            time.sleep(0.3)
            game_state.score += 200
            self.x = initial_position[0]
            self.y = initial_position[1]
            if self.settings.sound:
                voiceofdot2.play(dotpickup)
        elif not game_state.pacman.powerup and abs(game_state.pacman.x - self.x) <= 30 and abs(game_state.pacman.y - self.y) <= 30:
            if abs(game_state.pacman.x - self.x) <= 30 and abs(game_state.pacman.y - self.y) <= 30:
                game_state.is_pacman_alive = False

    def get_next_move(self, game_state, screen):

        default_tile = self.get_default_tile()

        ret = len(dx) * [math.inf]

        forbidden = inv_dir[self.last_move]

        rand_pos = (0, 0)

        if game_state.pacman.powerup and self.mode != MODE.EATEN:
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
                    elif self.mode == MODE.CHASING:
                        ret[i] = self.heuristic(
                            (nx, ny), game_state.pacman.x, game_state.pacman.y)
                    elif self.mode == MODE.FRIGHETENED:
                        ret[i] = self.heuristic(
                            (nx, ny), rand_pos[0], rand_pos[1])
                    elif self.mode == MODE.EATEN:
                        pos = self.get_intial_tile()
                        self.x = pos[0]
                        self.y = pos[1]
                    if self.settings.debug:
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

    def move(self, game_state, screen):
        self.check_pacman_collision(game_state)
        min_idx = self.get_next_move(game_state, screen)
        new_dx = dx[min_idx] * self.speed
        new_dy = dy[min_idx] * self.speed
        self.x += new_dx
        self.y += new_dy
        self.x %= 900  # The logic of the portal
        self.last_move = min_idx

    def draw(self, screen, powerup, counter):
        if self.timer is not None:
            elapsed_time = pygame.time.get_ticks() - self.timer.start
            if elapsed_time > self.timer.duration:
                self.mode = MODE.CHASING

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
