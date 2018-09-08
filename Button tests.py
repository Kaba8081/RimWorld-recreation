import pygame
from os import path
pygame.init()
screen=pygame.display.set_mode((1366,768),pygame.FULLSCREEN)
done=False
Inspector_Active=False
menu_open=False
small_menu_open=False
exit_confirmation_open=False
SoundsVolume=100
MusicVolume=100
AmbientVolume=100
imgDir=path.join(path.dirname(__file__),'Textures')
allSprites=pygame.sprite.Group()
menuSprites=pygame.sprite.Group()
buttons=[]
buttons.append(pygame.image.load(path.join(path.join(imgDir,'UI'),'bar1.png')).convert_alpha())
buttons.append(pygame.image.load(path.join(path.join(imgDir,'UI'),'button01.png')).convert())
buttons.append(pygame.image.load(path.join(path.join(imgDir,'UI'),'button02.png')).convert())
buttons.append(pygame.image.load(path.join(path.join(imgDir,'UI'),'Menu Bar.png')).convert())
buttons.append(pygame.image.load(path.join(path.join(imgDir,'UI'),'button03.png')).convert())
buttons.append(pygame.image.load(path.join(path.join(imgDir,'UI'),'button04.png')).convert())
buttons.append(pygame.image.load(path.join(path.join(imgDir,'UI'),'Sound_Input01.png')).convert())
cursor=pygame.image.load(path.join(path.join(imgDir,'UI'),'cursor.png')).convert_alpha()
Font=pygame.font.SysFont("Helvetica", 15,bold=False,italic=False)
FontColor=(207, 210, 214)
pygame.mouse.set_visible(False)
#pointerImg_rect = cursor.get_rect()
clock=pygame.time.Clock()
class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((12,16))
        self.rect=self.image.get_rect()
        self.image.set_colorkey((0,0,0))
        self.image=cursor
    def update(self,pos):
        self.rect.topleft=pos
class Button(pygame.sprite.Sprite):
    def __init__(self,value,*cords):
        pygame.sprite.Sprite.__init__(self)
        if value==0:
            self.image=pygame.Surface((432,164))
        elif value==3:
            self.image=pygame.Surface((600,468))
        elif value==6:
            self.image=pygame.Surface((30,15))
        else:
            self.image=pygame.Surface((136,35))
        self.rect=self.image.get_rect()
        self.image.set_colorkey((0,0,0))
        if value==0:
            self.image=buttons[0]
            self.rect.bottom=733
            self.rect.left=0
        elif value==1:
            self.image=buttons[1]
            self.rect.bottom=768
            self.rect.left=cords[0]
        elif value==2:
            self.image=buttons[2]
            self.rect.bottom=768
            self.rect.left=cords[0]
        elif value==3:
            self.image=buttons[3]
            self.rect.centerx=683
            self.rect.centery=384
        elif value==4:
            self.image=buttons[4]
        elif value==5:
            self.image=buttons[5]
        elif value==6:
            self.active=False
            self.text=''
            self.image=buttons[6]
            self.rect.left=cords[0]
            self.rect.bottom=cords[1]
        elif value==7:
            pass
buttonLabels=[]
buttonLabels.append(Font.render('Architekt',1,FontColor,None))
buttonLabels.append(Font.render('Praca',1,FontColor,None))
buttonLabels.append(Font.render('Harmonogram',1,FontColor,None))
buttonLabels.append(Font.render('Przydział',1,FontColor,None))
buttonLabels.append(Font.render('Zwierzęta',1,FontColor,None))
buttonLabels.append(Font.render('Badania',1,FontColor,None))
buttonLabels.append(Font.render('Świat',1,FontColor,None))
buttonLabels.append(Font.render('Historia',1,FontColor,None))
buttonLabels.append(Font.render('Frakcje',1,FontColor,None))
buttonLabels.append(Font.render('Menu',1,FontColor,None))
FPS_label=Font.render('FPS: '+str(clock.get_fps()),0,FontColor,None)
cursor2=Cursor()
def Open_menu_small():
    global SmallMenuLabels
    SmallMenuLabels=[]
    SmallMenuLabels.append(Font.render("Zapisz",1,FontColor,None))
    SmallMenuLabels.append(Font.render("Wczytaj",1,FontColor,None))
    SmallMenuLabels.append(Font.render("Zobacz scenariusz",1,FontColor,None))
    SmallMenuLabels.append(Font.render("Opcje",1,FontColor,None))
    SmallMenuLabels.append(Font.render("Wróć do menu",1,FontColor,None))
    SmallMenuLabels.append(Font.render("Wyjdź z gry",1,FontColor,None))
    MenuSprites.add(Button(7))
def Open_menu():
    global MenuLabels,inputbox
    MenuFont=pygame.font.SysFont("Helvetica", 20,bold=False,italic=False)
    menuSprites.add(Button(3))
    MenuLabels=[]
    MenuLabels.append(MenuFont.render('Dźwięk/Grafika',1,FontColor,None))
    MenuLabels.append(MenuFont.render('Rozgrywka',1,FontColor,None))
    MenuLabels.append(Font.render('Głośność dźięków',1,FontColor,None))
    MenuLabels.append(Font.render(str(SoundsVolume),1,FontColor,None))
    MenuLabels.append(Font.render('Głośność muzyki',1,FontColor,None))
    MenuLabels.append(Font.render(str(MusicVolume),1,FontColor,None))
    MenuLabels.append(Font.render('Głośność otoczenia',1,FontColor,None))
    MenuLabels.append(Font.render(str(AmbientVolume),1,FontColor,None))
    inputbox=[]
    y=221
    for i in range(3):
        inputbox.append(Button(6,448,y))
        menuSprites.add(Button(6,448,y))
        y+=45
def Update_menu():
    MenuLabels[3]=Font.render(str(SoundsVolume),1,FontColor,None)
    MenuLabels[5]=Font.render(str(MusicVolume),1,FontColor,None)
    MenuLabels[7]=Font.render(str(AmbientVolume),1,FontColor,None)
def  Exit_confirmation():
    global ExitMenuLabels
    
while not done:
    allSprites=pygame.sprite.Group()
    mousePos=pygame.mouse.get_pos()
    #Input
    for event in pygame.event.get():
        mousePress=pygame.mouse.get_pressed()
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN:
            if menu_open:
                if inputbox[0].active:
                    if event.key==pygame.K_BACKSPACE:
                        inputbox[0].text=inputbox[0].text[:-1]
                        SoundsVolume=inputbox[0].text
                    elif event.key==pygame.K_RETURN:
                        if inputbox[0].text=='':
                            inputbox[0].text='0'
                            SoundsVolume='0'
                        inputbox[0].active=False
                    elif event.unicode not in ['1','2','3','4','5','6','7','8','9','0'] or len(str(inputbox[0].text))>=3:
                        pass
                    elif int(inputbox[0].text+event.unicode)>100:
                        pass
                    else:
                        inputbox[0].text+=event.unicode
                        SoundsVolume=inputbox[0].text
                elif inputbox[1].active:
                    if event.key==pygame.K_BACKSPACE:
                        inputbox[1].text=inputbox[1].text[:-1]
                        MusicVolume=inputbox[1].text
                    elif event.key==pygame.K_RETURN:
                        if inputbox[1].text=='':
                            inputbox[1].text='0'
                            MusicVolume='0'
                        inputbox[1].active=False
                    elif event.unicode not in ['1','2','3','4','5','6','7','8','9','0'] or len(inputbox[1].text)>=3:
                        pass
                    elif int(inputbox[1].text+event.unicode)>100:
                        pass
                    else:
                        inputbox[1].text+=event.unicode
                        MusicVolume=inputbox[1].text
                elif inputbox[2].active:
                    if event.key==pygame.K_BACKSPACE:
                        inputbox[2].text=inputbox[2].text[:-1]
                        AmbientVolume=inputbox[2].text
                    elif event.key==pygame.K_RETURN:
                        if inputbox[2].text=='':
                            inputbox[2].text='0'
                            AmbientVolume='0'
                        inputbox[2].active=False
                    elif event.unicode not in ['1','2','3','4','5','6','7','8','9','0'] or len(inputbox[2].text)>=3:
                        pass
                    elif int(inputbox[2].text+event.unicode)>100:
                        pass
                    else:
                        inputbox[2].text+=event.unicode
                        AmbientVolume=inputbox[2].text
            if event.key==pygame.K_LALT and pygame.key.get_pressed()[pygame.K_F4]:
                done=True
                pygame.quit()
            elif event.key==pygame.K_F4 and pygame.key.get_pressed()[pygame.K_LALT]:
                done=True
                pygame.quit()
            elif event.key==pygame.K_ESCAPE:
                if not menu_open and not small_menu_open:
                    Open_menu_small()
                    small_menu_open=True
                else:
                    small_menu_open=False
                if menu_open:
                    menu_open=False
                if exit_confirmation_open:
                    exit_confirmation_open=False
                if small_menu_open and not menu_open and not exit_confirmation_open:
                    small_menu_open=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if mousePress[0]==1:
                if mousePos[1]<733:
                    if Inspector_Active:
                        Inspector_Active=False
                    else:
                        Inspector_Active=True
                if small_menu_open:
                    if menu_open:
                        index=0
                        for i in range(3):
                            if pygame.sprite.collide_rect(inputbox[index],cursor2):
                                inputbox[index].active=True
                            index+=1
                    else:
                        index=0
                        for i in range(6):
                            if pygame.sprite.collide_rect(inputbox[index],cursor2):
                                if index==1:
                                    pass
                                if index==2:
                                    pass
                                if index==3:
                                    pass
                                if index==4:
                                    Open_menu()
                                    menu_open=True
                                if index==5:
                                    pass
                                if index==6:
                                    Exit_confirmation()
                                    exit_confirmation_open=True
    #Update
    cursor2.update(mousePos)
    if menu_open:
        #menuSprites=pygame.sprite.Group()
        Update_menu()
        allSprites.add(menuSprites)
        x=0
        for i in range(3):
            if inputbox[x].active:
                pass # Zmienić teksturę
            x+=1
    if Inspector_Active:
        b=Button(0)
        allSprites.add(b)
    x=0
    for i in range(10):
        b=Button(1,x)
        allSprites.add(b)
        x=x+136
    if mousePos[1]>733:
        if mousePos[0]<137:
            b=Button(2,0)
        elif mousePos[0]>136 and mousePos[0]<273:
            b=Button(2,136)
        elif mousePos[0]>273 and mousePos[0]<408:
            b=Button(2,273)
        elif mousePos[0]>408 and mousePos[0]<544:
            b=Button(2,408)
        elif mousePos[0]>544 and mousePos[0]<680:
            b=Button(2,544)
        elif mousePos[0]>680 and mousePos[0]<816:
            b=Button(2,680)
        elif mousePos[0]>816 and mousePos[0]<952:
            b=Button(2,816)
        elif mousePos[0]>952 and mousePos[0]<1088:
            b=Button(2,952)
        elif mousePos[0]>1088 and mousePos[0]<1224:
            b=Button(2,1088)
        elif mousePos[0]>1224 and mousePos[0]<1350:
            b=Button(2,1224)
        allSprites.add(b)
    #Draw
    screen.fill((0,0,0))
    allSprites.add(cursor2)
    allSprites.draw(screen)
    x=15
    index=0
    screen.blit(FPS_label, (0,0))
    for i in range(10):
        screen.blit(buttonLabels[index],(x,741))
        x+=136
        index+=1
    if menu_open:
        screen.blit(MenuLabels[0],(463,155))
        screen.blit(MenuLabels[1],(663,155))
        screen.blit(MenuLabels[2],(400,185))
        screen.blit(MenuLabels[3],(450,205))
        screen.blit(MenuLabels[4],(400,225))
        screen.blit(MenuLabels[5],(450,250))
        screen.blit(MenuLabels[6],(400,275))
        screen.blit(MenuLabels[7],(450,295))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
