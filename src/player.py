from typing import List
from direction import DIRECTION
import map as Map
from util import get_sprites
import pygame


class Player():
    def __init__(self, sprite_sheet):
        self.x = 30 * 17 - 15
        self.y = 30 * 25 - 15
        self.sprite = get_sprites(sprite_sheet)
        self.speed = 6
        self.direction = DIRECTION.LEFT

    # checks if the current position of pacman is either a dot, big dot or free
    def is_valid(self,maze, x, y):
        if x >= 0 and x < 30:
            is_dot = maze.maze[y][x] == Map.D
            is_big_dot = maze.maze[y][x] == Map.BD
            is_free = maze.maze[y][x] == 0
            if is_dot or is_big_dot:
                maze.maze[y][x] = 0
            return (is_dot or is_free or is_big_dot)
        return True


    # checks collision with pacman and obstacles returns false if there is a collision and true otherwise
    def check_collision(self, maze, dx, dy, tile_width, tile_height):
        direct_x = [1, 0, -1, 0, 1, 1, -1, -1]
        direct_y = [0, 1, 0, -1, -1, 1, -1, 1]

        for i in range(len(direct_x)):
            ddx = dx
            ddy = dy
            nx = (self.x + ddx) + direct_x[i] * 14
            ny = (self.y + ddy) + direct_y[i] * 14
            x = nx // tile_width
            y = ny // tile_height
            if not self.is_valid(maze, x, y):
                return False

        return True

    def draw(self, screen, counter):
        radius = 30 // 2
        pos = (self.x - radius , self.y - radius)
        image = pygame.transform.scale(self.sprite[counter // 5], (35, 35))
        if self.direction == DIRECTION.UP:
            screen.blit(pygame.transform.rotate(image, 270), pos)
        elif self.direction == DIRECTION.DOWN:
            screen.blit(pygame.transform.rotate(image, 90), pos)
        elif self.direction == DIRECTION.RIGHT:
            screen.blit(pygame.transform.flip(image, True, False), pos)
        elif self.direction == DIRECTION.LEFT:
            screen.blit(image, pos)
