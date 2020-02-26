import pygame
import sys
import random

def print_text(text, pos, color = (222, 22, 2), size = 30):
    font1 = pygame.font.FONT(None, size)
    img = font1.render(text, True, color)
    c.bilt(img, pos)

rect_x = 300
rect_y = 0
rect_w = 150
rect_h = 50
c = pygame.display.set_mode((800, 600))
pygame.display.set_caption('下落的小球')
pygame.init
while True:
    for e in pygame.event.get():
       if e.type == pygame.QUIT:
           pygame.quit()
           sys.exit

    ball_y += 1
    if ball_y > 600:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        ball_x = random.randint(30, 770)
        ball_y = 30

    c.fill((0, 0, 0))
    pygame.draw.circle(c, (r, g, b), (ball_x, ball_y), 30)
    pygame.draw.rect(c, (255,0, 0), )
    print_text('Lives:3', (0, 0))
    print_text('Score:', (0, 0), )
    pygame.display.update
