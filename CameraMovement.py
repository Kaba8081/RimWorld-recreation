import pygame
from os import path

pygame.init()
screen = pygame.display.set_mode((600, 600))

done = False

cameraDirection='None'

imgDir=path.join(path.dirname(__file__),'Textures')
stoneTexture=pygame.image.load(path.join(path.join(imgDir,'Grounds'),'stone01.png')).convert()
dirtTexture=pygame.image.load(path.join(path.join(imgDir,'Grounds'),'dirt01.png')).convert()    

allSprites=pygame.sprite.Group()

class Tile(pygame.sprite.Sprite):
    def __init__(self,x,y,value):
        pygame.sprite.Sprite.__init__(self)
        if value==1:
            self.image=stoneTexture
        elif value==2:
            self.image=dirtTexture
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.left=x
        self.rect.top=y
    def update(self):
        if cameraDirection=='None':
            pass
        elif cameraDirection=='N':
            self.rect.centery = self.rect.centery+5
        elif cameraDirection=='E':
            self.rect.centerx = self.rect.centerx-5
        elif cameraDirection=='S':
            self.rect.centery = self.rect.centery-5
        elif cameraDirection=='W':
            self.rect.centerx = self.rect.centerx+5

terrain=[]
x=0
x2=0
for i in range(25):
    y=0
    y2=0
    lista=[]
    for j in range(25):
        lista.append('2')
        t=Tile(x,y,2)
        allSprites.add(t)
        y=y+16
    terrain.append(lista)
    x=x+16
Keydown=False
while not done:
    CameraDirection2='None'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
        if event.type== pygame.KEYDOWN:
            Keydown=True
            if event.key == pygame.K_w:
                cameraDirection2="N"
            if event.key == pygame.K_a:
                cameraDirection2="W"
            if event.key == pygame.K_s:
                cameraDirection2="S"
            if event.key == pygame.K_d:
                cameraDirection2="E"
        if event.type == pygame.KEYUP:
            Keydown=False
    if Keydown:
        cameraDirection=cameraDirection2
    else:
        cameraDirection="None"
    screen.fill((0,0,0))
    allSprites.update()
    allSprites.draw(screen)
    pygame.display.flip()
