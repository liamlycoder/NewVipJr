import pygame
from pygame.locals import*
class MainWindow:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((800,600))
        pygame.display.set_caption('plane fighting')
        pygame.image.load(r'resources/image/shoot.png')
        self.player=player(plane_img,(200,600))
        self.img2=self.img.subsurface(pygame.Rect(0,99,102,126))
        self.screen.blit(self.img2,(200,600))
        self.plane.blit(self.img2,(.......))
    def show(self):
        while Ture:
            self.screen.fill((0,0,0))
            self.player.drawPlane(self.screen)
            pygame.display.update()
            for e in pygame.event.get():
                if e.type==QUIT:
                    exit()
class Player:
    def __init__(self,plane_img,init_pos):
        play_rect=pygame.Rect(0,99,102,126)
        selfimage=plane_img.subsurface(play_rect)
        self.rect=play_rect
        self.rect.topleft=init_pos
        self.speed=1
    def checkPressed(self):
        key_pressed=pygame.key.get_pressed()
        if key_pressed[K_UP]:
            self.player.moveup()
        if key_pressed[K_DOWN]:
            self.player.moveDown()
        if key_pressed[K_LEFT]:
            self.player.moveLeft()
        if key_pressed[K_RIGHT]:
            self.player.moveRight()
a=MainWindow()
a.show()