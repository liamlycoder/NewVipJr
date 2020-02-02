# !/usr/bin/python
# coding: utf8
# Time: 2020/2/2 14:54
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import pygame
import sys
import random


def print_text(scr, font, x, y, text, color=(250, 25, 255)):
    imgText = font.render(text, True, color)
    scr.blit(imgText, (x, y))


def PlayGame(scr, lives, score):
    black, white = (0, 0, 0), (255, 255, 255)
    r, g, b = random.randint(1, 255), random.randint(0, 255), random.randint(0, 255)
    ball_x, ball_y = random.randint(30, 770), 0
    rect_x, rect_y, rect_w, rect_h = 43, 560, 120, 40
    speed = 14

    while lives > 0:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif e.type == pygame.MOUSEMOTION:
                rect_x = e.pos[0]

        # 键盘控制
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_LEFT]:
            rect_x -= 2
        if keys[pygame.K_RIGHT]:
            rect_x += 2

        if rect_x > 680:
            rect_x = 680

        scr.fill(black)
        pygame.draw.circle(scr, (r, g, b), (int(ball_x), int(ball_y)), 30, 0)
        pygame.draw.rect(scr, white, (rect_x, rect_y, rect_w, rect_h), 0)

        ball_y += speed
        if ball_y > 600:
            lives -= 1
            speed = speed + score / 3
            r, g, b = random.randint(1, 255), random.randint(0, 255), random.randint(0, 255)
            ball_x, ball_y = random.randint(30, 770), 0
        elif (rect_y - ball_y) < 30 and rect_x < ball_x < rect_x + rect_w:
            r, g, b = random.randint(1, 255), random.randint(0, 255), random.randint(0, 255)
            ball_x, ball_y = random.randint(30, 770), 0
            score += 1
        else:
            ball_y += speed
        print_text(scr, font1, 0, 0, "Lives: {}".format(lives))
        print_text(scr, font1, 720, 0, "Score: {}".format(score))
        pygame.display.update()
    return lives, score


pygame.init()
pygame.display.set_caption("Drop Ball")
screen = pygame.display.set_mode((800, 600))
font1 = pygame.font.Font(None, 24)
lives, score = 3, 0
while True:
    lives, score = PlayGame(screen, lives, score)
    for e in pygame.event.get():
        if e.type == pygame.MOUSEBUTTONUP:
            lives, score = 3, 0
        elif e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 0))
    print_text(screen, font1, 350, 320, "GAME OVER!")
    print_text(screen, font1, 340, 340, "Score:{} <Replay>".format(score))
    pygame.display.update()
