# !/usr/bin/python
# coding: utf8
# Time: 2020/2/1 14:47
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import pygame
import sys
import random

def print_text(scr, font, x, y, text, color=(250, 25, 255)):
    imgText = font.render(text, True, color)
    scr.blit(imgText, (x, y))

pygame.init()
pygame.display.set_caption("Drop Ball")
screen = pygame.display.set_mode((800, 600))
black, white = (0, 0, 0), (255, 255, 255)
r, g, b = random.randint(1, 255), random.randint(0, 255), random.randint(0, 255)
ball_x, ball_y = random.randint(30, 770), 0
rect_x, rect_y, rect_w, rect_h = 43, 560, 120, 40
font1 = pygame.font.Font(None, 24)
speed = 3

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif e.type == pygame.MOUSEMOTION:
            rect_x = e.pos[0]
    if rect_x > 680:
        rect_x = 680

    screen.fill(black)
    pygame.draw.circle(screen, (r, g, b), (int(ball_x), int(ball_y)), 30, 0)
    pygame.draw.rect(screen, white, (rect_x, rect_y, rect_w, rect_h), 0)

    ball_y += speed
    if ball_y > 600:
        r, g, b = random.randint(1, 255), random.randint(0, 255), random.randint(0, 255)
        ball_x, ball_y = random.randint(30, 770), 0
    elif (rect_y - ball_y) < 30 and rect_x < ball_x < rect_x + rect_w:
        r, g, b = random.randint(1, 255), random.randint(0, 255), random.randint(0, 255)
        ball_x, ball_y = random.randint(30, 770), 0
    else:
        ball_y += speed

    print_text(screen, font1, 0, 0, "Life: 3")
    print_text(screen, font1, 700, 0, "Score: 0")


    pygame.display.update()


