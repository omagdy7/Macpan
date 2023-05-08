from blinky import Blinky
from clyde import Clyde
from inky import Inky
from pinky import Pinky
from player import Player
from settings import settings
import map as Map
import pygame

WIDTH = settings.width
HEIGHT = settings.height
maze = Map.Map()
TILE_WIDTH = WIDTH // len(maze.maze[0])
TILE_HEIGHT = HEIGHT // len(maze.maze)


class GameState():
    def __init__(self, sprites):
        self.pacman = Player(sprites[0])
        self.blinky = Blinky(sprites[1], 12 * TILE_WIDTH +
                             15, 12 * TILE_HEIGHT + 15)
        self.pinky = Pinky(sprites[2], 11 * TILE_WIDTH +
                           15, 12 * TILE_HEIGHT + 15)
        self.inky = Inky(sprites[3], 13 * TILE_WIDTH +
                         15, 12 * TILE_HEIGHT + 15)
        self.clyde = Clyde(sprites[4], 14 * TILE_WIDTH +
                           15, 12 * TILE_HEIGHT + 15)
        self.map = Map.Map()
        self.game_over = False
        self.is_pacman_alive = True

    def reset(self, sprites):
        self.pacman = Player(sprites[0])
        self.blinky = Blinky(sprites[1], 12 * TILE_WIDTH +
                             15, 12 * TILE_HEIGHT + 15)
        self.pinky = Pinky(sprites[2], 11 * TILE_WIDTH +
                           15, 12 * TILE_HEIGHT + 15)
        self.inky = Inky(sprites[3], 13 * TILE_WIDTH +
                         15, 12 * TILE_HEIGHT + 15)
        self.clyde = Clyde(sprites[4], 14 * TILE_WIDTH +
                           15, 12 * TILE_HEIGHT + 15)
        self.map = Map.Map()
        self.game_over = False
        self.is_pacman_alive = True
        timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(timer_event, 1000 * 10, 1)
