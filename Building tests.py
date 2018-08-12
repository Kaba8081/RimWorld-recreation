import pygame
from os import path
done=False
pygame.init()
Resolution=624
screen = pygame.display.set_mode((Resolution, Resolution)) # okno gry
allSprites=pygame.sprite.Group() # główna grupa spritów 
imgDir= path.join(path.dirname(__file__),'Textures') #folder tekstur

missing=pygame.image.load(path.join(imgDir,'MissingTexture.png'))#[

index=1
rocks=[]
for i in range(17):
    rocks.append(pygame.image.load(path.join(path.join(path.join(path.dirname(__file__),'Textures'),'Rocks'),'Rock'+str(index)+'.png')).convert())
    index=index+1
#] - wczytywanie teksutr
class Tile(pygame.sprite.Sprite): # klasa do tworzenia tilów na mapie
    def __init__(self,value,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16,16))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.image=value
        self.rect.top=y
        self.rect.left=x
    def StructureInit(self,value,terrain,x,y): # inicjalizacja struktur i dobieranie odpowiednich tekstur
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
                        lista.append('x')
                    elif neighbourX<0 or neighbourY<0 or neighbourX>623 or neighbourY>623:
                        pass
                    elif terrain[neighbourX][neighbourY]!='-':
                        lista.append(1)
                    elif terrain[neighbourX][neighbourY]=='-':
                        lista.append(0)
                    y2=y2+1
                Neighbours.append(lista)
                x2=x2+1
            return Neighbours
        def CombinationChecking(Neighbours):
            if len(Neighbours[0])<3 or len(Neighbours[1])<3 or len(Neighbours[2])<3:
                pass
            elif Neighbours[0][1]==1 and Neighbours[1][0]==1 and Neighbours[1][2]==1 and Neighbours[2][1]==1:
                self.image=rocks[16]
            elif Neighbours[0][1]==0 and Neighbours[1][0]==0 and Neighbours[1][2]==0 and Neighbours[2][1]==0:
                self.image=rocks[8]
            elif Neighbours[0][1]==0 and Neighbours[1][0]==1 and Neighbours[1][2]==0 and Neighbours[2][1]==0:
                self.image=rocks[6]
            elif Neighbours[0][1]==0 and Neighbours[1][0]==0 and Neighbours[1][2]==0 and Neighbours[2][1]==1:
                self.image=rocks[7]
            elif Neighbours[0][1]==0 and Neighbours[1][0]==0 and Neighbours[1][2]==1 and Neighbours[2][1]==0:
                self.image=rocks[4]
            elif Neighbours[0][1]==1 and Neighbours[1][0]==0 and Neighbours[1][2]==0 and Neighbours[2][1]==0:
                self.image=rocks[5]
            elif Neighbours[0][1]==0 and Neighbours[1][0]==1 and Neighbours[1][2]==0 and Neighbours[2][1]==1:
                self.image=rocks[11]
            elif Neighbours[0][1]==0 and Neighbours[1][0]==0 and Neighbours[1][2]==1 and Neighbours[2][1]==1:
                self.image=rocks[2]
            elif Neighbours[0][1]==1 and Neighbours[1][0]==0 and Neighbours[1][2]==1 and Neighbours[2][1]==0:
                self.image=rocks[1]
            elif Neighbours[0][1]==1 and Neighbours[1][0]==1 and Neighbours[1][2]==0 and Neighbours[2][1]==0:
                self.image=rocks[12]
            elif Neighbours[0][1]==0 and Neighbours[1][0]==1 and Neighbours[1][2]==1 and Neighbours[2][1]==0:
                self.image=rocks[0]
            elif Neighbours[0][1]==1 and Neighbours[1][0]==0 and Neighbours[1][2]==0 and Neighbours[2][1]==1:
                self.image=rocks[3]
            elif Neighbours[0][1]==0 and Neighbours[1][0]==1 and Neighbours[1][2]==1 and Neighbours[2][1]==1:
                self.image=rocks[10]
            elif Neighbours[0][1]==1 and Neighbours[1][0]==1 and Neighbours[1][2]==1 and Neighbours[2][1]==0:
                self.image=rocks[9]
            elif Neighbours[0][1]==1 and Neighbours[1][0]==1 and Neighbours[1][2]==0 and Neighbours[2][1]==1:
                self.image=rocks[14]
            elif Neighbours[0][1]==1 and Neighbours[1][0]==0 and Neighbours[1][2]==1 and Neighbours[2][1]==1:
                self.image=rocks[15]
        a=CheckNeighbours(terrain,x,y)
        b=CombinationChecking(a)
terrain=[]
x=0
for i in range(100): # wypełnianie mapy teksturami
    y=0
    lista=[]
    for j in range(100):
        lista.append('-')
        t=Tile(missing,x,y)
        allSprites.add(t)
        y=y+16
    terrain.append(lista)
    x=x+16
while not done: # główna pętla gry
    x2=0
    y2=0
    z=0
    # Input
    for event in pygame.event.get(): # wydarzenia
        if event.type == pygame.QUIT: # wyjście
            done = True
            pygame.quit()
        if event.type== pygame.MOUSEBUTTONDOWN: # naciśnięcie przycisku myszy
            if pygame.mouse.get_pressed()[0]==1: # ppm
                a=int(pygame.mouse.get_pos()[0]/16)
                b=int(pygame.mouse.get_pos()[1]/16)
                for i in range(a):
                    x2=x2+16
                for j in range(b):
                    y2=y2+16
                z=1
            elif pygame.mouse.get_pressed()[2]==1: # lpm
                a=int(pygame.mouse.get_pos()[0]/16)
                b=int(pygame.mouse.get_pos()[1]/16)
                for i in range(a):
                    x2=x2+16
                for j in range(b):
                    y2=y2+16
                z=2
    # Update
    if z==1: #[
        terrain[a][b]=1
        t=Tile(rocks[8],x2,y2)
        allSprites.add(t)
        t.StructureInit(0,terrain,int(x2/16),int(y2/16))
    if z==2:
        terrain[a][b]=0
        t=Tile(missing,x2,y2)
        allSprites.add(t) #] - podmienianie tilów na mapie
    x=0
    for i in range(len(terrain)):
        y=0
        for j in range(len(terrain[0])):
            if terrain[x][y]==1:
                t=Tile(rocks[8],x*16,y*16)
                t.StructureInit(0,terrain,x,y)
                allSprites.add(t)
            y=y+1
        x=x+1
    # drawing 
    allSprites.draw(screen)#
    pygame.display.flip()  # wyświetlanie wszystkiego na ekranie
    
