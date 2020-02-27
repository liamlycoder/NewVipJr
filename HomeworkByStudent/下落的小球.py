import pygame
import sys
import random

def print_text(text, pos, color = (222, 22, 2), size = 30):
    font1 = pygame.font.Font(None, size)
    img = font1.render(text, True, color)
    c.blit(img, pos)
lives, scores = 3, 0
r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255),
ball_x, ball_y = random.randint(30, 770),0
rect_x = 300
rect_y = 550
rect_w = 150
rect_h = 50
pygame.init()
c = pygame.display.set_mode((800, 600))
pygame.display.set_caption('下落的小球')

while True:
    for e in pygame.event.get():
       if e.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
       if e.type == pygame.MOUSEMOTION:
           rect_x = e.pos(0)
    if rect_x > 650:
        rect_x = 650
    if (rect_y - ball_y < 30) and (ball_x < rect_x + rect_w):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        ball_x = random.randint(30, 770)
        ball_y = 30
        scores +=1

    elif ball_y > 600:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        ball_x = random.randint(30, 770)
        ball_y = 30
        lives -= 1

    ball_y += 1
    if ball_y > 600:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        ball_x = random.randint(30, 770)
        ball_y = 30

    c.fill((0, 0, 0))
    pygame.draw.circle(c, (r, g, b), int(ball_x), int(ball_y), 30)
    pygame.draw.rect(c, (255,0, 0), )
    print_text('Lives: {}'.format(lives), (0, 0))
    print_text('Score: {}'.format(scores), (700, 0))
    pygame.display.update()