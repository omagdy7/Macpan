from typing import List
from Direction import DIRECTION
from util import get_sprites
import pygame


class Player():
    def __init__(self, sprite_sheet):
        self.x = 30 * 17 - 15
        self.y = 30 * 25 - 15
        self.sprite = get_sprites(sprite_sheet)
        self.speed = 6
        self.direction = DIRECTION.LEFT

    def draw(self, screen, counter):
        radius = 30 // 2
        pos = (self.x - radius , self.y - radius)
        # pygame.draw.circle(screen, 'green', pos, radius)
        if self.direction == DIRECTION.UP:
            screen.blit(pygame.transform.rotate(
                self.sprite[counter // 5], 270), pos)
        elif self.direction == DIRECTION.DOWN:
            screen.blit(pygame.transform.rotate(
                self.sprite[counter // 5], 90), pos)
        elif self.direction == DIRECTION.RIGHT:
            screen.blit(pygame.transform.flip(
                self.sprite[counter // 5], True, False), pos)
        elif self.direction == DIRECTION.LEFT:
            screen.blit(self.sprite[counter // 5], pos)
