import pygame


# Initialize Pygame
pygame.init()

# Set the dimensions of the window
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Set the color of the circle
color = (255, 255, 153) # Light yellow

# Set the center position of the circle
center = [320, 240] # Center of the window
radius = 16

# Set the circle's velocity
dx = 0
dy = 0

# Set the speed of the circle's movement
speed = 10


fps = 30

clock = pygame.time.Clock()

# Checks collision with walls
def check_collision(circle_center_x, circle_center_y, dx, dy):
    # edges of the circle
    upper_circle_point = circle_center_y + radius
    lower_circle_point = circle_center_y - radius
    right_circle_point = circle_center_x + radius
    left_circle_point = circle_center_x - radius
    return upper_circle_point + dy > height or lower_circle_point + dy < 0 or right_circle_point + dx > width or left_circle_point + dx < 0 
    

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Move the circle based on the pressed key
            if event.key == pygame.K_w:
                dy = -speed
                dx = 0 # Necssarry to move only horizontal or vertical
            elif event.key == pygame.K_s:
                dy = speed
                dx = 0 # Necssarry to move only horizontal or vertical
            elif event.key == pygame.K_a:
                dx = -speed
                dy = 0 # Necssarry to move only horizontal or vertical
            elif event.key == pygame.K_d:
                dx = speed
                dy = 0 # Necssarry to move only horizontal or vertical
    
    # Update the circle's position
    if not check_collision(center[0], center[1], dx, dy):
        center[0] += dx
        center[1] += dy

    # Draw the filled circle on the screen
    screen.fill((0, 0, 0)) # Clear the screen
    pygame.draw.circle(screen, color, center, radius)

    # Update the screen
    pygame.display.flip()

    clock.tick(fps)

# Quit Pygame
pygame.quit()
