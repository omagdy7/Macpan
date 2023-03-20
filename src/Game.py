import Player
from Direction import DIRECTION
import settings as Settings
import map as Map
import pygame

class Game():
    def __init__(self):
        self.settings = Settings.settings

    def init(self):
        # Initialize Pygame
        pygame.init()

        # Set the dimensions of the window
        screen = pygame.display.set_mode((Settings.settings.width, Settings.settings.height))

        # Sprite sheet for pacman
        sprite_sheet = pygame.image.load('../assets/pacman_left_sprite.png').convert_alpha();

        player = Player.Player(sprite_sheet)

        # Set the circle's velocity
        dx = 0
        dy = 0

        # counter used to cycle through pacman sprite animation
        counter = 0

        clock = pygame.time.Clock()

        # Sprite sheet for pacman
        sprite_sheet = pygame.image.load('../assets/pacman_left_sprite.png').convert_alpha();

        sprite_width, sprite_height = 32, 32



        # Checks collision with walls
        def check_collision(dx, dy):
            return player.y + sprite_height + dy > Settings.settings.height or player.y + dy < 0 or player.x + sprite_width + dx > Settings.settings.width or player.x + dx < 0 

        map = Map.Map()
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

            # Handling events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    # Move the circle based on the pressed key
                    if event.key == pygame.K_w:
                        player.direction = DIRECTION.UP
                        dy = -player.speed
                        dx = 0 # Necssarry to move only horizontal or vertical
                    elif event.key == pygame.K_s:
                        player.direction = DIRECTION.DOWN
                        dy = player.speed
                        dx = 0 # Necssarry to move only horizontal or vertical
                    elif event.key == pygame.K_a:
                        player.direction = DIRECTION.LEFT
                        dx = -player.speed
                        dy = 0 # Necssarry to move only horizontal or vertical
                    elif event.key == pygame.K_d:
                        player.direction = DIRECTION.RIGHT
                        dx = player.speed
                        dy = 0 # Necssarry to move only horizontal or vertical


            # Update the circle's position and checking for collisions
            if not check_collision(dx, dy):
                player.x += dx
                player.y += dy

            screen.fill((0, 0, 0)) # Clear the screen

            map.draw_map(screen)
            player.draw(screen, counter)

            # Update the screen
            pygame.display.flip()


        # Quit Pygame
        pygame.quit()
