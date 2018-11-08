import pygame
from os import path

pygame.init()
pygame.font.init()

Resolution=(624,624)
screen = pygame.display.set_mode(Resolution)
allSprites = pygame.sprite.Group()
imgDir = path.join(path.dirname(__file__),'Textures')

done = False

missing = pygame.image.load(path.join(imgDir,'MissingTexture.png'))
buildingShadow = pygame.image.load(path.join(imgDir,'BuildShadow.png'))

rocks=[]
wood=[]
floors=[]

for i in range(25):
    rocks.append(pygame.image.load(path.join(path.join(imgDir,'Rocks'),'Rock'+str(i+1)+'.png')).convert())
for i in range(25):
    wood.append(pygame.image.load(path.join(path.join(path.join(imgDir,'walls'),'Wood'),'WoodenWall_'+str(i+1)+'.png')).convert())
for i in range(3):
    floors.append(pygame.image.load(path.join(path.join(imgDir,'Floors'),'Carpet'+str(i+1)+'.png')).convert())
floors.append(pygame.image.load(path.join(path.join(imgDir,'Floors'),'Concrete.png')).convert())
floors.append(pygame.image.load(path.join(path.join(imgDir,'Floors'),'stone.png')).convert())
floors.append(pygame.image.load(path.join(path.join(imgDir,'Floors'),'Wood.png')).convert())

class Tile(pygame.sprite.Sprite):
    def __init__(self,value,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16,16))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.image = value
        self.rect.top = y
        self.rect.left = x
    def WallsUpdate(self):
        pass

terrain = []
# Wypełnianie mapy teksturami
