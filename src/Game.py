from pygame.mouse import get_pressed
import Player
import Ghost
from Direction import DIRECTION
import settings as Settings
import map as Map
import pygame
import math


class Game():
    def __init__(self):
        self.settings = Settings.settings

    def init(self):
        # Initialize Pygame
        pygame.init()

        # Set the dimensions of the window
        screen = pygame.display.set_mode(
            (Settings.settings.width, Settings.settings.height))

        # Sprite sheet for pacman
        sprite_sheet = pygame.image.load(
            '../assets/pacman_left_sprite.png').convert_alpha()

        player = Player.Player(sprite_sheet)
        inky = Ghost.Ghost("green", 75, 75)
        pinky = Ghost.Ghost("cyan", 27 * 30, 30 * 30 + 15)
        clyde = Ghost.Ghost("red", 27 * 30 + 15, 75)
        winky = Ghost.Ghost("purple", 75, 30 * 30 + 15)

        # Set the pacman velocity
        dx = 0
        dy = 0

        # counter used to cycle through pacman sprite animation
        counter = 0

        clock = pygame.time.Clock()


        maze = Map.Map()

        # length of the map grid size
        grid_x = Settings.settings.width // len(maze.maze[0])
        grid_y = Settings.settings.height // len(maze.maze)

        print(grid_x, grid_y)

        # Checks collision with walls

        # checks if the current position of pacman is either a dot, big dot or free
        def is_valid(x, y):
            is_dot = maze.maze[y][x] == Map.D
            is_big_dot = maze.maze[y][x] == Map.BD
            is_free = maze.maze[y][x] == 0
            if is_dot or is_big_dot:
                maze.maze[y][x] = 0
            return (is_dot or is_free or is_big_dot)


        # checks collision with pacman and obstacles returns false if there is a collision and true otherwise
        def check_collision(dx, dy):
            direct_x = [1, 0, -1, 0, 1, 1, -1, -1]
            direct_y = [0, 1, 0, -1, -1, 1, -1, 1]

            for i in range(len(direct_x)):
                nx = (player.x + dx) + direct_x[i] * 14
                ny = (player.y + dy) + direct_y[i] * 14
                x = nx // grid_x
                y = ny // grid_y
                if not is_valid(x, y):
                    return False

            return True

        # Main game loop
        running = True

        while running:
            # setting game fps
            clock.tick(Settings.settings.fps)

            # counter logic for cycling between pacman different sprites
            if counter < 19:
                counter += 1
            else:
                counter = 0

            screen.fill((0, 0, 0))  # Clear the screen

            # Temporary values for delta_x and delta_y in the position of pacman
            tx = dx
            ty = dy

            # Handling events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    # Move the circle based on the pressed key
                    if event.key == pygame.K_w:
                        player.direction = DIRECTION.UP
                        ty = -player.speed
                        tx = 0  # Necssarry to move only horizontal or vertical
                    elif event.key == pygame.K_s:
                        player.direction = DIRECTION.DOWN
                        ty = player.speed
                        tx = 0  # Necssarry to move only horizontal or vertical
                    elif event.key == pygame.K_a:
                        player.direction = DIRECTION.LEFT
                        tx = -player.speed
                        ty = 0  # Necssarry to move only horizontal or vertical
                    elif event.key == pygame.K_d:
                        player.direction = DIRECTION.RIGHT
                        tx = player.speed
                        ty = 0  # Necssarry to move only horizontal or vertical

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                ty = -player.speed
                tx = 0
            elif keys[pygame.K_s]:
                ty = player.speed
                tx = 0
            elif keys[pygame.K_a]:
                tx = -player.speed
                ty = 0
            elif keys[pygame.K_d]:
                tx = player.speed
                ty = 0


            # if tx and ty doesn't lead to colliding change the current dx and dy to them and other wise
            # let pacman move in his previous direction
            if check_collision(tx, ty):
                dx = tx
                dy = ty

            if dx < 0:
                player.direction = DIRECTION.LEFT
            elif dx > 0:
                player.direction = DIRECTION.RIGHT
            elif dy < 0:
                player.direction = DIRECTION.UP
            elif dy > 0:
                player.direction = DIRECTION.DOWN

            if check_collision(dx, dy):
                player.x += dx
                player.y += dy


            inky.move(maze.maze, (player.x, player.y))
            pinky.move(maze.maze, (player.x, player.y))
            winky.move(maze.maze, (player.x, player.y))
            clyde.move(maze.maze, (player.x, player.y))
            maze.draw_map(screen)
            player.draw(screen, counter)
            inky.draw(screen)
            pinky.draw(screen)
            winky.draw(screen)
            clyde.draw(screen)

            # Update the screen
            pygame.display.flip()

        # Quit Pygame
        pygame.quit()
