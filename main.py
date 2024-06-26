import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Tire Game")
icon = pygame.image.load('image/icon.jpg')
pygame.display.set_icon(icon)


target_image = pygame.image.load('image/target.png')
target_width = 71
target_height = 50

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
color = random.choice(['blue', 'green', 'red', 'yellow', 'purple', 'orange'])





running = True
tire_count = 0
tire_count2 = 0
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                tire_count += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
            else:
                tire_count2 += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    screen.blit(target_image, (target_x, target_y))
    pygame.display.update()




pygame.quit()
print(f"Вы попали в мишень {tire_count} раз")
print(f"Вы попали мимо мишени {tire_count2} раз")