import random

# writers: 0 = Phoebe; 1 = Cassandra; 2 = Randy;
# dificulities: 0 = peaceful; 1 = base builder; 2 = Some Chalange; 3 = Rough; 4 = Intense; 5 = Extreme
# p1: 0 = human;
# p2: 0 = human; 1 = squirrel
# weapons: 0 = mele; 1 = ranged
def FightingSystem(writer, dificulity,p1,p2):
     def Body(player):
          if player==0:
               lista=[['głowa',['siniak'],['uszkodzenie słuchu','uszkodzenie wzroku','uszkodzenie mógzu','odstrzelone ucho']],['szyja',['siniak'],['rana postrzałowa']],['tors',['siniak','zadrapanie'],['rana postrzałowa']]]
          elif player==1:
               lista=[]
          return lista
     def Moves(player,weapon):
          if player==0:
               if weapon==0:
                    lista=['człowiek',['']]
               elif weapon==1:
                    lista=['człowiek',['']]
          elif player=1:
               lista=['wiewiórka',['']]
          return lista
     if writer==0: # Phoebe
          if dificulity==0:
               pass
          elif dificulity==1:
               pass
          elif dificulity==2:
               pass
          elif dificulity==3:
               pass
          elif dificulity==4:
               pass
          elif dificulity==5:
               pass
     elif writer==1: # Cassandra
          if dificulity==0:
               pass
          elif dificulity==1:
               pass
          elif dificulity==2:
               pass
          elif dificulity==3:
               pass
          elif dificulity==4:
               pass
          elif dificulity==5:
               pass
     elif writer==2: # Randy
          if dificulity==0:
               pass
          elif dificulity==1:
               pass
          elif dificulity==2:
               pass
          elif dificulity==3:
               pass
          elif dificulity==4:
               pass
          elif dificulity==5:
               pass
def main():
     def menu():
          while True:
               a=Exception
               print('Podaj pisarza: (1, 2 lub 3)')
               print('1.Phoebe')
               print('2.Kasandra')
               print('3.Randy')
               try:
                    x=int(input())
                    if x>3 or x<1:
                         raise a
                    x=x-1
                    while True:
                         b=Exception
                         print('Podaj poziom trudności: (1-6)')
                         print('1. Peaceful')
                         print('2. Base Builder')
                         print('3. Some Challange')
                         print('4. Rough')
                         print('5. Intense')
                         print('6. Extreme')
                         try:
                              y=int(input())
                              if y>6 or y<1:
                                   raise b
                              y=y-1
                              while True:
                                   c=Exception
                                   print('Podaj atakującego: (1-2)')
                                   print('1. Human')
                                   print('2. Squirrel')
                                   try:
                                      z=int(input())
                                      if z>2 or z<1:
                                           raise c
                                      z=z-1
                                      lista=[x,y,z]
                                      return lista
                                   except ValueError:
                                        print('Podaj liczbę!')
                                   except c:
                                        print('Podaj poprawną opcję!')
                              break
                         except ValueError:
                              print('Podaj liczbę!')
                         except b:
                              print('Podaj poprawną opcję!')
                    break
               except ValueError:
                    print('Podaj liczbę!')
               except a:
                    print('Podaj poprawną opcję!')
     lista=menu()
     print(FightingSystem(lista[0],lista[1],'0',lista[2]))
main()
     
     
     
