import pygame
from pygame.locals import *
from random import randint

screen_width = 800
screen_height = 600
R = 30
r = randint(0, 255)
g = randint(0, 255)
b = randint(0, 255)
ball_x, ball_y = randint(R, screen_width-30), 0
speed = 1
rect_w = 120
rect_h = 40
rect_x = 123
rect_y = screen_height - rect_h
lives = 3
score = 0

def dis_info(scr, text, pos, color = (25, 123, 255), size=33):

    pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("下落的小球")

while lives > 0:
    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        elif e.type == MOUSEMOTION:
            rect_x = e.pos[0]
    if rect_x > screen_width - rect_w:
        rect_x = screen_width - rect_w

    screen.fill((0,0,0))
    pygame.draw.circle(screen, (r, g, b), (ball_x, int(ball_y)),R)
    ball_y += speed

    if rect_x < ball_x < rect_x + rect_w and rect_y - R < ball_y <rect_y:
        score += 1
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        ball_x, ball_y = randint(R, screen_width - 30), 0
    elif ball_y > screen_height - 30:
        lives -= 1
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        ball_x, ball_y = randint(R, screen_width - 30),0

        pygame.draw.rect(screen, (255, 0, 0), (rect_x, rect_y, rect_w, rect_h))

        dis_info(screen, "Lives: {}".format(lives), (10, 10))
        dis_info(screen, "Score: {}".format(score), (screen_width - 120, 10))

        pygame.display.update()