import pygame
from pygame.locals import *
SCREEN_HEIGHT=800
SCREEN_WEIGHT=480
class Player:
    def __init__(self,plane_img,init_pos):
        player_rect=[]
        player_rect.append(pygame.Rect(0,99,102,126))
        player_rect.append(pygame.Rect(165,360,102,126))
        self.image=[]
        for i in range(2):
            self.image.append(plane_img.subsurface(player_rect[i]))
        self.img_index=1
        self.rect=player_rect[0]
        self.rect.topleft=init_pos
        self.speed=1
    def drawplane(self,scr):
        self.img_index+=1
        if self.img_index>=2:
            self.img_index=0
        scr.blit(self.image[self.img_index],self.rect)
    def moveUP(self):
        if self.rect.top<=0:
            self.rect.top=0
        self.rect.top-=self.speed
    def moveDOWN(self):
        if self.rect.bottom>=SCREEN_HEIGHT:
            self.rect.bottom=SCREEN_HEIGHT
        self.rect.top+=self.speed
    def moveLEFT(self):
        if self.rect.left <= 0:
            self.rect.left=0
        self.rect.left -= self.speed
    def moveRIGHT(self):
        if self.rect.right >= SCREEN_WEIGHT:
            self.rect.right = SCREEN_WEIGHT
        self.rect.right += self.speed
class MainWindow:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((SCREEN_WEIGHT,SCREEN_HEIGHT))
        pygame.display.set_caption('plane fighting')
        plane_img=pygame.image.load(r'resources/image/shoot.png')
        self.player=Player(plane_img,[200,600])
    def show(self):
        while True:
            for e in pygame.event.get():
                if e.type == QUIT:
                    exit()
            self.screen.fill((0,0,0))
            self.player.drawplane(self.screen)
            self.checkPressed()
            pygame.display.update()
    def checkPressed(self):
        key_pressed=pygame.key.get_pressed()
        if key_pressed[K_UP]:
            self.player.moveUP()
        if key_pressed[K_DOWN]:
            self.player.moveDOWN()
        if key_pressed[K_LEFT]:
            self.player.moveLEFT()
        if key_pressed[K_RIGHT]:
            self.player.moveRIGHT()

game=MainWindow()
game.show()
