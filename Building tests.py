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
buildingShadow=pygame.image.load(path.join(imgDir,'BuildShadow.png'))

index=1
rocks=[]
for i in range(25):
    rocks.append(pygame.image.load(path.join(path.join(path.join(path.dirname(__file__),'Textures'),'Rocks'),'Rock'+str(index)+'.png')).convert())
    index=index+1
index=1
wood=[]
for i in range(17):
    wood.append(pygame.image.load(path.join(path.join(path.join(path.join(path.dirname(__file__),'Textures'),'walls'),'Wood'),'WoodenWall_'+str(index)+'.png')).convert())
    index+=1
index=1
floors=[]
for i in range(3):
    floors.append(pygame.image.load(path.join(path.join(path.join(path.dirname(__file__),'Textures'),'Floors'),'Carpet'+str(index)+'.png')).convert())
    index+=1
floors.append(pygame.image.load(path.join(path.join(path.join(path.dirname(__file__),'Textures'),'Floors'),'Concrete.png')).convert())
floors.append(pygame.image.load(path.join(path.join(path.join(path.dirname(__file__),'Textures'),'Floors'),'stone.png')).convert())
floors.append(pygame.image.load(path.join(path.join(path.join(path.dirname(__file__),'Textures'),'Floors'),'Wood.png')).convert())
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
    def StructureInit(self,lista,terrain,x,y,LinkedToNeighbours,*ID): # inicjalizacja struktur i dobieranie odpowiednich tekstur
        if LinkedToNeighbours==0:
            ID=ID[0]
            if ID==1:
                self.image=lista[0]
            if ID==2:
                self.image=lista[1]
            if ID==3:
                self.image=lista[2]
            if ID==4:
                self.image=lista[3]
            if ID==5:
                self.image=lista[4]
            if ID==6:
                self.image=lista[5]
        else:
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
                elif Neighbours[0][1]==1 and Neighbours[1][0]==1 and Neighbours[1][2]==1 and Neighbours[2][1]==1:
                    self.image=lista[13]
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
structures=[]
for i in range(100):
    lista=[]
    for j in range(100):
        lista.append('-')
    structures.append(lista)
builds=[]
for i in range(100):
    lista=[]
    for j in range(100):
        lista.append('-')
    builds.append(lista)
index=1

BuildingMaterials=['rocks','wood']
StructureList=['carpet_green','carpet_red','carpet_blue','concrete','stone_floor','wooden_floor']

drag=0
lista=rocks
material='rocks'
builds2=[]
Font=pygame.font.SysFont("Arial", 12,bold=False,italic=False)

while not done: # główna pętla gry
    x2=0
    y2=0
    MouseButton=3
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
                if index==1:
                    index=2
                    material='carpet_green'
                elif index==2:
                    index=3
                    material='carpet_red'
                elif index==3:
                    index=4
                    material='concrete'
                elif index==4:
                    index=5
                    material='stone_floor'
                elif index==5:
                    index=6
                    material='wooden_floor'
                else:
                    index=1
                    material='carpet_blue'
        if event.type==pygame.MOUSEBUTTONDOWN: # naciśnięcie przycisku myszy
            if drag==0:
                drag_start_x=int(pygame.mouse.get_pos()[0])
                drag_start_y=int(pygame.mouse.get_pos()[1])
                drag=1
            if pygame.mouse.get_pressed()[0]==1: # ppm
                a=int(pygame.mouse.get_pos()[0]/16)
                b=int(pygame.mouse.get_pos()[1]/16)
                for i in range(a):
                    x2=x2+16
                for j in range(b):
                    y2=y2+16
                MouseButton=0
            elif pygame.mouse.get_pressed()[2]==1: # lpm
                a=int(pygame.mouse.get_pos()[0]/16)
                b=int(pygame.mouse.get_pos()[1]/16)
                for i in range(a):
                    x2=x2+16
                for j in range(b):
                    y2=y2+16
                MouseButton=1
        if event.type==pygame.MOUSEBUTTONUP:
            if material not in BuildingMaterials:
                texture=rocks[8]
            else:
                if material=='rocks':
                    texture=rocks[8]
                elif material=='wood':
                    texture=wood[8]
            drag=0
            drag_end_y=int(pygame.mouse.get_pos()[1])
            drag_end_x=int(pygame.mouse.get_pos()[0])
            if drag_end_x<drag_start_x:
                tmp=drag_end_x
                drag_end_x=drag_start_x
                drag_start_x=tmp
            if drag_end_y<drag_start_y:
                tmp=drag_end_y
                drag_end_y=drag_start_y
            i=int(int(drag_start_x/16)*16)
            while i<drag_end_x:
                j=int(int(drag_start_y/16)*16)
                while j<drag_end_y:
                    t=Tile(texture,i,j)
                    allSprites.add(t)
                    builds[int(i/16)][int(j/16)]=0
                    terrain[int(i/16)][int(j/16)]=index
                    j=j+16
                i=i+16
    # Update
    
    while len(builds2)>0:
        builds2[len(builds2)-1].kill()
        builds2.pop()
        print(builds2)
    if drag==1:
        drag_start_x2=drag_start_x
        drag_start_y2=drag_start_y
        drag_end_y=int(pygame.mouse.get_pos()[1])
        drag_end_x=int(pygame.mouse.get_pos()[0])
        if drag_end_x<drag_start_x:
            drag_start_x2=drag_end_x
            drag_end_x=drag_start_x
        if drag_end_y<drag_start_y:
            drag_start_y2=drag_end_y
            drag_end_y=drag_start_y
        i=int(int(drag_start_x2/16)*16)
        while i<drag_end_x:
            j=int(int(drag_start_y2/16)*16)
            while j<drag_end_y:
                t=Tile(buildingShadow,i,j)
                allSprites.add(t)
                builds2.append(t)
                j=j+16
            i=i+16
    #if MouseButton==0: #[
    #    if material in BuildingMaterials:
    #        block=True
    #        terrain[a][b]=index
    #    else:
    #        block=False
    #        structures[a][b]=index
    #    if not block:
    #        t=Tile(lista[0],x2,y2)
    #        t.StructureInit(lista,terrain,int(x2/16),int(y2/16),False,index)
    #   else:
    #        t=Tile(lista[8],x2,y2)
    #        t.StructureInit(lista,terrain,int(x2/16),int(y2/16),True)
    #    allSprites.add(t)
    if MouseButton==1:
        terrain[a][b]='-'
        t=Tile(missing,x2,y2)
        allSprites.add(t) #] - podmienianie tilów na mapie
    x=0
    for i in range(len(terrain)):
        y=0
        for j in range(len(terrain[0])):
            if terrain[x][y]==1:
                t=Tile(rocks[8],x*16,y*16)
                t.StructureInit(rocks,terrain,x,y,True)
                allSprites.add(t)
            if terrain[x][y]==2:
                t=Tile(wood[8],x*16,y*16)
                t.StructureInit(wood,terrain,x,y,True)
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
    label=Font.render('Tile properties: ID - '+str(terrain[a][b])+'| '+str(structures[a][b]),1,(168,168,168),(0,0,0))
    screen.blit(label,(470,22))
    pygame.display.flip()  # wyświetlanie wszystkiego na ekranie
    
