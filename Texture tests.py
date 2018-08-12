import pygame
from os import path
pygame.init()
screen = pygame.display.set_mode((624, 624))
WimgDir= path.join(path.join(path.join(path.dirname(__file__),'Textures'),'walls'),'Wood')
allSprites = pygame.sprite.Group()
done=False
page=1
index2=1
ww=[]
for i in range(14):
     ww.append(pygame.image.load(path.join(WimgDir,'WoodenWall_'+str(index2)+'.png')).convert())
     ww[index2-1].convert_alpha()
     index2=index2+1
class Tile(pygame.sprite.Sprite):
    def __init__(self,value,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16,16))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.image= value
        self.image = pygame.transform.scale(self.image,(48,48))
        self.rect.top=y
        self.rect.left=x
index=0
x=0
y=0
for i in range(13):
    t=Tile(ww[index],x,y)
    allSprites.add(t)
    y=y+48
    index=index+1
x=48
y=0
for i in range(1):
    t=Tile(ww[index],x,y)
    allSprites.add(t)
    y=y+48
    index=index+1

def Page2():
    index=1
    index2=1
    rt=[]
    ndat=[]
    for i in range(14): # Rocks
        try:
            rt.append(pygame.image.load(path.join(path.join(path.join(path.dirname(__file__),'Textures'),'Rocks'),'Rock'+str(index)+'.png')).convert())
        except pygame.error:
            rt.append(pygame.image.load(path.join(path.join(path.dirname(__file__),'Textures'),'MissingTexture.png')).convert())
        index=index+1
    for i in range(5): # Not discovered areas
        try:
            ndat.append(pygame.image.load(path.join(path.join(path.join(path.dirname(__file__),'Textures'),'Rocks'),'NotDiscoveredArea'+str(index2)+'.png')).convert_alpha())
        except pygame.error:
            ndat.append(pygame.image.load(path.join(path.join(path.dirname(__file__),'Textures'),'MissingTexture.png')).convert())
        index2=index2+1
    index3=0
    x=0
    y=0
    for i in range(13):
        t=Tile(rt[index3],x,y)
        allSprites.add(t)
        y=y+48
        index3=index3+1
    x=48
    y=0
    for i in range(1):
        t=Tile(rt[index3],x,y)
        allSprites.add(t)
        y=y+48
        index3=index3+1
    index3=0
    x=96
    y=0
    for i in range(5):
        t=Tile(ndat[index3],x,y)
        allSprites.add(t)
        y=y+48
        index3=index3+1
        
def Page3():
    index=1
    ft=[]
    for i in range(3):
        ft.append(pygame.image.load(path.join(path.join(path.join(path.dirname(__file__),'Textures'),'Floors'),'Carpet'+str(index)+'.png')).convert())
        index=index+1
    ft.append(pygame.image.load(path.join(path.join(path.join(path.dirname(__file__),'Textures'),'Floors'),'stone.png')).convert())
    ft.append(pygame.image.load(path.join(path.join(path.join(path.dirname(__file__),'Textures'),'Floors'),'Concrete.png')).convert())
    ft.append(pygame.image.load(path.join(path.join(path.join(path.dirname(__file__),'Textures'),'Floors'),'Wood.png')).convert())
    index2=0
    x=0
    y=0
    for i in range(6):
        t=Tile(ft[index2],x,y)
        allSprites.add(t)
        y=y+48
        index2=index2+1
while not done:
    screen.fill((0,0,0))
    allSprites.draw(screen)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if page==2 or page>2:
                pygame.quit()
                done=True
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_1:
                page=1
            if event.key == pygame.K_2:
                page=2
                Page2()
            if event.key == pygame.K_3:
                page=3
                Page3()

