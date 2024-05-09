import sys
import random
import pygame
from pygame import Surface, SurfaceType

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 1600
HEIGHT = 1600
WORLD_WIDTH = 3200 # new constant
WORLD_HEIGHT = 3200  # new constant
SPEED = 2

# Set up the display
screen: Surface | SurfaceType = pygame.display.set_mode((WIDTH, HEIGHT))

# Load the background texture
background_texture = pygame.image.load('background_texture.png')

# Load the player texture
player_texture = pygame.image.load('player_texture.png')

# Load the tree texture
tree_texture = pygame.image.load('tree_texture.png')

# Load the rock texture
rock_texture = pygame.image.load('rock_texture.png')

# Load the boundary texture
boundary_texture = pygame.image.load('boundary_texture.png')



    screen.blit(boundary_texture, (0, 0))  # Draw the top boundary
    screen.blit(boundary_texture, (0, HEIGHT - boundary_texture.get_height()))  # Draw the bottom boundary
    screen.blit(boundary_texture, (0, 0), (0, 0, boundary_texture.get_width(), boundary_texture.get_height()))  # Draw the left boundary
    screen.blit(boundary_texture, (WIDTH - boundary_texture.get_width(), 0), (0, 0, boundary_texture.get_width(), boundary_texture.get_height()))

# Set up the player
player = player_texture.get_rect(center=(WIDTH / 2, HEIGHT / 2))

# Set up the trees
trees = [tree_texture.get_rect(center=(random.randint(0, WIDTH), random.randint(0, HEIGHT))) for _ in range(10)]

# Set up the rocks
rocks = [rock_texture.get_rect(center=(random.randint(0, WIDTH), random.randint(0, HEIGHT))) for _ in range(10)]

# ...

# Set up the camera
# Set up the camera
camera_x = 0
camera_y = 0

try:
    while True:
        # your game loop code here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get a list of all keys currently being pressed down
        keys = pygame.key.get_pressed()

        # Move the player
        if keys[pygame.K_UP]:
            player.y -= SPEED
        if keys[pygame.K_DOWN]:
            player.y += SPEED
        if keys[pygame.K_LEFT]:
            player.x -= SPEED
        if keys[pygame.K_RIGHT]:
            player.x += SPEED

        # Update the camera position
        camera_x = max(0, min(player.x - WIDTH / 2, WORLD_WIDTH - WIDTH))
        camera_y = max(0, min(player.y - HEIGHT / 2, WORLD_HEIGHT - HEIGHT))

        # Draw everything
        screen.blit(background_texture, (-camera_x, -camera_y))  # Draw the background
        screen.blit(player_texture, (player.x - camera_x, player.y - camera_y))  # Draw the player
        for tree in trees:
            screen.blit(tree_texture, (tree.x - camera_x, tree.y - camera_y))  # Draw the trees
        for rock in rocks:
            screen.blit(rock_texture, (rock.x - camera_x, rock.y - camera_y))  # Draw the rocks

        # Update the display
        pygame.display.flip()
except KeyboardInterrupt:
    print("Program interrupted by user")
    pygame.quit()
    sys.exit()