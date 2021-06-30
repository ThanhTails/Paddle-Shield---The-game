from tkinter import*
from pygame import*
from random import*
import time as tm
init()
#Variable
width,height=700,500
FPS=60
clock=time.Clock()
#Color
red=(255,0,0)
orange=(255,140,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)
yellow=(255,255,0)
white=(255,255,255)
deepink=(255,20,147)
deepviolet=(148,0,211)
#Font
fonts=font.Font("freesansbold.ttf",10)
font2=font.Font("freesansbold.ttf",30)

class team1():
  def __init__(self):
    self.x=20
    self.y=280
    self.x2=20
    self.y2=480
    self.up=False#player1
    self.down=False
    self.stay=True
    self.up2=False#player2
    self.down2=False
    self.stay2=True
    self.point=0
  def draw_p1_team1(self):
    draw.rect(main,red,(self.x,self.y,20,40))
    if self.up:
      self.y-=4
    if self.down:
      self.y+=4
    if self.y<=0:
      self.y=0
    if self.y>=460:
      self.y=460
  def draw_p2_team1(self):
    draw.rect(main,deepink,(self.x2,self.y2,20,40))
    if self.up2:
      self.y2-=4
    if self.down2:
      self.y2+=4
    if self.y2<=0:
      self.y2=0
    if self.y2>=460:
      self.y2=460
class team2():
  def __init__(self):
    self.x=660
    self.y=250
    self.x2=660
    self.y2=450
    self.up=False
    self.down=False
    self.stay=True
    self.up2=False
    self.down2=False
    self.stay2=True
    self.point=0
  def draw_p1_team2(self):
    draw.rect(main,orange,(self.x,self.y,20,40))
    if self.up:
      self.y-=4
    if self.down:
      self.y+=4
    if self.y<=0:
      self.y=0
    if self.y>=460:
      self.y=460
  def draw_p2_team2(self):
    draw.rect(main,orange,(self.x2,self.y2,20,40))
    if self.up2:
      self.y2-=4
    if self.down2:
      self.y2+=4
    if self.y2<=0:
      self.y2=0
    if self.y2>=460:
      self.y2=460
class opponent():
  def __init__(self):
    self.x=340
    self.x2=360
    self.y=randrange(2,490,2)
    self.y2=randrange(2,490,2)
    self.speed=1
  def draw_bull(self):
    draw.rect(main,green,(self.x,self.y,20,20))
    draw.rect(main,green,(self.x2,self.y2,20,20))
class bounce_op():
  def __init__(self):
    self.x=340
    self.y=randrange(10,484,4)
    self.x2=360
    self.y2=randrange(10,484,4)
    self.up=False
    self.down=True
    self.up2=False
    self.down2=True
  def draw_bouncy(self):
    draw.rect(main,yellow,(self.x,self.y,20,20))
    draw.rect(main,yellow,(self.x2,self.y2,20,20))
    if self.up:
      self.y-=2
    if self.down:
      self.y+=2
    if self.up2:
      self.y2-=2
    if self.down2:
      self.y2+=2

def arena_2_vs_2():
  players1=team1()
  players2=team2()
  op=opponent()
  bouncy_bullet=bounce_op()
  done=False
  global main
  main=display.set_mode((width,height))
  display.set_caption("1 vs 1")
  while not done:
    main.fill(black)
    for e in event.get():
      if e.type==QUIT:
        done=True
      #keyboard
      if e.type==KEYDOWN:
        if e.key==K_UP:
          if players2.down:
            players2.stay=True
            players2.down=False
          else:
            players2.up=True
            players2.stay=False
        if e.key==K_DOWN:
          if players2.up:
            players2.stay=True
            players2.up=False
          else:
            players2.down=True
            players2.stay=False
        if e.key==K_o:
          if players2.down2:
            players2.stay2=True
            players2.down2=False
          else:
            players2.up2=True
            players2.stay2=False
        if e.key==K_l:
          if players2.up2:
            players2.stay2=True
            players2.up2=False
          else:
            players2.down2=True
            players2.stay2=False
        if e.key==K_q:#quit
          quit()
      #player 2
        if e.key==K_w:
          if players1.down:
            players1.stay=True
            players1.down=False
          else:
            players1.up=True
            players1.stay=False
        if e.key==K_s:
          if players1.up:
            players1.stay=True
            players1.up=False
          else:
            players1.down=True
            players1.stay=False
        
        #player 2 mem 2
        if e.key==K_a:
          if players1.down2:
            players1.stay2=True
            players1.down2=False
          else:
            players1.up2=True
            players1.stay2=False
        if e.key==K_z:
          if players1.up2:
            players1.stay2=True
            players1.up2=False
          else:
            players1.down2=True
            players1.stay2=False
    
    #open
    players1.draw_p1_team1()
    players1.draw_p2_team1()
    players2.draw_p1_team2()
    players2.draw_p2_team2()
    op.draw_bull()
    bouncy_bullet.draw_bouncy()
    op.x-=2
    op.x2+=2
    bouncy_bullet.x-=1
    bouncy_bullet.x2+=1
    #checking crashed
    if op.x<=0:
      op.x=340
      op.y=randrange(2,490,2)
      players1.point-=1

    if op.x2>=700:
      op.x2=360
      op.y2=randrange(2,490,2)
      players2.point-=1

    if op.y<=players1.y+40 and op.y>=players1.y:
      if op.x<=players1.x:
        op.x=340
        op.y=randrange(2,490,2)
        players1.point+=1
    if op.y<=players1.y2+40 and op.y>=players1.y2:
      if op.x<=players1.x:
        op.x=340
        op.y=randrange(2,490,2)
        players1.point+=1
    if op.y2<=players2.y+40 and op.y2>=players2.y:
      if op.x2>=players2.x:
        op.x2=340
        op.y2=randrange(2,490,2)
        players2.point+=1
    if op.y2<=players2.y2+40 and op.y2>=players2.y2:
      if op.x2>=players2.x:
        op.x2=340
        op.y2=randrange(2,490,2)
        players2.point+=1
    #bouncy dude
    if bouncy_bullet.x<=0:
      bouncy_bullet.x=340
      bouncy_bullet.y=randrange(10,484,4)
      players1.point-=1
    if bouncy_bullet.x2>=700:
      bouncy_bullet.x2=360
      bouncy_bullet.y2=randrange(10,484,4)
      players2.point-=1
    if bouncy_bullet.y<=players1.y+40 and bouncy_bullet.y>=players1.y:
      if bouncy_bullet.x<=players1.x:
        bouncy_bullet.x=340
        bouncy_bullet.y=randrange(2,490,2)
        players1.point+=1
    if bouncy_bullet.y2<=players2.y+40 and bouncy_bullet.y2>=players2.y:
      if bouncy_bullet.x2>=players2.x:
        bouncy_bullet.x2=340
        bouncy_bullet.y2=randrange(2,490,2)
        players2.point+=1
    if bouncy_bullet.y<=players1.y2+40 and bouncy_bullet.y>=players1.y2:
      if bouncy_bullet.x<=players1.x:
        bouncy_bullet.x=340
        bouncy_bullet.y=randrange(2,490,2)
        players1.point+=1
    if bouncy_bullet.y2<=players2.y2+40 and bouncy_bullet.y2>=players2.y2:
      if bouncy_bullet.x2>=players2.x:
        bouncy_bullet.x2=340
        bouncy_bullet.y2=randrange(2,490,2)
        players2.point+=1
    #point
    pointp1=fonts.render("Team 1 point: "+str(players1.point),True,white)#p1
    pointp2=fonts.render("Team 2 point: "+str(players2.point),True,white)#p2
    #when ?
    if bouncy_bullet.y<=0:
      bouncy_bullet.down=True
      bouncy_bullet.up=False
    if bouncy_bullet.y>=500:
      bouncy_bullet.down=False
      bouncy_bullet.up=True
    if bouncy_bullet.y2<=0:
      bouncy_bullet.down2=True
      bouncy_bullet.up2=False
    if bouncy_bullet.y2>=500:
      bouncy_bullet.down2=False
      bouncy_bullet.up2=True
    
  
    #show a point and life
    main.blit(pointp1,(200,5))    
    main.blit(pointp2,(400,5)) 
    if players1.point>=10:
      ans=font2.render("Team 1 win",True,green) 
      main.blit(ans,(250,250))
      done=True  
    if players2.point>=10:
      ans=font2.render("Team 2 win",True,green) 
      main.blit(ans,(250,250)) 
      done=True 
    clock.tick(FPS)
    display.update()
  tm.sleep(3)
  quit()