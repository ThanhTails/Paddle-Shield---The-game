from pygame import*
import time as tm
from random import*
init()
#var
width,height=700,540
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
    self.x=width-650
    self.y=250
    self.point=0
    self.y_top=self.y-10
    self.hp=5
    self.up=False
    self.down=False
    self.stay=True
  def draw_player(self):
    draw.rect(main,red,(self.x,self.y,20,40))
    if self.y<=0:
      self.x=0
    if self.y>=500:
      self.x=500
    if self.up:
      players.y-=4
    if self.down:
      players.y+=4
class opponent():
  def __init__(self):
    self.y=randrange(10,480,4)
    self.x=width
    self.speed=1
  def draw_ex(self):
    draw.rect(main,green,(self.x,self.y,20,20))
    if self.x<=0:
      self.y=randrange(10,480,4)
      self.x=width
#bouncing bullet
class bounce_op():
  def __init__(self):
    self.x=width
    self.y=randrange(10,484,4)
    self.up=False
    self.down=True
  def draw_bouncy(self):
    draw.rect(main,yellow,(self.x,self.y,20,20))
    if self.up:
      self.y-=2
    if self.down:
      self.y+=2
players=player()
op=opponent()
bouncing_bullet=bounce_op()
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
        if e.key==K_UP or e.key==K_w:
          if players.down:
            players.down=False
            players.stay=True
          else:
            players.up=True
            players.stay=False
        if e.key==K_DOWN or e.key==K_s:
          if players.up:
            players.up=False
            players.stay=True
          else:
            players.stay=False
            players.down=True
        if e.key==K_q:
          quit()
    if op.y>=players.y and op.y<=players.y+40:
      if op.x<=players.x:
        op.y=randrange(10,480,4)
        op.x=width
        players.point+=1
        op.speed+=0.1
    if bouncing_bullet.y>=players.y and bouncing_bullet.y<=players.y+40:
      if bouncing_bullet.x<=players.x:
        bouncing_bullet.y=randrange(10,480,4)
        bouncing_bullet.x=width
        players.point+=1
        op.speed+=0.1
    if op.x<=0:
      op.y=randrange(10,480,4)
      op.x=width
      players.hp-=1
      op.speed+=0.1
    if bouncing_bullet.x<=0:
      bouncing_bullet.x=width
      bouncing_bullet.y=randrange(10,484,4)
      players.hp-=1
      op.speed+=1
    if bouncing_bullet.y<=0:
      bouncing_bullet.down=True
      bouncing_bullet.up=False
    if bouncing_bullet.y>=500:
      bouncing_bullet.down=False
      bouncing_bullet.up=True
    
    #controls auto
    
    players.draw_player()
    op.draw_ex()
    bouncing_bullet.draw_bouncy()
    #font: point
    points=fonts.render("Point: "+str(players.point),True,blue)
    
    #font: health
    if players.hp<=5 and players.hp>=3:
      life=fonts.render("Health: "+str(players.hp),True,green)
    if players.hp==2:
      life=fonts.render("Health: "+str(players.hp),True,yellow)
    if players.hp==1:
      life=fonts.render("Health: "+str(players.hp),True,red)
    main.blit(life,(300,30))
    main.blit(points,(20,30))

    op.x-=op.speed
    bouncing_bullet.x-=op.speed
    if players.hp<=0:
      lost=font2.render("GAME OVER!",True,red)
      main.blit(lost,(50,350))
      done=True
    clock.tick(FPS)
    display.update()
  tm.sleep(5)
  quit()