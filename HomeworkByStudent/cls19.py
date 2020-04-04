import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("下落的小球")
x = 20
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0, 0, 0))
    x += 1
    pygame.draw.circle(screen, (255, 255, 0), (x, 60), 30)
    pygame.display.update()
