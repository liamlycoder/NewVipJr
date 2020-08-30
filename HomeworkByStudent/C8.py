import pygame as g
import random as r

from pygame.constants import K_LEFT, K_RIGHT


def display_text(scr, text, pos, size=30, color=(100, 0, 250)):
    myfont = g.font.Font(r"C:\Windows\Fonts\simsun.ttc", size)
    img = myfont.render(text, True, color)
    scr.blit(img, pos)


wide = 800
hight = 600
R = 30
X, Y = r.randint(30, 770), -30
lives = 3
scores = 0
speed = 3
mspeed=3
c1, c2, c3 = r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)
rect_x, rect_y, rect_h, rect_w = 360, 570, 30, 80


g.init()
s = g.display.set_mode((wide, hight))
g.display.set_caption("Drop Ball")

while True:
    for e in g.event.get():
        if e.type == g.QUIT:
            exit()
        elif e.type==g.MOUSEMOTION:
            rect_x=g.event.pos[0]

    Y += speed
    s.fill((255, 255, 255))
    g.draw.circle(s, (c1, c2, c3), (int(X), int(Y)), R)
    if Y > 830:
        X, Y = r.randint(30, 770), -30
        c1, c2, c3 = r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)
        lives -= 1

    display_text(s, "lives:{}".format(lives), (0, 0))
    display_text(s, "scores:{}".format(scores), (670, 0))

    if 0 > rect_x:
        rect_x = 0
    elif rect_x > wide-80:
        rect_x = wide - rect_w
    else:
        pass

    g.draw.rect(s, (0, 0, 0), (rect_x, rect_y, rect_w, rect_h))

    keys = g.key.get_pressed()
    if keys[K_LEFT]:
        rect_x -= mspeed
    if keys[K_RIGHT]:
        rect_x += mspeed
    #if keys[K_ESC]:
     #   exit()

    g.display.update()
