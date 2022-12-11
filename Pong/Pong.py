'''Mobin Azadani, Pong ap E3 13,1,400
Special featurse are:
-focusing in screen after opening
-bats don't move out of the screen
-playing wiht multiple balls are available (must be said within the code)
-tow bats are available
- tracking and showing scores with button on screen
- pausing the game
'''

from tkinter import messagebox
from textwrap import fill
from tkinter import *
import random
# building a window
root = Tk()
root.geometry('550x400')
root.title("AP4002 Pong Game")
class Ball:
    start_pos = 100
    dir_speed = [1,-1]
    def __init__(self,master,canvas,ball_x_speed = 0.075,ball_y_speed = 0.075 ):
       
        self.master = master
        self.canvas = canvas
        self.position = Ball.start_pos,Ball.start_pos,Ball.start_pos+10,Ball.start_pos+10
        self.ball = self.canvas.create_oval(*self.position,fill='brown')
        self.ball_x_speed = random.choice(Ball.dir_speed)*ball_x_speed
        self.ball_y_speed = random.choice(Ball.dir_speed)*ball_y_speed
        Ball.start_pos += 20

    def move(self,x,y):

        self.canvas.move(self.ball,x ,y)
    def ball_passed(self,bats_pos):
        
        ball_pos = self.canvas.coords(self.ball)
        if len(bats_pos) ==2:
            if (ball_pos[1] <= 0) and ball_pos[2] <= 550 and ball_pos[0] >= 0:
                return g.restart('1')
            if (ball_pos[3] >= 360 ) and ball_pos[2] <= 550 and ball_pos[0] >= 0:
                return g.restart('2')
            if ball_pos[0] <= 0 or ball_pos[2] >= 550:
                self.ball_x_speed = self.ball_x_speed *-1 +random.choice(Ball.dir_speed)/100
            for i in range(2):
                bat_pos = bats_pos[i]
                if i == 0:
                    bat_got_ball1 = ball_pos[0]>= bat_pos[0] and ball_pos[2] <=bat_pos[2] and ball_pos[3] >= bat_pos[1]
                    bat_got_ball2 = ((ball_pos[0]< bat_pos[0] and ball_pos[2] > bat_pos[0])or(ball_pos[0]< bat_pos[2]and ball_pos[2] > bat_pos[2])) and ball_pos[3] >= bat_pos[1]
                    if bat_got_ball1 or bat_got_ball2  :
                        self.ball_y_speed = self.ball_y_speed *-1 +random.choice(Ball.dir_speed)/100
                elif i == 1:
                    bat_got_ball3 = (ball_pos[0] >= bat_pos[0]) and (ball_pos[2] <= bat_pos[2]) and (ball_pos[1] <= bat_pos[3])
                    bat_got_ball4 = (((ball_pos[0]<= bat_pos[0]) and (ball_pos[2] >= bat_pos[0]))or((ball_pos[0]<= bat_pos[2])and (ball_pos[2] >= bat_pos[2]))) and (ball_pos[1] <= bat_pos[3])
                    if bat_got_ball3 or bat_got_ball4  :
                        self.ball_y_speed = self.ball_y_speed *-1 +random.choice(Ball.dir_speed)/100
        else:
            bat_pos = bats_pos[0]
            if (ball_pos[3] >= 360 ) and ball_pos[2] <= 550 and ball_pos[0] >= 0:
                return g.restart(None)
               
            if ball_pos[0] <= 0 or ball_pos[2] >= 550:
                self.ball_x_speed = self.ball_x_speed *-1 +random.choice(Ball.dir_speed)/100
            bat_got_ball1 = ball_pos[0]>= bat_pos[0] and ball_pos[2] <=bat_pos[2] and ball_pos[3] >= bat_pos[1]
            bat_got_ball2 = ((ball_pos[0]< bat_pos[0] and ball_pos[2] > bat_pos[0])or(ball_pos[0]< bat_pos[2]and ball_pos[2] > bat_pos[2])) and ball_pos[3] >= bat_pos[1]
            if ball_pos[1] <= 0 or bat_got_ball1 or bat_got_ball2  :
                self.ball_y_speed = self.ball_y_speed *-1 +random.choice(Ball.dir_speed)/100

        self.move(self.ball_x_speed,self.ball_y_speed)
        return True
        

class Bat:
    keys = iter(['<Right>','<Left>','<Key-z>','<Key-c>'])
    start_pos = iter([(200,340,250,350),(200,0,250,10)])
    def __init__(self,canvas,speed):
        self.canvas = canvas
        self.position = next(Bat.start_pos)
        self.bat = self.canvas.create_rectangle(*self.position,fill='yellow')
        self.speed = speed
        self.canvas.bind_all(next(Bat.keys),self.move)
        self.canvas.bind_all(next(Bat.keys),self.move)
    def move(self,key):
         if key.keysym == 'Right' or key.keysym =='c' :
            if self.canvas.coords(self.bat)[2] < 550:
                self.canvas.move(self.bat,self.speed,0)
         elif key.keysym == 'Left' or key.keysym =='z':
            if self.canvas.coords(self.bat)[0] > 0:
                self.canvas.move(self.bat,-1*self.speed,0)
class Game:
    players = {'1':0,'2':0}
    balls = []
    bats = []
    def __init__(self,master,ball_number=1,bat_number=1): 
        self.master = master
        self.canvas = Canvas(master,width=550,height=350,bg='#116562')
        self.canvas.grid(row=1,column=0)
        self.canvas.focus()
        self.frame = Frame(self.master,width=550,height=20)
        if bat_number > 1:
            self.show_scores = Button(self.frame,text='Show Scores',font=("Helvetica", 10),width=10,height=1,command=self.scores)
            self.show_scores.grid(column = 0 , row =0)
        self.pause_b = Button(self.frame,text='Pause',font=("Helvetica", 10),width=10,height=1,command=self.Pause)
        self.pause_b.grid(column = 1 , row =0)
        self.frame.grid(row=0,column=0)
        self.game_play = True
        for i in range(ball_number):
            Game.balls.append( Ball(master,self.canvas))
        for i in range(bat_number):
            Game.bats.append(Bat(self.canvas,6))
    def Pause(self):
        self.game_play = False
        while not messagebox.askyesno("Game paused","Resume game?\n(By canceling game willbe restarted))"):
            pass
        self.game_play = True
        self.game_control()
    def scores(self):
        self.game_play = False
        while not messagebox.askquestion("Score Board",f"PLayer1:   {Game.players['1']} pnt\n Player2:  {Game.players['2']} pnt"):
            pass
        self.game_play = True
        self.game_control()
            
    def game_control(self):
        bats_pos =[self.canvas.coords(bat.bat) for bat in Game.bats]
        #print(bats_pos)
        for ball in Game.balls:
            result = ball.ball_passed(bats_pos)
            if not result:
                return
        if self.game_play:
            self.canvas.after(1,self.game_control)
    def restart(self,player):
        if player:
            Game.players[player] += 1
 
        if not messagebox.askyesno("Continue","Do you want to continue?"):
            self.master.destroy()
            return 

        for bat in Game.bats:
                bat_pos = self.canvas.coords(bat.bat)
                self.canvas.move(bat.bat,bat.position[0]-bat_pos[0],bat.position[1]-bat_pos[1])
        for ball in Game.balls:
            ball_pos = self.canvas.coords(ball.ball)
            self.canvas.move(ball.ball,ball.position[0]-ball_pos[0],ball.position[1]-ball_pos[1])
        self.game_control()

g = Game(root,ball_number=3,bat_number=2) # example of playing with tow bats and balls 
g.game_control()
root.mainloop()