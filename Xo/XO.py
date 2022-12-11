#Mobin Azadani- XO game 17.12.1400
#extra options:
#-getting name of each player just after runnig
#-keeping each players point after a match

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def name():
    '''via this function program receives plyers name and until it doesn't
        benn kill, main window (root) will not strart'''
    names = [] 
    def get_entry():
        '''this function activates when the ok button is pressed and
            returns entries'''
        nonlocal names
        first,second = e1.get(),e2.get()
        w.destroy()
        names.append((first[:7],second[:7]))
        
    w = Tk() #creating entry window
    w.title('Tic-Tac-Toe')
    w.resizable(False, False)
    
    Label(w, text="1st player :",font=("Helvetica", 12)).grid(row=0)
    Label(w, text="2nd player :",font=("Helvetica", 12)).grid(row=1)
    Button(w,text="ok",font=("Helvetica", 12),width=4,command=get_entry).grid(row=2)
    e1 = Entry(w,width=6,font=("Helvetica", 15))
    e2 = Entry(w,width=6,font=("Helvetica", 15))

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    
    w.mainloop()
    return names    

class game(): #this class holds main varibales and methods for  the game.
    board = {} #a dictionary to hold x and o places (column,row):x or o .
    turn = 'X' #a string to know which player turn it is.
    player = {'X':0,'O':0} #a dictionary to hold each players point.
    p1 = 'X' # these tow strings are used after each game to hold order of points
    p2 = 'O' #- combined with 'player'.
    def move(self,btn,number):
        '''This method activates after a board button is pressed and updates the
            board and dictionary'''
        btn.config(text = game.turn)
        game.board[number] = game.turn
        btn['state'] = 'disabled'
        game.turn = 'O' if game.turn == 'X' else 'X' #changes the turn
        Board.game_ended(number)   
        
    def game_ended(self,number):
        ''' this function is for whether the game is ended or not'''
        victory_pattern = [(1,0),(0,1),(1,1),(-1,1)] #this list stores victory vectors   
        for square in game.board:
            for pattern in victory_pattern:
                for multiply in range(1,3):#this function produces points to check with main square
                    othersquare_x = square[0]+(multiply*pattern[0])
                    othersquare_y = square[1]+(multiply*pattern[1])
                    if (othersquare_x,othersquare_y) not in game.board:
                        break
                    if game.board[square] != game.board[(othersquare_x,othersquare_y)]:
                        break
                    elif multiply == 2:
                        #all squares were equall and a player won the game!
                        for i in range(9):
                            #disalbling all board buttons
                            exec(f'board_b{i}["state"] = "disabled"')
                        for i in [square,(othersquare_x,othersquare_y),((square[0]+othersquare_x)/2,(square[1]+othersquare_y)/2)]:
                            #coloring wining squares
                            exec(f'board_b{int(i[1]*3 + i[0])}.config(bg="light green")')
                        game.player[game.board[square]] += 1
                        score_board.config(text = f'{names[0][0].upper():^9}: {game.player[game.p1]} {names[0][1].upper():^9}: {game.player[game.p2]}')
                        
                        if not messagebox.askokcancel("Tic Tac Toe", f"winner winner chicken dinner!\n{game.board[square]} won!\n Load next game?"):
                            return
                        Board.restart(True,False)
                        return
                                            
                    
        if len(game.board) == 9: #this if is for when nor player won and all squares are taken           
            if not messagebox.askokcancel("Tic Tac Toe", "It's a tie!!\nNo one wins!\n Load next game?"):
                return
            Board.restart(True,False)
            return
        
    def restart(self,keep_points=False,restart_b=True):
        '''this function activates when player presses the restart button or
            when game ends with game_ended'''
        if restart_b: #if player activated the method
            if not messagebox.askokcancel("Warning","By restarting records are being lost.\n Do you want to restart?"):
                    return
        game.board.clear()
        game.turn = 'X'
        game.player['X'],game.player['O'] = game.player['O'],game.player['X']
        game.p1,game.p2 = game.p2,game.p1
        if not keep_points:
            game.player['X'] = 0
            game.player['O'] = 0
            

        score_board.config(text = f'{names[0][0].upper():^9}: {game.player[game.p1]} {names[0][1].upper():^9}: {game.player[game.p2]}')
        for i in range(9):
            exec(f'board_b{i}.config(text = "   ",bg="white")')
            exec(f'board_b{i}["state"] = "normal"')
            
names = name()

root = Tk()
root.geometry('500x550')
root.title('Tic-Tac-Toe')
root.resizable(False, False)
root.config(bg='#116562')

menu_frame = ttk.Frame(root, width =500,)#a frame for holding score board and restart button
board_frame = ttk.Frame(root,width =180,height=500 )#frame of board game

menu_frame.grid(column = 0 , row =0,pady=10)
board_frame.grid(column = 0,row =1,padx=60)

Board = game()

score_board = Label(menu_frame,text=f'{names[0][0].upper():^9}: {game.player[game.p1]} {names[0][1].upper():^9}: {game.player[game.p2]}',font=("Helvetica", 20),width=20,height=1)
score_board.grid(column = 1 , row =0)



restart = Button(menu_frame,text = 'Restart',font=("Helvetica", 10),height=3,command = Board.restart)
restart.grid(column = 0 , row = 0)
for i in range(9):# creating similar buttons
    exec(f'board_b{i} = Button( board_frame,activebackground="ghost white",text = "    ",font=("Helvetica", 25), height=3, width=6,bg="white",command = lambda: Board.move(board_b{i},({i%3 },{i//3})))')
    exec(f'board_b{i}.grid(column = {i%3 } ,row = {i//3})')   
root.mainloop()

