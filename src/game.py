from direction import DIRECTION
from game_state import GameState
from mode import MODE
from settings import settings
from game_state import WIDTH, HEIGHT, TILE_WIDTH, TILE_HEIGHT
import pygame


class Game():
    def __init__(self):
        self.settings = settings

    def show_gameover_screen(self, screen, game_state, sprites):
        font = pygame.font.SysFont(None, 64)

        # Render the "Game Over" text to a surface
        game_over_text_1 = font.render(
            "Game Over", True, (255, 255, 255))
        game_over_text_2 = font.render(
            "Press R to try again or Q to quit.", True, (255, 255, 255))

        # Blit the "Game Over" text onto the screen
        text_rect_1 = game_over_text_1.get_rect(
            center=(WIDTH/2, HEIGHT/2 - 75))
        text_rect_2 = game_over_text_2.get_rect(
            center=(WIDTH/2, HEIGHT/2))

        screen.blit(game_over_text_1, text_rect_1)
        screen.blit(game_over_text_2, text_rect_2)

        # Update the display
        pygame.display.flip()

        quit_game = False  # Initialize the flag variable
        while not quit_game:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    # Reset the game and start again
                    # Add your own code here to reset the game state
                    self.reset_game(game_state, sprites)
                    game_state.game_over = False
                    quit_game = True  # Set the flag to True to break out of both loops
                    break
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    game_state.game_over = True
                    quit_game = True
                    break
                elif event.type == pygame.QUIT:
                    game_state.game_over = True
                    quit_game = True  # Set the flag to True to break out of both loops
                    break

    def show_wining_screen(self, screen, game_state, sprites):
        font = pygame.font.SysFont(None, 64)

        # Render the "Game Over" text to a surface
        wining_text_1 = font.render(
            "Congratulation You Won!!", True, (255, 255, 255))
        wining_text_2 = font.render(
            "Press R to play again or Q to quit", True, (255, 255, 255))

        text_rect_1 = wining_text_1.get_rect(
            center=(WIDTH/2, HEIGHT/2 - 75))
        text_rect_2 = wining_text_2.get_rect(
            center=(WIDTH/2, HEIGHT/2))

        # Blit the "Game Over" text onto the screen
        text_rect_1 = wining_text_1.get_rect(
            center=(WIDTH/2, HEIGHT/2))
        text_rect_2 = wining_text_2.get_rect(
            center=(WIDTH/2, HEIGHT/2 + 100))
        screen.blit(wining_text_1, text_rect_1)
        screen.blit(wining_text_2, text_rect_2)

        # Update the display
        pygame.display.flip()

        quit_game = False  # Initialize the flag variable
        while not quit_game:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    # Reset the game and start again
                    # Add your own code here to reset the game state
                    self.reset_game(game_state, sprites)
                    game_state.game_over = False
                    quit_game = True  # Set the flag to True to break out of both loops
                    break
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    game_state.game_over = True
                    quit_game = True
                    break
                elif event.type == pygame.QUIT:
                    game_state.game_over = True
                    quit_game = True  # Set the flag to True to break out of both loops
                    break

    def reset_game(self, game_state, sprites):
        game_state.reset(sprites)

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

        sprites = [sprite_sheet, blinky_sprite,
                   pinky_sprite, inky_sprite, clyde_sprite]

        # Set the timer to trigger after 10,000 milliseconds (10 seconds)
        timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(timer_event, 1000 * 10, 1)

        game_state = GameState(sprites)

        # Set the pacman velocity
        dx = 0
        dy = 0

        # counter used to cycle through pacman sprite animation
        counter = 0

        clock = pygame.time.Clock()

        pygame.mixer.music.load('../assets/sfx/game_start.wav')
        siren_sound = pygame.mixer.Sound('../assets/sfx/siren_1.wav')

        if settings.sound:
            pygame.mixer.music.play()
            siren_sound.play(-1)

        # Main game loop
        while not game_state.game_over:
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
                    game_state.game_over = True
                elif event.type == pygame.KEYDOWN:
                    # Move the circle based on the pressed key
                    if event.key == pygame.K_w:
                        game_state.pacman.direction = DIRECTION.UP
                        ty = -game_state.pacman.speed
                        tx = 0  # Necssarry to move only horizontal or vertical
                    elif event.key == pygame.K_s:
                        game_state.pacman.direction = DIRECTION.DOWN
                        ty = game_state.pacman.speed
                        tx = 0  # Necssarry to move only horizontal or vertical
                    elif event.key == pygame.K_a:
                        game_state.pacman.direction = DIRECTION.LEFT
                        tx = -game_state.pacman.speed
                        ty = 0  # Necssarry to move only horizontal or vertical
                    elif event.key == pygame.K_d:
                        game_state.pacman.direction = DIRECTION.RIGHT
                        tx = game_state.pacman.speed
                        ty = 0  # Necssarry to move only horizontal or vertical
                    # Check for the timer event
                if event.type == timer_event:
                    game_state.pinky.mode = MODE.CHASING
                    game_state.inky.mode = MODE.CHASING
                    game_state.blinky.mode = MODE.CHASING
                    game_state.clyde.mode = MODE.CHASING

            keys = pygame.key.get_pressed()

            # Simulates holding the key which adds better playability for pacman
            if keys[pygame.K_w]:
                game_state.pacman.direction = DIRECTION.UP
                ty = -game_state.pacman.speed
                tx = 0
            elif keys[pygame.K_s]:
                game_state.pacman.direction = DIRECTION.DOWN
                ty = game_state.pacman.speed
                tx = 0
            elif keys[pygame.K_a]:
                game_state.pacman.direction = DIRECTION.LEFT
                tx = -game_state.pacman.speed
                ty = 0
            elif keys[pygame.K_d]:
                game_state.pacman.direction = DIRECTION.RIGHT
                tx = game_state.pacman.speed
                ty = 0

            # if tx and ty doesn't lead to colliding change the current
            # dx and dy to them and other wise
            # let pacman move in his previous direction
            if game_state.pacman.check_collision(game_state, tx, ty, TILE_WIDTH, TILE_HEIGHT):
                dx = tx
                dy = ty

            if dx < 0:
                game_state.pacman.direction = DIRECTION.LEFT
            elif dx > 0:
                game_state.pacman.direction = DIRECTION.RIGHT
            elif dy < 0:
                game_state.pacman.direction = DIRECTION.UP
            elif dy > 0:
                game_state.pacman.direction = DIRECTION.DOWN

            if game_state.pacman.check_collision(game_state, dx, dy, TILE_WIDTH, TILE_HEIGHT):
                game_state.pacman.x += dx
                game_state.pacman.y += dy
                game_state.pacman.x %= 900  # logic for portal

            # Move ghosts
            game_state.blinky.move(game_state, screen)
            game_state.pinky.move(game_state, screen)
            game_state.inky.move(game_state, screen)
            game_state.clyde.move(game_state, screen)

            # Draw the map on each frame
            game_state.map.draw_map(screen)

            # Draw the game_state.pacman and the ghosts
            game_state.pacman.draw(screen, counter)
            game_state.blinky.draw(screen, game_state.pacman.powerup, counter)
            game_state.pinky.draw(screen, game_state.pacman.powerup, counter)
            game_state.inky.draw(screen, game_state.pacman.powerup, counter)
            game_state.clyde.draw(screen, game_state.pacman.powerup, counter)

            if game_state.food == 246:
                self.show_wining_screen(screen, game_state, sprites)


            if not game_state.is_pacman_alive:
                self.show_gameover_screen(
                    screen, game_state, sprites)
                game_state.is_pacman_alive = True
            else:
                # Update the screen
                pygame.display.flip()

        # Quit Pygame
        print(game_state.score)
        pygame.quit()
