import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("下落的小球")
ball_y = 0
ball_x = random.randint(30,770)
r = random.randint(1,255)
g = random.randint(0,255)
b = random.randint(0,255)
speed =0.4
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0,0,0))
    pygame.draw.circle(screen,(r,g,b),(ball_x,int(ball_y)),30)
    ball_y += speed
    if ball_y > 600:
        ball_y = 0
        ball_x = random.randint(30,770)
        r = random.randint(1, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        pygame.display.update()
