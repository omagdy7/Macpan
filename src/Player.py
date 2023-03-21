from typing import List
from Direction import DIRECTION
import pygame
import settings as Settings


def get_sprites(sprite_sheet) -> List:
    sheet_width, sheet_height = sprite_sheet.get_size()
    sprite_width, sprite_height = 32, 32
    rows = sheet_height // sprite_height
    columns = sheet_width // sprite_width
    sprites = []

    for row in range(rows):
        for col in range(columns):
            x = col * sprite_width
            y = row * sprite_height
    
            # Create a new surface for the current sprite and blit it from the sprite sheet onto this new surface 
            new_sprite_surface = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA)
            new_sprite_surface.blit(sprite_sheet, (0, 0), (x, y, x + sprite_width, y +sprite_height))

            # Add this new surface to our list of sprites 
            sprites.append(new_sprite_surface)

    return sprites


class Player():
    def __init__(self, sprite_sheet):
        self.x = 450
        self.y = 663
        self.sprite = get_sprites(sprite_sheet)
        self.speed = 10
        self.direction = DIRECTION.LEFT

    def draw(self, screen, counter):
        pos = (self.x, self.y)
        if self.direction == DIRECTION.UP:
            screen.blit(pygame.transform.rotate(self.sprite[counter // 5], 270), pos)
        elif self.direction == DIRECTION.DOWN:
            screen.blit(pygame.transform.rotate(self.sprite[counter // 5], 90), pos)
        elif self.direction == DIRECTION.RIGHT:
            screen.blit(pygame.transform.flip(self.sprite[counter // 5], True, False), pos)
        elif self.direction == DIRECTION.LEFT:
            screen.blit(self.sprite[counter // 5], pos)

