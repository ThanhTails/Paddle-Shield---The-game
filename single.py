from pygame import*
import time as tm
from random import*
import main
init()
#var
width,height=440,700
plX=200
plY=600
FPS=60
fonts=font.Font("freesansbold.ttf",20)
font2=font.Font("freesansbold.ttf",50)
#clock
clock=time.Clock()
#Colors
red=(255,0,0)
green=(0,255,0)
yellow=(255,255,0)
black=(0,0,0)
blue=(0,0,255)


class player():
  def __init__(self):
    self.x=plX
    self.y=plY
    self.point=0
    self.y_top=self.y-10
    self.hp=3
    self.right=False
    self.left=False
    self.stay=True
  def draw_player(self):
    draw.rect(main,red,(self.x,self.y,40,20))
    if self.x<=0:
      self.x=0
    if self.x>=400:
      self.x=400
    if self.right:
      players.x+=2
    if self.left:
      players.x-=2
class opponent():
  def __init__(self):
    self.x=randrange(10,380,4)
    self.y=0
    self.speed=1
  def draw_ex(self):
    draw.rect(main,green,(self.x,self.y,20,20))
    if self.y>=700:
      self.y=0
      self.x=randrange(10,380,2)

players=player()
op=opponent()
def main_window():#window
  done=False
  global main
  main=display.set_mode((width,height))
  display.set_caption("Shoot v0.1")
  while not done:
    main.fill(black)
    for e in event.get():
      if e.type==QUIT:
        done=True
      if e.type==KEYDOWN:
        if e.key==K_LEFT or e.key==K_a:
          if players.right:
            players.right=False
            players.stay=True
          else:
            players.left=True
            players.stay=False
        if e.key==K_RIGHT or e.key==K_d:
          if players.left:
            players.left=False
            players.stay=True
          else:
            players.stay=False
            players.right=True
        if e.key==K_q:
          quit()
    if op.x>=players.x-20 and players.x+20>=op.x:
      if op.y==players.y:
        op.y=0
        op.x=randrange(10,380,2)
        players.point+=1
    if op.y>=700:
      op.y=0
      op.x=randrange(10,380,4)
      players.hp-=1
      op.speed+=0.1
    
    #controls auto
    
    players.draw_player()
    op.draw_ex()
    #font: point
    points=fonts.render("Point: "+str(players.point),True,blue)
    
    #font: health
    if players.hp==3:
      life=fonts.render("Health: "+str(players.hp),True,green)
    if players.hp==2:
      life=fonts.render("Health: "+str(players.hp),True,yellow)
    if players.hp==1:
      life=fonts.render("Health: "+str(players.hp),True,red)
    main.blit(life,(300,50))
    main.blit(points,(20,50))

    op.y+=op.speed
    if players.hp<=0:
      lost=font2.render("GAME OVER!",True,red)
      main.blit(lost,(50,350))
      done=True
    clock.tick(FPS)
    display.update()
  tm.sleep(5)
  quit()