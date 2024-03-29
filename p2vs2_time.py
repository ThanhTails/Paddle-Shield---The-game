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
dimgrey=(105,105,105)
pink=(255,192,203)
#Font
fonts=font.Font("freesansbold.ttf",10)
font2=font.Font("freesansbold.ttf",30)
font3=font.Font("freesansbold.ttf",20)
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
    self.timer=500
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
    self.x=680
    self.y=250
    self.x2=680
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
    draw.rect(main,blue,(self.x2,self.y2,20,40))
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
#danger
#for team 1
class danger1():
  def __init__(self):
    #direction
    #for orange bullets
    self.x=340
    self.y=randint(4,690)
    self.count_orange=0

    #for pink bullets
    self.x_1=340
    self.y_1=randint(4,690)
    self.count_pink=0
  def draw_danger_orange(self):
    draw.rect(main,orange,(self.x,self.y,20,20))
  def draw_danger_pink(self):
    draw.rect(main,pink,(self.x_1,self.y_1,20,20))
#for team 2
class danger2():
  def __init__(self):
    #direction
    #for orange bullets
    self.x=360
    self.y=randint(4,690)
    self.count_orange=0

    #for pink bullets
    self.x_1=360
    self.y_1=randint(4,690)
    self.count_pink=0
  def draw_danger_orange(self):
    draw.rect(main,orange,(self.x,self.y,20,20))
  def draw_danger_pink(self):
    draw.rect(main,pink,(self.x_1,self.y_1,20,20))
def arena_2_vs_2():
  players1=team1()
  players2=team2()
  op=opponent()
  bouncy_bullet=bounce_op()
  caution1=danger1()
  caution2=danger2()
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
        if e.key==K_j:
          if players2.down:
            players2.stay=True
            players2.down=False
          else:
            players2.up=True
            players2.stay=False
        if e.key==K_m:
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
    if bouncy_bullet.count>=5:
      bouncy_bullet.draw_bouncy()
      bouncy_bullet.x-=1
    if bouncy_bullet.count2>=5:
      bouncy_bullet.draw_bouncy()
      bouncy_bullet.x2+=1
    #caution!
    #p1
    if caution1.count_orange>=9:
      caution1.draw_danger_orange()
      caution1.x-=2
      if caution1.y>=players1.y and caution1.y<=players1.y+40:
        if caution1.x<=players1.x:
          caution1.x=340
          caution1.y=randint(2,698)
          players1.point+=1
          caution1.count_orange=0
      if caution1.y>=players1.y2 and caution1.y<=players1.y2+40:
        if caution1.x<=players1.x2:
          caution1.x=340
          caution1.y=randint(2,698)
          players1.point+=1
          caution1.count_orange=0
      if caution1.x<=0:
        caution1.x=340
        caution1.y=randint(2,698)
        players1.point-=5
        caution1.count_orange=0
    if caution1.count_pink>=7:
      caution1.draw_danger_pink()
      caution1.x_1-=2
      if caution1.y_1>=players1.y and caution1.y_1<=players1.y+40:
        if caution1.x_1<=players1.x:
          caution1.x_1=340
          caution1.y_1=randint(2,698)
          caution1.count_pink=0
          players1.point-=1
      if caution1.y_1>=players1.y2 and caution1.y_1<=players1.y2+40:
        if caution1.x_1<=players1.x2:
          caution1.x_1=340
          caution1.y_1=randint(2,698)
          caution1.count_pink=0
          players1.point-=1
      if caution1.x_1<=0:
        caution1.x_1=340
        caution1.y_1=randint(2,698) 
        caution1.count_pink=0
    #p2
    if caution2.count_orange>=9:
      caution2.draw_danger_orange()
      caution2.x+=2
      if caution2.y>=players2.y and caution2.y<=players2.y+40:
        if caution2.x<=players2.x:
          caution2.x=360
          caution2.y=randint(2,698)
          players2.point+=1
          caution2.count_orange=0
      if caution2.y>=players2.y2 and caution2.y<=players2.y2+40:
        if caution2.x<=players2.x2:
          caution2.x=360
          caution2.y=randint(2,698)
          players2.point+=1
          caution2.count_orange=0
      if caution2.x<=0:
        caution2.x=360
        caution2.y=randint(2,698)
        players2.point-=5
        caution2.count_orange=0
    if caution2.count_pink>=7:
      caution2.draw_danger_pink()
      caution2.x_1+=2
      if caution2.y_1>=players2.y and caution1.y_1<=players2.y+40:
        if caution2.x_1<=players2.x:
          caution2.x_1=360
          caution2.y_1=randint(2,698)
          caution2.count_pink=0
          players2.point-=1
      if caution2.y_1>=players2.y2 and caution1.y_1<=players2.y2+40:
        if caution2.x_1<=players2.x2:
          caution2.x_1=360
          caution2.y_1=randint(2,698)
          caution2.count_pink=0
          players2.point-=1
      if caution1.x_1<=0:
        caution1.x_1=360
        caution1.y_1=randint(2,698)
        caution2.count_pink=0
    op.x-=2
    op.x2+=2
    
    
    #checking crashed
    if op.x<=0:
      op.x=340
      op.y=randrange(2,490,2)
      players1.point-=1
      bouncy_bullet.count+=1
      caution1.count_orange+=1
      caution1.count_pink+=1
    if op.x2>=700:
      op.x2=360
      op.y2=randrange(2,490,2)
      players2.point-=1
      bouncy_bullet.count2+=1
      caution2.count_orange+=1
      caution2.count_pink+=1
    if op.y<=players1.y+40 and op.y>=players1.y:
      if op.x<=players1.x:
        op.x=340
        op.y=randrange(2,490,2)
        players1.point+=1
        bouncy_bullet.count+=1
        caution1.count_orange+=1
        caution1.count_pink+=1
    if op.y<=players1.y2+40 and op.y>=players1.y2:
      if op.x<=players1.x:
        op.x=340
        op.y=randrange(2,490,2)
        players1.point+=1
        bouncy_bullet.count+=1
        caution1.count_orange+=1
        caution1.count_pink+=1
    if op.y2<=players2.y+40 and op.y2>=players2.y:
      if op.x2>=players2.x:
        op.x2=340
        op.y2=randrange(2,490,2)
        players2.point+=1
        bouncy_bullet.count2+=1
        caution2.count_orange+=1
        caution2.count_pink+=1
    if op.y2<=players2.y2+40 and op.y2>=players2.y2:
      if op.x2>=players2.x:
        op.x2=340
        op.y2=randrange(2,490,2)
        players2.point+=1
        bouncy_bullet.count2+=1
        caution2.count_orange+=1
        caution2.count_pink+=1
    #bouncy dude
    if bouncy_bullet.x<=0:
      bouncy_bullet.x=340
      bouncy_bullet.y=randrange(10,484,4)
      players1.point-=1
      bouncy_bullet.count=0
      caution1.count_orange+=1
      caution1.count_pink+=1
    if bouncy_bullet.x2>=700:
      bouncy_bullet.x2=360
      bouncy_bullet.y2=randrange(10,484,4)
      players2.point-=1
      bouncy_bullet.count2=0
      caution2.count_orange+=1
      caution2.count_pink+=1
    if bouncy_bullet.y<=players1.y+40 and bouncy_bullet.y>=players1.y:
      if bouncy_bullet.x<=players1.x:
        bouncy_bullet.x=340
        bouncy_bullet.y=randrange(2,490,2)
        players1.point+=2
        bouncy_bullet.count=0
        caution1.count_orange+=1
        caution1.count_pink+=1
    if bouncy_bullet.y2<=players2.y+40 and bouncy_bullet.y2>=players2.y:
      if bouncy_bullet.x2>=players2.x:
        bouncy_bullet.x2=340
        bouncy_bullet.y2=randrange(2,490,2)
        players2.point+=2
        bouncy_bullet.count=0
        caution2.count_orange+=1
        caution2.count_pink+=1
    if bouncy_bullet.y<=players1.y2+40 and bouncy_bullet.y>=players1.y2:
      if bouncy_bullet.x<=players1.x:
        bouncy_bullet.x=340
        bouncy_bullet.y=randrange(2,490,2)
        players1.point+=2
        bouncy_bullet.count2=0
        caution1.count_orange+=1
        caution1.count_pink+=1
    if bouncy_bullet.y2<=players2.y2+40 and bouncy_bullet.y2>=players2.y2:
      if bouncy_bullet.x2>=players2.x:
        bouncy_bullet.x2=340
        bouncy_bullet.y2=randrange(2,490,2)
        players2.point+=2
        bouncy_bullet.count2=0
        caution2.count_orange+=1
        caution2.count_pink+=1
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
    pointp1=fonts.render("Team 1 point: "+str(players1.point),True,white)#p1
    pointp2=fonts.render("Team 2 point: "+str(players2.point),True,white)#p2
    #time color
    if players1.timer>=300:
      timer=font3.render("Time: "+str(players1.timer),True,green)
    if players1.timer>=200 and players1.timer<=299:
      timer=font3.render("Time: "+str(players1.timer),True,yellow)
    if players1.timer<=199:
      timer=font3.render("Time: "+str(players1.timer),True,red)
    main.blit(timer,(330,470))
    #show a point and life
    main.blit(pointp1,(150,5))    
    main.blit(pointp2,(400,5))
    
    if players1.timer<=0:
      if players1.point>=players2.point:
        ans=font2.render("Team 1 win",True,green) 
        main.blit(ans,(250,250))
        done=True  
      if players2.point>=players1.point:
        ans=font2.render("Team 2 win",True,green) 
        main.blit(ans,(250,250)) 
        done=True 
    players1.timer-=0.1
    clock.tick(FPS)
    display.update()
  tm.sleep(3)
  quit()