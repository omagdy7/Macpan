from enum import Enum
import pygame




# Initialize Pygame
pygame.init()

# Set the dimensions of the window
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Sprite sheet for pacman
sprite_sheet = pygame.image.load('../assets/pacman_left_sprite.png').convert_alpha();

sheet_width, sheet_height = sprite_sheet.get_size()

sprite_width, sprite_height = 32, 32

rows = sheet_height // sprite_height
columns = sheet_width // sprite_width

# Set the center position of the circle
center = [320, 240] # Center of the window
radius = 16

# Set the circle's velocity
dx = 0
dy = 0

# Set the speed of the pacman movement
speed = 5


fps = 60

clock = pygame.time.Clock()

sprites = []

class DIRECTION(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4



def get_sprites():
    for row in range(rows):
        for col in range(columns):
            x = col * sprite_width
            y = row * sprite_height
    
            # Create a new surface for the current sprite and blit it from the sprite sheet onto this new surface 
            new_sprite_surface = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA)
            new_sprite_surface.blit(sprite_sheet, (0, 0), (x, y, x + sprite_width, y +sprite_height))

            # Add this new surface to our list of sprites 
            sprites.append(new_sprite_surface)

# Checks collision with walls
def check_collision(circle_center_x, circle_center_y, dx, dy):
    # edges of the circle
    upper_circle_point = circle_center_y + radius
    lower_circle_point = circle_center_y - radius
    right_circle_point = circle_center_x + radius
    left_circle_point = circle_center_x - radius
    return upper_circle_point + dy > height or lower_circle_point + dy < 0 or right_circle_point + dx > width or left_circle_point + dx < 0 
    
get_sprites()

counter = 0

def draw_player(center, direction):
    if direction == DIRECTION.UP:
        screen.blit(pygame.transform.rotate(sprites[counter // 5], 270), center)
    elif direction == DIRECTION.DOWN:
        screen.blit(pygame.transform.rotate(sprites[counter // 5], 90), center)
    elif direction == DIRECTION.RIGHT:
        screen.blit(sprites[counter // 5], center)
    elif direction == DIRECTION.LEFT:
        screen.blit(pygame.transform.flip(sprites[counter // 5], True, False), center)




    




sprite_direction = DIRECTION.LEFT
    

# Main game loop
running = True
while running:
    # Handle events
    clock.tick(fps)

    if counter < 19:
        counter += 1
    else:
        counter = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Move the circle based on the pressed key
            if event.key == pygame.K_w:
                sprite_direction = DIRECTION.UP
                dy = -speed
                dx = 0 # Necssarry to move only horizontal or vertical
            elif event.key == pygame.K_s:
                sprite_direction = DIRECTION.DOWN
                dy = speed
                dx = 0 # Necssarry to move only horizontal or vertical
            elif event.key == pygame.K_a:
                sprite_direction = DIRECTION.RIGHT
                dx = -speed
                dy = 0 # Necssarry to move only horizontal or vertical
            elif event.key == pygame.K_d:
                sprite_direction = DIRECTION.LEFT
                dx = speed
                dy = 0 # Necssarry to move only horizontal or vertical
    
    # Update the circle's position
    if not check_collision(center[0], center[1], dx, dy):
        center[0] += dx
        center[1] += dy

    screen.fill((0, 0, 0)) # Clear the screen


    draw_player(center, sprite_direction)

    # Update the screen
    pygame.display.flip()


# Quit Pygame
pygame.quit()
