import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((1000, 850))
pygame.display.set_caption('小球落下')
color = (78, 90, 5)
colour = (0, 0, 0)
x = 40
y = 40
# 长方形的位置
# ——-——-——-——-——-——
rect_x = 50
rect_y = 770
# ——-——-——-——-——-——
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
    screen.fill((230, 230, 230))
    w = pygame.draw.circle(screen, color, (int(x), int(y)), 40)
    y += 1
    if y > 810:
        y = random.randint(40, 810)
        x = random.randint(40, 1000)
        color = (random.randint(0, 225), random.randint(0, 225), random.randint(0, 225))
    pygame.display.flip()
