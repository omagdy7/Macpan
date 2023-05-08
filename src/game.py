from blinky import Blinky
from clyde import Clyde
from direction import DIRECTION
from inky import Inky
from pinky import Pinky
from player import Player
from settings import settings
import map as Map
import pygame

WIDTH = settings.width
HEIGHT = settings.height


class Game():
    def __init__(self):
        self.settings = settings

    def run(self):
        # Initialize Pygame
        pygame.init()

        # Set the dimensions of the window
        screen = pygame.display.set_mode((WIDTH, HEIGHT))

        # Sprite sheet for pacman
        sprite_sheet = pygame.image.load(
            '../assets/pacman_left_sprite.png').convert_alpha()

        # Sprite sheets for the ghosts
        blinky_sprite = pygame.image.load(
            '../assets/blinky.png').convert_alpha()
        pinky_sprite = pygame.image.load('../assets/pinky.png').convert_alpha()
        clyde_sprite = pygame.image.load('../assets/clyde.png').convert_alpha()
        inky_sprite = pygame.image.load('../assets/inky.png').convert_alpha()

        # our beautiful maze
        maze = Map.Map()

        # length of the map grid size
        TILE_WIDTH = WIDTH // len(maze.maze[0])
        TILE_HEIGHT = HEIGHT // len(maze.maze)

        # Initialize the player and the ghosts
        player = Player(sprite_sheet)
        blinky = Blinky(blinky_sprite, 75, 75)
        pinky = Pinky(pinky_sprite, 27 * 30, 30 * 30 + 15)
        inky = Inky(inky_sprite, 75, 30 * 30 + 15)
        clyde = Clyde(clyde_sprite, 27 * 30 + 15, 75)

        # Set the pacman velocity
        dx = 0
        dy = 0

        # counter used to cycle through pacman sprite animation
        counter = 0

        clock = pygame.time.Clock()

        pygame.mixer.music.load('../assets/sfx/game_start.wav')
        siren_sound = pygame.mixer.Sound('../assets/sfx/siren_1.wav')
        munch_sound = pygame.mixer.Sound('../assets/sfx/munch_1.wav')

        if settings.sound:
            pygame.mixer.music.play()
            siren_sound.play(-1)
        is_game_over = [False]

        # Main game loop
        while not is_game_over[0]:
            # setting game fps
            clock.tick(settings.fps)

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
                    is_game_over = False
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

            # Simulates holding the key which adds better playability for pacman
            if keys[pygame.K_w]:
                player.direction = DIRECTION.UP
                ty = -player.speed
                tx = 0
            elif keys[pygame.K_s]:
                player.direction = DIRECTION.DOWN
                ty = player.speed
                tx = 0
            elif keys[pygame.K_a]:
                player.direction = DIRECTION.LEFT
                tx = -player.speed
                ty = 0
            elif keys[pygame.K_d]:
                player.direction = DIRECTION.RIGHT
                tx = player.speed
                ty = 0

            # if tx and ty doesn't lead to colliding change the current dx and dy to them and other wise
            # let pacman move in his previous direction
            if player.check_collision(maze, tx, ty, TILE_WIDTH, TILE_HEIGHT):
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

            if player.check_collision(maze, dx, dy, TILE_WIDTH, TILE_HEIGHT):
                player.x += dx
                player.y += dy
                player.x %= 900

            # Move ghosts
            blinky.move(maze.maze, player, screen, is_game_over, blinky)
            pinky.move(maze.maze, player, screen, is_game_over, blinky)
            inky.move(maze.maze, player, screen, is_game_over, blinky)
            clyde.move(maze.maze, player, screen, is_game_over, blinky)

            # Draw the map on each frame
            maze.draw_map(screen)

            # Draw the player and the ghosts
            player.draw(screen, counter)
            blinky.draw(screen)
            pinky.draw(screen)
            inky.draw(screen)
            clyde.draw(screen)

            # Update the screen
            pygame.display.flip()

        # Quit Pygame
        pygame.quit()
