import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Tire Game")
icon = pygame.image.load('image/icon.png')
pygame.display.set_icon(icon)


target_image = pygame.image.load('image/target.png')
target_width = 71
target_height = 50

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
color = random.choice(['blue', 'green', 'red', 'yellow', 'purple', 'orange'])





running = True
while running:
    pass
pygame.quit()