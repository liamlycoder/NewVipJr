import pygame
import sys
import random

r = radint(0, 255)
g = radint(0, 255)
b = radint(0, 255)

ball_x = 400
ball_y = 30

c = pygame.display.set_mode(800, 600)
pygame.display.set_caption('下落的小球')

while True:
    for e in pygame.event.get():
       if e.type == pygame.QUIT:
           pygame.quit()
           eyes.exit
    ball_y += 1
    if ball_y > 600:
        ball_x = radint(30, 770)
        ball_y = 0

    c.fill((0, 0, 0))
    pygame.draw.circle(c, (r, g, b), (ball_x, ball_y), 30)
    pygame.display.update
