from tkinter import*
import single
import pl1vs1,p1vs1_score,pl1vs1_timer,pl2vs2,p2vs2_score,p2vs2_time,multi
#window
def main_menu():
  global win
  win=Tk()
  win.title("Paddle shield")
  win.geometry("600x400")
  t=Label(win,text="PADDLE SHIELD GAME",font=("Arial",30,"normal"))
  t.grid(row=0,column=0)
  a=Button(win,text="1 player",font=("Arial",20,"normal"),bg="red",command=open_1_player)
  a.grid(row=1,column=0)
  b=Button(win,text="2 player vs 2 player (4 player)",font=("Arial",20,"normal"),bg="red",command=open_2_player)
  b.grid(row=2,column=0)
  d=Button(win,text="2 player",font=("Arial",20,"normal"),bg="red",command=open_multiplayer)
  d.grid(row=4,column=0)
  c=Button(win,text="Quit",font=("Arial",20,"normal"),bg="red",command=close)
  c.grid(row=8,column=0)
  #another
  v1=Button(win,text="1 vs 1 (PVP)",font=("Arial",20,"normal"),bg="red",command=open_1_v_1)
  v1.grid(row=3,column=0)
  ver=Label(win,text="Version 0.2 DEMO")
  ver.grid(row=9,column=0)
  cre=Label(win,text="®2021 ThanhTails")
  cre.grid(row=10,column=0)
def open_1_player():
  single.main_window()
def open_2_player():# 2 vs 2
  global s
  s=Tk()
  a=Button(s,text="Normal - Which team out of health: lost",command=open_2_vs_2)
  a.pack()
  c=Button(s,text="Score limit - Which team 10 points first is the winner",command=open_2_vs_2_score)
  c.pack()
  b=Button(s,text="Time limit - Which team best score is the winner. You have 3 minutes.",command=open_timer_2)
  b.pack()
  cl=Button(s,text="Close",command=close_2_v_2)
  cl.pack()
def open_1_v_1():
  global s
  s=Tk()
  a=Button(s,text="Normal - Who out of health: lost",command=open_1_vs_1_2)
  a.pack()
  c=Button(s,text="Score limit - Who 10 points first is the winner",command=open_1_vs_1_score)
  c.pack()
  b=Button(s,text="Time limit - WHo best score is the winner. You have 3 minutes.",command=open_timer)
  b.pack()
  cl=Button(s,text="Close",command=close_2_v_2)
  cl.pack()
def close_2_v_2():
  s.destroy()
def open_2_vs_2_score():
  p2vs2_score.arena_2_vs_2()
def open_1_vs_1_2():
  pl1vs1.arena_1_vs_1()
def open_1_vs_1_score():
  p1vs1_score.arena_1_vs_1()
def open_timer():
  pl1vs1_timer.arena_1_vs_1()
def open_timer_2():
  p2vs2_time.arena_2_vs_2()
def close():
  print("Bye")
  win.destroy()
def open_2_vs_2():
  pl2vs2.arena_2_vs_2()
def open_multiplayer():
  multi.main_window()
main_menu()