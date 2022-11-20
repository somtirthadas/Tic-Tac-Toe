import tkinter as t
import random

def new_game():
    global player
    player=random.choice(players)
    label.config(text=(player + "'s turn"))
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text='',bg='navajo white')

def empty_space():
    space=9
    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text']!='':
                space -=1
    
    if space==0:
        return False
    else:
        return True

def check_winner():
    for row in range(3):
        if buttons[row][0]['text']==buttons[row][1]['text']==buttons[row][2]['text']!="":
            buttons[row][0].config(bg='forest green')
            buttons[row][1].config(bg='forest green')
            buttons[row][2].config(bg='forest green')
            return True
    for col in range(3):
        if buttons[0][col]['text']==buttons[1][col]['text']==buttons[2][col]['text']!="":
            buttons[0][col].config(bg='forest green')
            buttons[1][col].config(bg='forest green')
            buttons[2][col].config(bg='forest green')
            return True
    if buttons[0][0]['text']==buttons[1][1]['text']==buttons[2][2]['text']!="":
        buttons[0][0].config(bg='forest green')
        buttons[1][1].config(bg='forest green')
        buttons[2][2].config(bg='forest green')
        return True
    elif buttons[0][2]['text']==buttons[1][1]['text']==buttons[2][0]['text']!="":
        buttons[0][2].config(bg='forest green')
        buttons[1][1].config(bg='forest green')
        buttons[2][0].config(bg='forest green')
        return True
    elif empty_space() is False:
        for i in range(3):
            for j in range(3):
                buttons[i][j].config(bg='yellow')
        return 'Tie'
    else:
        return False

def next_turn(row,col):
    global player
    if buttons[row][col]['text']=='' and check_winner() is False:
        if player==players[0]:
            buttons[row][col]['text']=player
            if check_winner() is False:
                player=players[1]
                label.config(text=(players[1] + "'s turn"))
            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))
            elif check_winner() =='Tie':
                label.config(text="Tie")
        else:
            buttons[row][col]['text']=player
            if check_winner() is False:
                player=players[0]
                label.config(text=(players[0] + "'s turn"))
            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))
            elif check_winner() =='Tie':
                label.config(text="Match Tie!!")
    

if __name__=='__main__':

    window=t.Tk()
    window.title("Tic Tac Toe")
    window.config(bg='peru')
    
    players=["X","O"]
    player=random.choice(players)
    buttons=[[0,0,0],[0,0,0],[0,0,0]]
    
    label=t.Label(text=player + "'s turn",font=('Helvetica',40),bg='peru')
    label.pack(side='top')
    
    reset_button=t.Button(text='Play Again',font=('Helvetica',20),bg='tan',command=new_game) #Restart button #light salmon
    reset_button.pack(side='top')

    frame=t.Frame(window)
    frame.pack()

    for row in range(3):
        for col in range(3):
            buttons[row][col]=t.Button(frame,text='',font=('Helvetica',40),width = 4, height = 2,bg='navajo white',command=lambda row = row,col=col:next_turn(row,col))

            buttons[row][col].grid(row=row,column=col)

    window.mainloop()

