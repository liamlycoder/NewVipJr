import pygame as g
import random as r

from pygame.constants import *


def game(speed,scr,lives,scores):


    R = 30
    ball_x, ball_y = r.randint(30, 770), -30
    mspeed = 3
    c1, c2, c3 = r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)
    rect_x, rect_y, rect_h, rect_w = 360, 570, 30, 80

    g.init()
    g.display.set_caption("Drop Ball")

    while lives>0:
        for e in g.event.get():
            if e.type == g.QUIT:
                exit()
            elif e.type == g.MOUSEMOTION:
                rect_x = e.pos[0]

        scr.fill((255, 255, 255))
        g.draw.circle(scr, (c1, c2, c3), (int(ball_x), int(ball_y)), R)
        ball_y += speed

        if ball_y > 830:
            ball_x, ball_y = r.randint(30, 770), -30
            c1, c2, c3 = r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)
            lives-=1
        elif rect_x < ball_x < rect_x + rect_w and ball_y == rect_y - R:
            ball_x, ball_y = r.randint(30, 770), -30
            c1, c2, c3 = r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)
            scores += 1

        display_text(scr, "lives:{}".format(lives), (0, 0))
        display_text(scr, "scores:{}".format(scores), (670, 0))

        if 0 > rect_x:
            rect_x = 0
        elif rect_x > wide - 80:
            rect_x = wide - rect_w
        else:
            pass

        g.draw.rect(scr, (0, 0, 0), (rect_x, rect_y, rect_w, rect_h))

        keys = g.key.get_pressed()
        if keys[K_LEFT]:
            rect_x -= mspeed
        if keys[K_RIGHT]:
            rect_x += mspeed
        if keys[K_ESCAPE]:
            exit()

        g.display.update()
    return lives,scores
def display_text(screen, text, pos, size=30, color=(100, 0, 250)):
    myfont = g.font.Font(r"C:\Windows\Fonts\simsun.ttc", size)
    img = myfont.render(text, True, color)
    screen.blit(img, pos)

lives = 3
scores = 0
wide = 800
hight = 600
s1 = g.display.set_mode((wide, hight))
s2=g.display.set_mode((wide, hight))

while True:
    lives,scores=game(3,s1,lives,scores)

    for i in g.event.get():
        if i.type==MOUSEBUTTONDOWN:
            lives,scores=3,0

    g.init()
    sc.fill((255,0,0))
    display_text(sc,'GAME OVER',(400,300),color=(255,255,255),size=40)
    display_text("scores={}<retry>".format(scores),(400,300))