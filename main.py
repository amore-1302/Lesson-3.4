import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/cart1.jpg")
pygame.display.set_icon(icon)
target_image = pygame.image.load("img/target.png")

TARGET_WIDTH = 80
TARGET_HEIGHT = 80

target_x = random.randint(0, SCREEN_WIDTH - TARGET_WIDTH)
target_y = random.randint(0, SCREEN_HEIGHT - TARGET_HEIGHT)
color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x <= mouse_x < target_x + TARGET_HEIGHT and target_y <= mouse_y < target_y + TARGET_HEIGHT:
                target_x = random.randint(0, SCREEN_WIDTH - TARGET_WIDTH)
                target_y = random.randint(0, SCREEN_HEIGHT - TARGET_HEIGHT)
    screen.blit(target_image, (target_x, target_y))
    pygame.display.update()

pygame.quit()