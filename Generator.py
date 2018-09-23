import pygame
import time
from os import path
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
pygame.init()
screen=pygame.display.set_mode((600,600)) # okno 600x600
pygame.display.set_caption("Terrain generator") # nazwa okna
done=False
imgDir=path.join(path.dirname(__file__),'Textures')   # folder gry
rockTexture=pygame.image.load(path.join(path.join(path.join(path.dirname(__file__),'Textures'),'Rocks'),'Rock14.png')).convert()  #
rocksTexture=pygame.image.load(path.join(path.join(imgDir,'Grounds'),'stone01.png')).convert()                                    #
grassTexture=pygame.image.load(path.join(path.join(imgDir,'Grounds'),'grass01.png')).convert_alpha()                              #  Wczytywanie potrzebnych tekstur
dirtTexture=pygame.image.load(path.join(path.join(imgDir,'Grounds'),'dirt01.png')).convert()                                      # 
treeTexture=pygame.image.load(path.join(path.join(path.join(imgDir,'Plants'),'tree01'),'01.png')).convert_alpha()                 #

BLACK=(0, 0, 0)

global terrain
terrain=[]    #  \
structures=[] #  | 3 warstwy na których zapisywane są dane terenu, struktur i mebli
furniture=[]  #  /
#map1=[terrain,structures,furniture] ---> skopiować i przenieć do systemu zapisu

class Tile(pygame.sprite.Sprite): # klasa do tworzenia płytek do terenu
    def __init__(self,value,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16,16))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        if value == 0:
            self.image= rocksTexture
        elif value== 1:   
            self.image = dirtTexture
        elif value==2:
            self.image = grassTexture
        elif value==3:
            self.image = treeTexture
        elif value==4:
            self.image = rockTexture
        self.rect.top=y
        self.rect.left=x
def main(): # główny proces gry
    def generation(): # generacja
        try:
            def PlaceStone(OldTerrain): # stawia kamień na istniejących płytach kamienia z warstwy terrain
                def CountGrassAround(map1,x,y):
                    i=-1
                    count=0
                    for a in range(3):
                        j=-1
                        for b in range(3):
                            neighbourX=x+i
                            neighbourY=y+j
                            if i==0 and j==0:
                                pass
                            elif neighbourX<0 or neighbourY<0 or neighbourX>x2-1 or neighbourY>y2-1:
                                pass
                            elif map1[neighbourX][neighbourY]==1:
                                count=count+1
                            j=j+1
                        i=i+1
                    return count
                Structures=[]
                for j in range(len(OldTerrain)):
                    lista=[]
                    for i in range(len(OldTerrain[0])):
                        lista.append('-')
                    Structures.append(lista)
                x=0
                for i in range(x2):
                    y=0
                    for j in range(y2):
                        if OldTerrain[x][y]==0:
                             Structures[x][y]=0
                        else:
                            pass
                        y+=1
                    x+=1
                x=0
                for i in range(x2):
                    y=0
                    for j in range(y2):
                        nbs=CountGrassAround(OldTerrain,x,y)
                        if OldTerrain[x][y]==1:
                            pass
                        elif nbs>1:
                            Structures[x][y]='-'
                        y+=1
                    x+=1
                #print(Structures)
                return Structures
            def PlantTrees(OldTerrain): # sadzi drzewa na mapie
                def Countdirt():
                    pass
            def PlantGrass(OldTerrain): # sadzi trawę na mapie omijając kamień
                NewTerrain=OldTerrain
                x=0
                for i in range(x2):
                    y=0
                    for j in range(y2):
                        if OldTerrain[x][y]==0:
                            pass
                        else:
                            NewTerrain[x][y]=2
                        y=y+1
                    x=x+1
                return NewTerrain
            def doSimulationStep(OldTerrain):   # wygładza wygenerowany teren
                def countAliveNeighbours(map1,x,y):
                    i=-1
                    count=0
                    for a in range(3):
                        j=-1
                        for b in range(3):
                            neighbourX=x+i
                            neighbourY=y+j
                            if i==0 and j==0:
                                pass
                            elif neighbourX<0 or neighbourY<0 or neighbourX>x2-1 or neighbourY>y2-1:
                                count=count+1
                            elif map1[neighbourX][neighbourY]==1:
                                count=count+1
                            j=j+1
                        i=i+1
                    return count
                NewTerrain=[]
                for a in range(len(OldTerrain)):
                    lista=[]
                    for z in range(len(OldTerrain[0])):
                        lista.append(0)
                    NewTerrain.append(lista)
                x=0
                for b in range(x2):
                    y=0
                    for c in range(y2):
                        nbs=countAliveNeighbours(OldTerrain,x,y)
                        if OldTerrain[x][y]==1:
                            if nbs<4:
                                NewTerrain[x][y]=0
                            else:
                                NewTerrain[x][y]=1
                        else:
                            if nbs>4:
                                NewTerrain[x][y]=1
                            else:
                                NewTerrain[x][y]=0
                        y+=1
                    x+=1
                return NewTerrain
            terrainL=pygame.sprite.Group()     #
            structuresL=pygame.sprite.Group()  #  grupy spritów na mapie
            import random
            global x,y,z,d,terrain,structures
            if not isinstance(x, int):      #[
                x2=int(x.get())
            else:
                x2=x
            if not isinstance(y, int):
                y2=int(y.get())
            else:
                y2=y
            if not isinstance(z, int):
                z2=int(z.get())
            else:
                z2=z
            if not isinstance(d, int):  
                d2=int(d.get())             #] - sprawdza czy zmienne są zdatne do odczytania
            else:
                d2=d
            x3=0
            screen.fill((0,0,0)) 
            terrain=[]
            for a in range(x2): # wypełnia teren losowymi wartościami 0-1
                y3=0
                collumn=[]
                for b in range(y2):
                    c=random.randint(1,99)
                    GrassOrDirt=random.randint(1,2)
                    if c<z2:
                        t=Tile(1,x3,y3)
                        terrainL.add(t)
                        collumn.append(1)
                    else:
                        t=Tile(0,x3,y3)
                        terrainL.add(t)
                        collumn.append(0)
                    y3+=16
                terrain.append(collumn)
                x3+=16
            for loop in range(d2): # wygładza teren określoną ilość razy
                terrain=doSimulationStep(terrain)
                x3=0
                x4=0
                for a in range(x2):
                    y3=0
                    y4=0
                    for b in range(y2):
                        if terrain[x4][y4]==1:
                            t=Tile(1,x3,y3)
                        else:
                            t=Tile(0,x3,y3)
                        terrainL.add(t)
                        y3+=16
                        y4+=1
                    x3+=16
                    x4+=1
            #terrain=PlantGrass(terrain)    # sadzenie trawy
            x3=0
            x4=0
            for a in range(x2):  # stawianie tilów w odpowiednich miejscach z odpowiednimi teksturami
                y4=0
                y3=0
                for b in range(y2):
                    if terrain[x4][y4]==0:
                        t=Tile(0,x3,y3)
                    elif terrain[x4][y4]==1:
                        t=Tile(1,x3,y3)
                    elif terrain[x4][y4]==2:
                        t=Tile(2,x3,y3)
                    elif terrain[x4][y4]==3:
                        pass
                        #t=Tile(3,x3,y3)
                    terrainL.add(t)
                    y3+=16
                    y4=y4+1
                x3+=16
                x4=x4+1
                #print(terrain)
            structures=PlaceStone(terrain) # stawianie kamieni
            x3=0
            x4=0
            for a in range(x2): # stawianie struktur
                y4=0
                y3=0
                for b in range(y2):
                    if structures[x4][y4]=='-':
                        pass
                    elif structures[x4][y4]==0:
                        t=Tile(4,x3,y3)
                        structuresL.add(t)
                    y3+=16
                    y4+=1
                x3+=16
                x4+=1
            terrainL.draw(screen)    # 
            structuresL.draw(screen) # wyświetlanie wszystkiego na ekranie
            pygame.display.flip()    #
        except ValueError:
            messagebox.showwarning("Warning","Jako wielkość należy podać liczby!")
    root = Tk() #[
    root.title('Terrain Generator Settings')
    mainframe = ttk.Frame(root,padding='3 3 12 12')
    mainframe.grid(column=0, row=0,sticky=(N,W,E,S))
    mainframe.rowconfigure(0,weight=1)
    global x
    global y
    global z
    global d
    x=StringVar() # dla normalnego biomu ustawić generator na - - 53 5
    y=StringVar() # lub - - 50 12
    z=StringVar()
    d=StringVar()
    entry=ttk.Entry(mainframe,width=7, textvariable=x)
    entry.grid(column=2,row=1)
    entry2=ttk.Entry(mainframe,width=7, textvariable=y)
    entry2.grid(column=2,row=2)
    entry3=ttk.Entry(mainframe,width=3, textvariable=z)
    entry3.grid(column=2,row=3)
    entry4=ttk.Entry(mainframe,width=3, textvariable=d)
    entry4.grid(column=2,row=4)
    ttk.Label(mainframe,text='Szerokość:').grid(column=1,row=1)
    ttk.Label(mainframe,text='Wysokość:').grid(column=1,row=2)
    ttk.Label(mainframe,text='Poziom wypełnienia:').grid(column=1,row=3)
    ttk.Label(mainframe,text='Ilość wygładzeń:').grid(column=1,row=4)
    ttk.Button(mainframe,text='Generuj',command=generation).grid(column=3,row=4)
    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
    root.mainloop() #] - menu generowania
    global done
    while not done: # główna pętla pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
main()
