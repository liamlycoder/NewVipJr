import pygame
from pygame.locals import*
class MainWindow:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((800,600))
        pygame.display.set_caption('plane fighting')
    def show(self):
        for e in pygame.event.get():
            if e.type==QUIT:
                exit()
a=MainWindow()
a.show()