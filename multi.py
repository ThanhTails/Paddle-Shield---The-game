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
orange=(255,140,0)
white=(255,255,255)
deepink=(255,20,147)
pink=(255,192,203)
class player():
  def __init__(self):
    self.x=width-680
    self.y=250
    self.x2=width-680
    self.y2=300
    self.point=0
    self.y_top=self.y-10
    self.hp=5
    self.up=False
    self.down=False
    self.stay=True
    self.up2=False
    self.down2=False
    self.stay2=True
    self.point2=0
  def draw_player(self):
    draw.rect(main,red,(self.x,self.y,20,40))
    draw.rect(main,orange,(self.x2,self.y2,20,40))
    if self.y<=0:#for player 1
      self.y=0
    if self.y>=500:
      self.y=500
    if self.up:
      self.y-=4
    if self.down:
      self.y+=4
    if self.y2<=0:#for player 2
      self.y2=0
    if self.y2>=500:
      self.y2=500
    if self.up2:
      self.y2-=4
    if self.down2:
      self.y2+=4
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
    self.count_appear=0
    self.speed=0.5
  def draw_bouncy(self):
    draw.rect(main,yellow,(self.x,self.y,20,20))
    if self.up:
      self.y-=2
    if self.down:
      self.y+=2
#danger bullets
class danger():
  def __init__(self):
    #direction
    self.speed=2
    #for orange bullets
    self.x=560
    self.y=randint(4,690)
    self.count_orange=0

    #for pink bullets
    self.x_1=560
    self.y_1=randint(4,690)
    self.count_pink=0
  def draw_danger_orange(self):
    draw.rect(main,orange,(self.x,self.y,20,20))
  def draw_danger_pink(self):
    draw.rect(main,pink,(self.x_1,self.y_1,20,20))
players=player()
op=opponent()
bouncing_bullet=bounce_op()
caution=danger()
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
        if e.key==K_i:
          if players.down:
            players.down=False
            players.stay=True
          else:
            players.up=True
            players.stay=False
        if e.key==K_k:
          if players.up:
            players.up=False
            players.stay=True
          else:
            players.stay=False
            players.down=True
        #for player 2
        if e.key==K_w:
          if players.down2:
            players.down2=False
            players.stay2=True
          else:
            players.up2=True
            players.stay2=False
        if e.key==K_s:
          if players.up2:
            players.up2=False
            players.stay2=True
          else:
            players.stay2=False
            players.down2=True
        if e.key==K_q:
          quit()
    if op.y>=players.y and op.y<=players.y+40:
      if op.x<=players.x:
        op.y=randrange(10,480,4)
        op.x=width
        players.point+=1
        op.speed+=0.1
        bouncing_bullet.speed+=0.1
        players.hp+=1
        caution.count_orange+=1
        caution.count_pink+=1
        bouncing_bullet.count_appear+=1
    if bouncing_bullet.y>=players.y and bouncing_bullet.y<=players.y+40:
      if bouncing_bullet.x<=players.x:
        bouncing_bullet.y=randrange(10,480,4)
        bouncing_bullet.x=width
        players.point+=2
        bouncing_bullet.count_appear=0
        players.hp+=1
        caution.count_orange+=1
        caution.count_pink+=1
    #for player 2
    if op.y>=players.y2 and op.y<=players.y2+40:
      if op.x<=players.x2:
        op.y=randrange(10,480,4)
        op.x=width
        players.point2+=1
        op.speed+=0.1
        bouncing_bullet.speed+=0.1
        players.hp+=1
        caution.count_orange+=1
        caution.count_pink+=1
        bouncing_bullet.count_appear+=1
    if bouncing_bullet.y>=players.y and bouncing_bullet.y<=players.y+40:
      if bouncing_bullet.x<=players.x:
        bouncing_bullet.y=randrange(10,480,4)
        bouncing_bullet.x=width
        players.point+=2
        bouncing_bullet.count_appear=0
        players.hp+=1
        caution.count_orange+=1
        caution.count_pink+=1
    if op.x<=0:
      op.y=randrange(10,480,4)
      op.x=width
      players.hp-=1
      op.speed+=0.1
      bouncing_bullet.count_appear+=1
      caution.count_orange+=1
      caution.count_pink+=1
    if bouncing_bullet.x<=0:
      bouncing_bullet.x=width
      bouncing_bullet.y=randrange(10,484,4)
      players.hp-=1
      bouncing_bullet.speed+=0.1
      bouncing_bullet.count_appear=0
      caution.count_orange+=1
      caution.count_pink+=1
    if bouncing_bullet.y<=0:
      bouncing_bullet.down=True
      bouncing_bullet.up=False
    if bouncing_bullet.y>=500:
      bouncing_bullet.down=False
      bouncing_bullet.up=True
    #controls auto
    
    players.draw_player()
    op.draw_ex()
    if bouncing_bullet.count_appear>=5:
      bouncing_bullet.draw_bouncy()
      bouncing_bullet.x-=bouncing_bullet.speed
    #show danger
    if caution.count_orange>=9:
      caution.draw_danger_orange()
      caution.x-=caution.speed
      if caution.x<=0:
        caution.x=730
        caution.y=randint(4,696)
        caution.count_orange=0
        players.hp-=8
        caution.speed+=1
      if caution.y>=players.y and caution.y<=players.y+40 or caution.y>=players.y2 and caution.y<=players.y2+40:
        if caution.x<=players.x:
          caution.x=730
          caution.y=randint(4,696)
          caution.count_orange=0
          players.hp+=1
          caution.speed+=1
    if caution.count_pink>=7:
      caution.draw_danger_pink()
      caution.x_1-=op.speed+2
      if caution.x_1<=0:
        caution.y_1=randint(4,696)
        caution.x_1=730
        caution.count_pink=0
        caution.speed+=1
      if caution.y_1>=players.y and caution.y_1<=players.y+40 or caution.y_1>=players.y2 and caution.y_1<=players.y2+40:
        if caution.x_1<=players.x:
          caution.x_1=730
          caution.y_1=randint(4,696)
          caution.count_pink=0
          players.hp-=1
          caution.speed+=1
    #font: point
    points=fonts.render("P1 Point: "+str(players.point),True,red)
    pointp2=fonts.render("P2 point: "+str(players.point2),True,orange)
    total=fonts.render("Total: "+str(players.point+players.point2),True,white)
    
    #font: health
    if players.hp>=3:
      life=fonts.render("Health: "+str(players.hp),True,green)
    if players.hp==2:
      life=fonts.render("Health: "+str(players.hp),True,yellow)
    if players.hp==1:
      life=fonts.render("Health: "+str(players.hp),True,red)
    main.blit(life,(300,30))
    main.blit(points,(20,30))
    main.blit(pointp2,(50,460))
    main.blit(total,(150,30))
    op.x-=op.speed
    if players.hp<=0:
      lost=font2.render("GAME OVER!",True,red)
      main.blit(lost,(50,350))
      done=True
    clock.tick(FPS)
    display.update()
  tm.sleep(5)
  quit()