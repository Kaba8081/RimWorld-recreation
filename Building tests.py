import pygame
from os import path
done=False
pygame.init()
Resolution=624
screen = pygame.display.set_mode((Resolution, Resolution))
allSprites=pygame.sprite.Group()
imgDir= path.join(path.dirname(__file__),'Textures')

missing=pygame.image.load(path.join(imgDir,'MissingTexture.png'))

rock=pygame.image.load(path.join(path.join(path.join(path.dirname(__file__),'Textures'),'Rocks'),'Rock9.png')).convert()

class Tile(pygame.sprite.Sprite):
    def __init__(self,value,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16,16))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.image=value
        self.rect.top=y
        self.rect.left=x
    def StructureInit(self,value,terrain,x,y):
        def CheckNeighbours(terrain,x,y):
            Neighbours=[]
            Combination=0
            x2=-1
            for a in range(3):
                y2=-1
                lista=[]
                for b in range(3):
                    neighbourX=x+x2
                    neighbourY=y+y2
                    if x2==0 and y2==0:
                        pass
                    elif neighbourX<0 or neighbourY<0 or neighbourX>x2-1 or neighbourY>y2-1:
                        pass
                    elif terrain[neighbourX][neighbourY]!='-':
                        lista.append(1)
                    elif terrain[neighbourX][neighbourY]=='-':
                        lista.append(0)
                Neighbours.append(lista)
            return Neighbours
        a=CheckNeighbours(terrain,x,y)
        print(a)
terrain=[]
x=0
for i in range(100):
    y=0
    lista=[]
    for j in range(100):
        lista.append('-')
        t=Tile(missing,x,y)
        allSprites.add(t)
        y=y+16
    terrain.append(lista)
    x=x+16
while not done:
    x2=0
    y2=0
    z=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
        if event.type== pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]==1:
                a=int(pygame.mouse.get_pos()[0]/16)
                b=int(pygame.mouse.get_pos()[1]/16)
                for i in range(a):
                    x2=x2+16
                for j in range(b):
                    y2=y2+16
                z=1
            elif pygame.mouse.get_pressed()[2]==1:
                a=int(pygame.mouse.get_pos()[0]/16)
                b=int(pygame.mouse.get_pos()[1]/16)
                for i in range(a):
                    x2=x2+16
                for j in range(b):
                    y2=y2+16
                z=2

    if z==1:
        t=Tile(rock,x2,y2)
        allSprites.add(t)
        t.StructureInit(0,terrain,x2,y2)
    if z==2:
        t=Tile(missing,x2,y2)
        allSprites.add(t)
    #print(int(pygame.mouse.get_pos()[0]/16))
    allSprites.draw(screen)
    pygame.display.flip()
    
