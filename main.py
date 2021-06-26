from tkinter import*
import single
import multi
#window
def main_menu():
  global win
  win=Tk()
  win.title("Paddle shield")
  win.geometry("600x700")
  t=Label(win,text="PADDLE SHIELD GAME",font=("Arial",30,"normal"))
  t.grid(row=0,column=0)
  a=Button(win,text="1 player",font=("Arial",20,"normal"),bg="red",command=open_1_player)
  a.grid(row=1,column=0)
  b=Button(win,text="2 player",font=("Arial",20,"normal"),bg="red",command=open_2_player)
  b.grid(row=2,column=0)
  c=Button(win,text="Quit",font=("Arial",20,"normal"),bg="red",command=close)
  c.grid(row=3,column=0)
  ver=Label(win,text="Version 0.1 DEMO")
  ver.grid(row=4,column=0)
  cre=Label(win,text="®2021 ThanhTails")
  cre.grid(row=5,column=0)
def open_1_player():
  single.main_window()
def open_2_player():
  multi.main_window2()
def close():
  print("Bye")
  win.destroy()
main_menu()