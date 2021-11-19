#Holiday HW - Class 11
#Tic Tac Toe using Tkinter module.

#importing tkinter and messagebox, create and name window

import tkinter as tk                #importing tkinter
from tkinter import messagebox      #importing messagebox from the tkinter module
win=tk.Tk()                         #creating tkinter window
win.title("Tic-Tac-Toe by Lowell Monis")            #window title
win['bg']="slateblue"               #window colour
xscore=0                            #creating variables for score
yscore=0

#creation of click function for Tic-Tac-Toe grid with error message for used box

def b_click(b):
    global clicked,count
    if b["text"]=="" and clicked==True:
        b["text"]="X"
        clicked=False
        count+=1
        winner_check()
    elif b["text"]=="" and clicked==False:
        b["text"]="O"
        clicked=True
        count+=1
        winner_check()
    else:
        messagebox.showerror("Tic-Tac-Toe","That box is already filled. Pick another one!")

#definition of logical function to determine winner

def winner_check():
    global winner
    winner=False
    
    #checking if X wins via all possible arrangements
    
    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
        global xscore
        xscore+=1
        b1.config(bg="green")
        b1.config(fg="white")
        b2.config(bg="green")
        b2.config(fg="white")
        b3.config(bg="green")
        b3.config(fg="white")
        winner=True
        messagebox.showinfo("Tic-Tac-Toe", "X wins!")
        nextmatch()
    elif b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
        xscore+=1
        b4.config(bg="green")
        b4.config(fg="white")
        b5.config(bg="green")
        b5.config(fg="white")
        b6.config(bg="green")
        b6.config(fg="white")
        winner=True
        messagebox.showinfo("Tic-Tac-Toe", "X wins!")
        nextmatch()
    elif b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X":
        xscore+=1
        b7.config(bg="green")
        b7.config(fg="white")
        b8.config(bg="green")
        b8.config(fg="white")
        b9.config(bg="green")
        b9.config(fg="white")
        winner=True
        messagebox.showinfo("Tic-Tac-Toe", "X wins!")
        nextmatch()
    elif b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X":
        xscore+=1
        b1.config(bg="green")
        b1.config(fg="white")
        b4.config(bg="green")
        b4.config(fg="white")
        b7.config(bg="green")
        b7.config(fg="white")
        winner=True
        messagebox.showinfo("Tic-Tac-Toe", "X wins!")
        nextmatch()
    elif b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X":
        xscore+=1
        b2.config(bg="green")
        b2.config(fg="white")
        b5.config(bg="green")
        b5.config(fg="white")
        b8.config(bg="green")
        b8.config(fg="white")
        winner=True
        messagebox.showinfo("Tic-Tac-Toe", "X wins!")
        nextmatch()
    elif b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":
        xscore+=1
        b3.config(bg="green")
        b3.config(fg="white")
        b6.config(bg="green")
        b6.config(fg="white")
        b9.config(bg="green")
        b9.config(fg="white")
        winner=True
        messagebox.showinfo("Tic-Tac-Toe", "X wins!")
        nextmatch()
    elif b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X":
        xscore+=1
        b1.config(bg="green")
        b1.config(fg="white")
        b5.config(bg="green")
        b5.config(fg="white")
        b9.config(bg="green")
        b9.config(fg="white")
        winner=True
        messagebox.showinfo("Tic-Tac-Toe", "X wins!")
        nextmatch()
    elif b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X":
        xscore+=1
        b3.config(bg="green")
        b3.config(fg="white")
        b5.config(bg="green")
        b5.config(fg="white")
        b7.config(bg="green")
        b7.config(fg="white")
        winner=True
        messagebox.showinfo("Tic-Tac-Toe", "X wins!")
        nextmatch()
    
    #checking if O wins via all possible arrangements
        
    elif b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O":
        global yscore
        yscore+=1
        b1.config(bg="green")
        b1.config(fg="white")
        b2.config(bg="green")
        b2.config(fg="white")
        b3.config(bg="green")
        b3.config(fg="white")
        winner=True
        messagebox.showinfo("Tic-Tac-Toe", "O wins!")
        nextmatch()
    elif b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O":
        yscore+=1
        b4.config(bg="green")
        b4.config(fg="white")
        b5.config(bg="green")
        b5.config(fg="white")
        b6.config(bg="green")
        b6.config(fg="white")
        winner=True
        messagebox.showinfo("Tic-Tac-Toe", "O wins!")
        nextmatch()
    elif b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O":
        yscore+=1
        b7.config(bg="green")
        b7.config(fg="white")
        b8.config(bg="green")
        b8.config(fg="white")
        b9.config(bg="green")
        b9.config(fg="white")
        winner=True
        messagebox.showinfo("Tic-Tac-Toe", "O wins!")
        nextmatch()
    elif b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O":
        yscore+=1
        b1.config(bg="green")
        b1.config(fg="white")
        b4.config(bg="green")
        b4.config(fg="white")
        b7.config(bg="green")
        b7.config(fg="white")
        winner=True
        messagebox.showinfo("Tic-Tac-Toe", "O wins!")
        nextmatch()
    elif b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O":
        yscore+=1
        b2.config(bg="green")
        b2.config(fg="white")
        b5.config(bg="green")
        b5.config(fg="white")
        b8.config(bg="green")
        b8.config(fg="white")
        winner=True
        messagebox.showinfo("Tic-Tac-Toe", "O wins!")
        nextmatch()
    elif b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O":
        yscore+=1
        b3.config(bg="green")
        b3.config(fg="white")
        b6.config(bg="green")
        b6.config(fg="white")
        b9.config(bg="green")
        b9.config(fg="white")
        winner=True
        messagebox.showinfo("Tic-Tac-Toe", "O wins!")
        nextmatch()
    elif b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O":
        yscore+=1
        b1.config(bg="green")
        b1.config(fg="white")
        b5.config(bg="green")
        b5.config(fg="white")
        b9.config(bg="green")
        b9.config(fg="white")
        winner=True
        messagebox.showinfo("Tic-Tac-Toe", "O wins!")
        nextmatch()
    elif b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O":
        yscore+=1
        b3.config(bg="green")
        b3.config(fg="white")
        b5.config(bg="green")
        b5.config(fg="white")
        b7.config(bg="green")
        b7.config(fg="white")
        winner=True
        messagebox.showinfo("Tic-Tac-Toe", "O wins!")
        nextmatch()
    
    #checking for draw
        
    elif count==9 and winner==False:
        messagebox.showinfo("Tic-Tac-Toe", "It's a Draw!")
        nextmatch()

#definition of the end game button
        
def end():
    if xscore>yscore:
        messagebox.showinfo("Tic-Tac-Toe", "X wins the game! See you next time!")
    elif yscore>xscore:
        messagebox.showinfo("Tic-Tac-Toe", "O wins the game! See you next time!")
    elif xscore==yscore:
        messagebox.showinfo("Tic-Tac-Toe", "It's a Tie! See you next time!")
    win.destroy()
        
#definition of the function to start next game / basic format of the grid
    
def nextmatch():

    #creation of buttons

    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global clicked,count
    clicked=True
    count=0

    b1=tk.Button(win,text="",font=("Times New Roman",20),height=3,width=6,
                 bg="SystemButtonFace",command=lambda: b_click(b1))
    b2=tk.Button(win,text="",font=("Times New Roman",20),height=3,width=6,
                 bg="SystemButtonFace",command=lambda: b_click(b2))
    b3=tk.Button(win,text="",font=("Times New Roman",20),height=3,width=6,
                 bg="SystemButtonFace",command=lambda: b_click(b3))
    b4=tk.Button(win,text="",font=("Times New Roman",20),height=3,width=6,
                 bg="SystemButtonFace",command=lambda: b_click(b4))
    b5=tk.Button(win,text="",font=("Times New Roman",20),height=3,width=6,
                 bg="SystemButtonFace",command=lambda: b_click(b5))
    b6=tk.Button(win,text="",font=("Times New Roman",20),height=3,width=6,
                 bg="SystemButtonFace",command=lambda: b_click(b6))
    b7=tk.Button(win,text="",font=("Times New Roman",20),height=3,width=6,
                 bg="SystemButtonFace",command=lambda: b_click(b7))
    b8=tk.Button(win,text="",font=("Times New Roman",20),height=3,width=6,
                 bg="SystemButtonFace",command=lambda: b_click(b8))
    b9=tk.Button(win,text="",font=("Times New Roman",20),height=3,width=6,
                 bg="SystemButtonFace",command=lambda: b_click(b9))

    #creation of grid

    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)
    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)
    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)
    
    #creation of score labels
    
    xscoreLabel=tk.Label(win,text="X's Score:",font=("Times",16),bg="crimson")
    xscoreLabel.grid(row=3,column=0)
    x_scoreLabel=tk.Label(win,text=str(xscore),font=("Times",16),bg="lightcoral")
    x_scoreLabel.grid(row=3,column=1,sticky="ew")
    yscoreLabel=tk.Label(win,text="O's Score:",font=("Times",16),bg="lime")
    yscoreLabel.grid(row=4,column=0)
    y_scoreLabel=tk.Label(win,text=str(yscore),font=("Times",16),bg="greenyellow")
    y_scoreLabel.grid(row=4,column=1,sticky="ew")
    
    #creation of end game button
    
    bend=tk.Button(win,text="End Game",font=("BlackChancery",12),bg="thistle",command=lambda: end())
    bend.grid(row=4,column=2,sticky="ew")
    
    #creation of restart game button
    
    rst=tk.Button(win,text="Reset Game",font=("BlackChancery",12),bg="thistle",command=lambda: restart())
    rst.grid(row=3,column=2)
    
#definition of the restart game function

def restart():
    global xscore,yscore
    if xscore>yscore:
        messagebox.showinfo("Tic-Tac-Toe", "X wins the game!\nClick OK to continue to a new round.")
    elif yscore>xscore:
        messagebox.showinfo("Tic-Tac-Toe", "O wins the game!\nClick OK to continue to a new round.")
    elif xscore==yscore:
        messagebox.showinfo("Tic-Tac-Toe", "It's a Tie!\nClick OK to continue to a new round.")
    xscore=0
    yscore=0
    nextmatch()

nextmatch()

win.mainloop()
