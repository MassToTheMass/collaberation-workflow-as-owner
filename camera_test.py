import pygame

# Initialize Pygame
pygame.init()

# Screen and world dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WORLD_WIDTH, WORLD_HEIGHT = 2000, 2000  # Bigger world for camera movement

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Player settings
player = pygame.Rect(WORLD_WIDTH // 2, WORLD_HEIGHT // 2, 50, 50)  # Starting in the center of the world
player_speed = 5

# Camera offset
camera_x = 0
camera_y = 0

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.y -= player_speed
    if keys[pygame.K_s]:
        player.y += player_speed
    if keys[pygame.K_a]:
        player.x -= player_speed
    if keys[pygame.K_d]:
        player.x += player_speed

    # Camera follows the player
    camera_x = player.x - SCREEN_WIDTH // 2 + player.width // 2
    camera_y = player.y - SCREEN_HEIGHT // 2 + player.height // 2

    # Ensure the camera doesn't show areas outside the world
    camera_x = max(0, min(camera_x, WORLD_WIDTH - SCREEN_WIDTH))
    camera_y = max(0, min(camera_y, WORLD_HEIGHT - SCREEN_HEIGHT))

    # Fill the screen with a color (background)
    screen.fill((0, 0, 0))

    # Drawing the world (relative to the camera)
    for x in range(0, WORLD_WIDTH, 100):
        for y in range(0, WORLD_HEIGHT, 100):
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x - camera_x, y - camera_y, 100, 100), 1)

    # Draw the player (also relative to the camera)
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(player.x - camera_x, player.y - camera_y, player.width, player.height))

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()