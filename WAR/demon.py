# !/usr/bin/python
# coding: utf8
# Time: 2020/1/19 10:13
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import pygame
from pygame.locals import *

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("飞机大战")

while True:
    screen.fill((255, 255, 255))
    plane_img = pygame.image.load("images/myPlane.png")
    img = plane_img.subsurface(Rect(0, 99, 102, 126))
    screen.blit(img, (200, 300))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()

