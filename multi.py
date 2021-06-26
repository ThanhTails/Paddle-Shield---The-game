from pygame import*
import time as tm
from random import*
import main
init()
#var
width,height=440,700
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
orange=(255,140,0)
white=(255,255,255)


class player1():
  def __init__(self):
    self.x=300
    self.y=plY
    self.point=0
    self.y_top=self.y-10
    self.hp=3
    self.right=False
    self.left=False
    self.stay=True
  def draw_player1(self):
    draw.rect(main,red,(self.x,self.y,40,20))
    if self.x<=0:
      self.x=0
    if self.x>=400:
      self.x=400
    if self.right:
      self.x+=2
    if self.left:
      self.x-=2
class player2():
  def __init__(self):
    self.x=100
    self.y=plY
    self.point=0
    self.y_top=self.y-10
    self.hp=3
    self.right=False
    self.left=False
    self.stay=True
  def draw_player2(self):
    draw.rect(main,orange,(self.x,self.y,40,20))
    if self.x<=0:
      self.x=0
    if self.x>=400:
      self.x=400
    if self.right:
      self.x+=2
    if self.left:
      self.x-=2
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


def main_window2():#window
  players1=player1()
  players2=player2()
  op=opponent()
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
        if e.key==K_LEFT:
          if players1.right:
            players1.right=False
            players1.stay=True
          else:
            players1.left=True
            players1.stay=False
        if e.key==K_RIGHT:
          if players1.left:
            players1.left=False
            players1.stay=True
          else:
            players1.stay=False
            players1.right=True
        if e.key==K_a:
          if players2.right:
            players2.right=False
            players2.stay=True
          else:
            players2.left=True
            players2.stay=False
        if e.key==K_d:
          if players2.left:
            players2.left=False
            players2.stay=True
          else:
            players2.stay=False
            players2.right=True
        if e.key==K_q:
          quit()
    if op.x>=players1.x-20 and players1.x+20>=op.x:
      if op.y==players1.y:
        op.y=0
        op.x=randrange(10,380,2)
        players1.point+=1
    if op.x>=players2.x-20 and players2.x+20>=op.x:
      if op.y==players2.y:
        op.y=0
        op.x=randrange(10,380,2)
        players2.point+=1
        op.speed+=0.1
    if op.y>=700:
      op.y=0
      op.x=randrange(10,380,4)
      players1.hp-=1
    
    #controls auto
    players1.draw_player1()
    players2.draw_player2()
    op.draw_ex()
    #font: health 
    #player 1
    if players1.hp==3:
      lifep1=fonts.render("Health: "+str(players1.hp),True,green)
    if players1.hp==2:
      lifep1=fonts.render("Health: "+str(players1.hp),True,yellow)
    if players1.hp==1:
      lifep1=fonts.render("Health: "+str(players1.hp),True,red)
    #font: point
    pointsp1=fonts.render("P1 Point: "+str(players1.point),True,blue)
    pointsp2=fonts.render("P2 Point: "+str(players2.point),True,blue)
    #point total
    point_t=fonts.render("Total points: "+str(players1.point+players2.point),True,white)
    #show a points and life
    main.blit(lifep1,(10,10))
    main.blit(pointsp1,(300,80))
    main.blit(pointsp2,(10,80))
    main.blit(point_t,(250,10))
    op.y+=op.speed
    if players1.hp<=0 or players2.hp<=0:
      lost=font2.render("GAME OVER!",True,red)
      main.blit(lost,(50,350))
      done=True
    clock.tick(FPS)
    display.update()
  tm.sleep(5)
  quit()