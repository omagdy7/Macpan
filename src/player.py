from direction import DIRECTION
from timer import Timer
import map as Map
from util import get_sprites
import pygame


class Player():

    def __init__(self, sprite_sheet, settings):
        self.settings = settings
        self.x = 30 * 17 - 15
        self.y = 30 * 25 - 15
        self.sprite_sheet = sprite_sheet
        self.sprite = get_sprites(sprite_sheet)
        self.speed = 6
        self.direction = DIRECTION.LEFT
        self.powerup = False
        self.timer = None

    # checks if the current position of pacman is either a dot, big dot or free
    def is_valid(self, game_state, x, y):

        if x >= 0 and x < 30:
            is_dot = game_state.map.maze[y][x] == Map.D
            is_big_dot = game_state.map.maze[y][x] == Map.BD
            is_free = game_state.map.maze[y][x] == 0
            if is_dot or is_big_dot:
                game_state.map.maze[y][x] = 0
                game_state.food += 1
            if is_dot:
                game_state.score += 10


            if is_big_dot:
                self.powerup = True
                self.timer = Timer(5 * 1000)
                game_state.score += 50
            return (is_dot or is_free or is_big_dot)
        return True

    # checks collision with pacman and obstacles returns false
    # if there is a collision and true otherwise
    def check_collision(self, game_state, dx, dy, tile_width, tile_height):
        direct_x = [1, 0, -1, 0, 1, 1, -1, -1]
        direct_y = [0, 1, 0, -1, -1, 1, -1, 1]

        for i in range(len(direct_x)):
            ddx = dx
            ddy = dy
            nx = (self.x + ddx) + direct_x[i] * 14
            ny = (self.y + ddy) + direct_y[i] * 14
            x = nx // tile_width
            y = ny // tile_height
            if not self.is_valid(game_state, x, y):
                return False

        return True

    def draw(self, screen, counter):
        voice = pygame.mixer.Channel(2)
        Soundpowerup = pygame.mixer.Sound('../assets/sfx/power_pellet.wav')
        if self.timer is not None:
            elapsed_time = pygame.time.get_ticks() - self.timer.start
            if elapsed_time > self.timer.duration:
                self.powerup = False



        radius = 30 // 2
        pos = (self.x - radius, self.y - radius)
        sprite_sheet = [2, 0, 3, 1]
        if self.powerup:
            self.sprite = get_sprites(pygame.image.load(
                '../assets/pacman_as_ghost.png').convert_alpha())
            image = pygame.transform.scale(
                self.sprite[sprite_sheet[self.direction.value]], (40, 40))
            screen.blit(image, pos)
            if self.settings.sound:
                if not (voice.get_busy()):
                     voice.play(Soundpowerup)

        else:
            voice.stop()
            self.sprite = get_sprites(self.sprite_sheet)
            image = pygame.transform.scale(self.sprite[counter // 5], (35, 35))
            if self.direction == DIRECTION.UP:
                screen.blit(pygame.transform.rotate(image, 270), pos)
            elif self.direction == DIRECTION.DOWN:
                screen.blit(pygame.transform.rotate(image, 90), pos)
            elif self.direction == DIRECTION.RIGHT:
                screen.blit(pygame.transform.flip(image, True, False), pos)
            elif self.direction == DIRECTION.LEFT:
                screen.blit(image, pos)
