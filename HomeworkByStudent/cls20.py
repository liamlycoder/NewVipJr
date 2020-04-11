import pygame
import sys
import random
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("下落的小球")
ball_x, ball_y = 400, 30
R = random.randint(0, 255)
G = random.randint(0, 255)
B = random.randint(0, 255)
rect_x, rect_y, rect_w, rect_h = 340, 560, 120, 40
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.MOUSEMOTION:
            rect_x = e.pos[0]
    screen.fill((0, 0, 0))
    ball_y += 1
    font1 = pygame.font.Font(None, 30)
    img_text = font1.render("Life:3", True, (255, 255, 0))
    screen.blit(img_text, (10, 10))
    font1 = pygame.font.Font(None, 30)
    img_text = font1.render("Score:0", True, (255, 255, 0))
    screen.blit(img_text, (720, 10))
    pygame.draw.circle(screen, (R, G, B), (ball_x, ball_y), 30)
    pygame.draw.rect(screen, (255, 0, 0), (rect_x, rect_y, rect_w, rect_h))
    if rect_x > 680:
        rect_x = 680
    if ball_y > 600:
        ball_y = 30
        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)
        ball_x = random.randint(30, 770)
    pygame.display.update()
