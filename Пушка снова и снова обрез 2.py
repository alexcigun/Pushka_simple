from random import randrange as rnd, choice
from tkinter import *
import math
 
#print (dir(math))
 
import time
root = Tk()
fr = Frame(root)
root.geometry('800x600')
canv = Canvas(root, bg = 'white')
canv.pack(fill=BOTH,expand=1)
 
class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20,450,50,420,width=7)
         
    def fire2_start(self,event):
        self.f2_on = 1
 
    def fire2_end(self,event):
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y)/(event.x-new_ball.x))
        new_ball.vx = self.f2_power*math.cos(self.an)
        new_ball.vy = -self.f2_power*math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10
 
 
    def targetting (self,event=0):
        if event:
            self.an = math.atan((event.y-450)/(event.x-20))    
        if self.f2_on:
            canv.itemconfig(self.id,fill = 'orange')
        else:
            canv.itemconfig(self.id,fill = 'black')
        canv.coords(self.id, 20, 450, 20 + max(self.f2_power, 20) * math.cos(self.an), 450 + max(self.f2_power, 20) * math.sin(self.an))
         
    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id,fill = 'orange')
        else:
            canv.itemconfig(self.id,fill = 'black')
         
 
screen1 = canv.create_text(400,300, text = '',font = '28')
g1 = gun()
bullet = 0
balls = []
 
 
def new_game(event=''):
    global gun, screen1, balls, bullet
    bullet = 0
    balls = []
    canv.bind('<Button-1>',g1.fire2_start)
    canv.bind('<ButtonRelease-1>',g1.fire2_end)
    canv.bind('<Motion>',g1.targetting)
 
    z = 0.03
    canv.delete(gun)
    root.after(750,new_game)
new_game()   
 
mainloop()
