import pygame 
import random

"Lab 4 Andres Paiz 191142 Conways game of life"
pygame.init()
vivas = (100,50,100)
rx,ry = 200,200
screen = pygame.display.set_mode((200,200))
pygame.display.set_caption(" LAB 4")

display = pygame.Surface((rx,ry))

for i in range(5000):                
    x = random.randint(0,rx)
    y = random.randint(0,ry)
    display.set_at((x,y),vivas)

def contvivas(x,y):   
    cont = 0 
    for i in range(-1,2):
        for k in range(-1,2):
            if i==0 and k ==0:continue
            x1 = x + i  ; y1 = y + k
            if x1 >= 0 and x1< rx and y1>=0 and y1<ry:
                color = display.get_at((x1,y1))
                if color == vivas:cont = cont + 1
    return cont

while True:
   
    for x in range(rx):
        for y in range(ry):
          cel = display.get_at((x,y))
          cel_cont = contvivas(x,y)
          if cel == vivas:
              if cel_cont == 3 or cel_cont==2 :continue  
              if cel_cont < 2 or cel_cont >3 :display.set_at((x,y),(0,0,0)) 
          else:
              if cel_cont == 3 : display.set_at((x,y),vivas)  
 
    screen.blit(display,(0,0))
    pygame.display.update()
        
  



