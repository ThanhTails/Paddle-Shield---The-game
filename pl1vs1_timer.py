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
dimgrey=(105,105,105)
#Font
fonts=font.Font("freesansbold.ttf",10)
font2=font.Font("freesansbold.ttf",30)
font3=font.Font("freesansbold.ttf",20)
class player1():
  def __init__(self):
    self.x=20
    self.y=280
    self.up=False
    self.down=False
    self.stay=True
    self.timer=180
    self.point=0
  def draw_p1(self):
    draw.rect(main,red,(self.x,self.y,20,40))
    if self.up:
      self.y-=4
    if self.down:
      self.y+=4
    if self.y<=0:
      self.y=0
    if self.y>=460:
      self.y=460
class player2():
  def __init__(self):
    self.x=680
    self.y=250
    self.up=False
    self.down=False
    self.stay=True
    self.point=0
  def draw_p2(self):
    draw.rect(main,orange,(self.x,self.y,20,40))
    if self.up:
      self.y-=4
    if self.down:
      self.y+=4
    if self.y<=0:
      self.y=0
    if self.y>=460:
      self.y=460
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
    self.count=0
    self.count2=0
  def draw_bouncy(self):
    draw.rect(main,yellow,(self.x,self.y,20,20))
    if self.up:
      self.y-=2
    if self.down:
      self.y+=2
    
  def draw_bouncy2(self):
    draw.rect(main,yellow,(self.x2,self.y2,20,20))
    if self.up2:
      self.y2-=2
    if self.down2:
      self.y2+=2
def arena_1_vs_1():
  players1=player1()
  players2=player2()
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
        if e.key==K_i:
          if players2.down:
            players2.stay=True
            players2.down=False
          else:
            players2.up=True
            players2.stay=False
        if e.key==K_k:
          if players2.up:
            players2.stay=True
            players2.up=False
          else:
            players2.down=True
            players2.stay=False
        if e.key==K_q:
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
    
    #open
    players1.draw_p1()
    players2.draw_p2()
    op.draw_bull()
    if bouncy_bullet.count>=5:
      bouncy_bullet.draw_bouncy()
      bouncy_bullet.x-=1
    if bouncy_bullet.count2>=5:
      bouncy_bullet.draw_bouncy2()
      bouncy_bullet.x2+=1
    op.x-=2
    op.x2+=2
    
    
    #checking crashed
    if op.x<=0:
      op.x=340
      op.y=randrange(2,490,2)
      players1.point-=1
      bouncy_bullet.count+=1
    if op.x2>=700:
      op.x2=360
      op.y2=randrange(2,490,2)
      players2.point-=1
      bouncy_bullet.count2+=1
    if op.y<=players1.y+40 and op.y>=players1.y:
      if op.x>=players1.x:
        op.x=340
        op.y=randrange(2,490,2)
        players1.point+=1
        bouncy_bullet.count+=1
    if op.y2<=players2.y+40 and op.y2>=players2.y:
      if op.x2>=players2.x:
        op.x2=340
        op.y2=randrange(2,490,2)
        players2.point+=1
        bouncy_bullet.count2+=1
    #touching bullet bouncing
    if bouncy_bullet.x<=0:
      bouncy_bullet.x=340
      bouncy_bullet.y=randrange(10,484,4)
      players1.point-=1
      bouncy_bullet.count=0
    if bouncy_bullet.x2>=700:
      bouncy_bullet.x2=360
      bouncy_bullet.y2=randrange(10,484,4)
      players2.point-=1
      bouncy_bullet.count2=0
    if bouncy_bullet.y<=players1.y+40 and bouncy_bullet.y>=players1.y:
      if bouncy_bullet.x<=players1.x:
        bouncy_bullet.x=340
        bouncy_bullet.y=randrange(2,490,2)
        players1.point+=2
        bouncy_bullet.count=0
    if bouncy_bullet.y2<=players2.y+40 and bouncy_bullet.y2>=players2.y:
      if bouncy_bullet.x2>=players2.x:
        bouncy_bullet.x2=340
        bouncy_bullet.y2=randrange(2,490,2)
        players2.point+=2
        bouncy_bullet.count2=0
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
    #point
    pointp1=fonts.render("P1 point: "+str(players1.point),True,white)#p1
    pointp2=fonts.render("P2 point: "+str(players2.point),True,white)#p2
    #time color
    if players1.timer<=180 and players1.timer>=120:
      timer=font3.render("Time: "+str(players1.timer),True,green)
    if players1.timer<=110 and players1.timer>=60:
      timer=font3.render("Time: "+str(players1.timer),True,yellow)
    if players1.timer<=59:
      timer=font3.render("Time: "+str(players1.timer),True,red)
    main.blit(timer,(330,470))
    #show a point and life
    main.blit(pointp1,(150,5))    
    main.blit(pointp2,(400,5)) 
    if players1.timer<=0:
      if players1.point>=players2.point:
        ans=font2.render("Player 1 win",True,green) 
        main.blit(ans,(250,250))
        done=True  
      if players2.point<=players2.point:
        ans=font2.render("Player 2 win",True,green) 
        main.blit(ans,(250,250)) 
        done=True 
    players1.timer-=0.1
    
    clock.tick(FPS)
    display.update()
  tm.sleep(3)
  quit()