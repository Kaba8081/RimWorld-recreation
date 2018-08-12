import pygame
from os import path
done=False
pygame.init()
pygame.font.init()
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
index=1
wood=[]
for i in range(17):
    wood.append(pygame.image.load(path.join(path.join(path.join(path.join(path.dirname(__file__),'Textures'),'walls'),'Wood'),'WoodenWall_'+str(index)+'.png')).convert())
    index+=1
index=2
floors=[]
for i in range(2):
    floors.append(pygame.image.load(path.join(path.join(path.join(path.dirname(__file__),'Textures'),'Floors'),'Carpet'+str(index)+'.png')).convert())
    index+=1
floors.append(pygame.image.load(path.join(path.join(path.join(path.dirname(__file__),'Textures'),'Floors'),'Concrete.png')).convert())
floors.append(pygame.image.load(path.join(path.join(path.join(path.dirname(__file__),'Textures'),'Floors'),'stone.png')).convert())
floors.append(pygame.image.load(path.join(path.join(path.join(path.dirname(__file__),'Textures'),'Floors'),'Wood.png')).convert())
print(floors)
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
    def StructureInit(self,lista,terrain,x,y,*value): # inicjalizacja struktur i dobieranie odpowiednich tekstur
        def Floors(terrain,x,y,lista,value):
            print(value)
            if value==3:
                self.image=lista[0]
            if value==4:
                self.image=lista[1]
            if value==5:
                self.image=lista[2]
            if value==6:
                self.image=lista[3]
            if value==7:
                self.image=lista[4]
            if value==8:
                self.image=lista[5]
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
        def CombinationChecking(Neighbours,lista):
            if len(Neighbours[0])<3 or len(Neighbours[1])<3 or len(Neighbours[2])<3:
                pass
            elif Neighbours[0][1]==1 and Neighbours[1][0]==1 and Neighbours[1][2]==1 and Neighbours[2][1]==1:
                self.image=lista[16]
            elif Neighbours[0][1]==0 and Neighbours[1][0]==0 and Neighbours[1][2]==0 and Neighbours[2][1]==0:
                self.image=lista[8]
            elif Neighbours[0][1]==0 and Neighbours[1][0]==1 and Neighbours[1][2]==0 and Neighbours[2][1]==0:
                self.image=lista[6]
            elif Neighbours[0][1]==0 and Neighbours[1][0]==0 and Neighbours[1][2]==0 and Neighbours[2][1]==1:
                self.image=lista[7]
            elif Neighbours[0][1]==0 and Neighbours[1][0]==0 and Neighbours[1][2]==1 and Neighbours[2][1]==0:
                self.image=lista[4]
            elif Neighbours[0][1]==1 and Neighbours[1][0]==0 and Neighbours[1][2]==0 and Neighbours[2][1]==0:
                self.image=lista[5]
            elif Neighbours[0][1]==0 and Neighbours[1][0]==1 and Neighbours[1][2]==0 and Neighbours[2][1]==1:
                self.image=lista[11]
            elif Neighbours[0][1]==0 and Neighbours[1][0]==0 and Neighbours[1][2]==1 and Neighbours[2][1]==1:
                self.image=lista[2]
            elif Neighbours[0][1]==1 and Neighbours[1][0]==0 and Neighbours[1][2]==1 and Neighbours[2][1]==0:
                self.image=lista[1]
            elif Neighbours[0][1]==1 and Neighbours[1][0]==1 and Neighbours[1][2]==0 and Neighbours[2][1]==0:
                self.image=lista[12]
            elif Neighbours[0][1]==0 and Neighbours[1][0]==1 and Neighbours[1][2]==1 and Neighbours[2][1]==0:
                self.image=lista[0]
            elif Neighbours[0][1]==1 and Neighbours[1][0]==0 and Neighbours[1][2]==0 and Neighbours[2][1]==1:
                self.image=lista[3]
            elif Neighbours[0][1]==0 and Neighbours[1][0]==1 and Neighbours[1][2]==1 and Neighbours[2][1]==1:
                self.image=lista[10]
            elif Neighbours[0][1]==1 and Neighbours[1][0]==1 and Neighbours[1][2]==1 and Neighbours[2][1]==0:
                self.image=lista[9]
            elif Neighbours[0][1]==1 and Neighbours[1][0]==1 and Neighbours[1][2]==0 and Neighbours[2][1]==1:
                self.image=lista[14]
            elif Neighbours[0][1]==1 and Neighbours[1][0]==0 and Neighbours[1][2]==1 and Neighbours[2][1]==1:
                self.image=lista[15]
        if len(lista)<17:
            return Floors(terrain,x,y,lista,value)
        a=CheckNeighbours(terrain,x,y)
        b=CombinationChecking(a,lista)
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
index=1
lista=rocks
material='rocks'
Font=pygame.font.SysFont("Arial", 12,bold=False,italic=False)
while not done: # główna pętla gry
    x2=0
    y2=0
    z=0
    # Input
    for event in pygame.event.get(): # wydarzenia
        if event.type == pygame.QUIT: # wyjście
            done = True
            pygame.quit()
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_1:
                index=1
                lista=rocks
                material='rocks'
            elif event.key == pygame.K_2:
                index=2
                lista=wood
                material='wood'
            elif event.key== pygame.K_3:
                lista=floors
                if index==3:
                    index=4
                    material='carpet_green'
                elif index==4:
                    index=5
                    material='carpet_red'
                elif index==5:
                    index=6
                    material='concrete'
                elif index==6:
                    index=7
                    material='stone_floor'
                elif index==7:
                    index=8
                    material='wooden_floor'
                else:
                    index=3
                    material='carpet_blue'
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
        terrain[a][b]=index
        if index>2 and index<9:
            t=Tile(lista[0],x2,y2)
            t.StructureInit(lista,terrain,int(x2/16),int(y2/16),index)
        else:
            t=Tile(lista[8],x2,y2)
            t.StructureInit(lista,terrain,int(x2/16),int(y2/16))
        allSprites.add(t)
    if z==2:
        terrain[a][b]='-'
        t=Tile(missing,x2,y2)
        allSprites.add(t) #] - podmienianie tilów na mapie
    x=0
    for i in range(len(terrain)):
        y=0
        for j in range(len(terrain[0])):
            if terrain[x][y]==1:
                t=Tile(rocks[8],x*16,y*16)
                t.StructureInit(rocks,terrain,x,y)
                allSprites.add(t)
            if terrain[x][y]==2:
                t=Tile(wood[8],x*16,y*16)
                t.StructureInit(wood,terrain,x,y)
                allSprites.add(t)
            y=y+1
        x=x+1
    c=pygame.mouse.get_pos()
    a=int(c[0]/16)
    b=int(c[1]/16)
    # drawing
    #text='Building material: '+str(material)
    #text2='Tile properties: ID - '+str(terrain[a][b])
    allSprites.draw(screen)
    label=Font.render('Building material: '+str(material),1,(168,168,168),(0,0,0))
    screen.blit(label,(470,10))
    label=Font.render('Tile properties: ID - '+str(terrain[a][b]),1,(168,168,168),(0,0,0))
    screen.blit(label,(470,22))
    pygame.display.flip()  # wyświetlanie wszystkiego na ekranie
    
