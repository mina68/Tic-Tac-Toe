# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 12:30:59 2019

@author: Mina
"""

from tkinter import *
from tkinter import messagebox
from functools import partial
from socket import *
from _thread import *

s = socket((AF_INET), SOCK_STREAM)
host = "127.0.0.1"
port = 7772
s.bind((host, port))
s.listen(50)
c, ad = s.accept()

window = Tk()
window.title("tic tac toe")
window.geometry("300x300")

player_simbol = 'O'
opponent_simbol = 'X'
lbl1 = Label(window, text="You play " + player_simbol)
lbl1.grid(row=1, column=0)

my_turn = 0
def clicked(btn, i, j):
    global my_turn
    global player_simbol
    global c
    if (btn["text"]==" " and my_turn==1) :
        btn["text"]=player_simbol
        button_number = i*3+j
        c.send(str(button_number).encode('utf-8'))
        my_turn=0
        check(btn)

iteration=1
def check(btn):
    global iteration
    global btns
    global player_simbol
    win = 0
    for i in range(3):
        if((btns[i][0]["text"]==btns[i][1]["text"] and btns[i][0]["text"]==btns[i][2]["text"] and btns[i][0]["text"]!=" ") 
        or (btns[0][i]["text"]==btns[1][i]["text"] and btns[0][i]["text"]==btns[2][i]["text"] and btns[0][i]["text"]!=" ")):
            if(btn["text"] == player_simbol):
                messagebox.showinfo("Congratulations! " + player_simbol, "Congratulations you won!")
            else:
                messagebox.showinfo("Game over " + player_simbol, "You lost! better luck next time")
            win = 1
            reset()
            
    if win==0:     
        if((btns[0][0]["text"]==btns[1][1]["text"] and btns[0][0]["text"]==btns[2][2]["text"] and btns[0][0]["text"]!=" ") 
        or (btns[0][2]["text"]==btns[1][1]["text"] and btns[0][2]["text"]==btns[2][0]["text"] and btns[0][2]["text"]!=" ")):
            if(btn["text"] == player_simbol):
                messagebox.showinfo("Congratulations! " + player_simbol, "Congratulations you won!")
            else:
                messagebox.showinfo("Game over " + player_simbol, "You lost! better luck next time")
            win==1
            reset()
        
    if win==0 and iteration==9:
        messagebox.showinfo("game over ", "no player won")
        reset()
        
    iteration = iteration+1
    
    
def reset():
    global iteration
    global my_turn
    global btns
    for i in range(3):
        for j in range(3):
            btns[i][j].config(text=" ")
    my_turn = 0
    iteration = 0
    
            
    

btns = [[0 for x in range(3)] for y in range(3)] 
for i in range(3):
    for j in range(3):
        btns[i][j] = Button(window,text=" ",bg="yellow",fg="black",width=8,height=4)
        btns[i][j].config(command=partial(clicked, btns[i][j], i, j))
        btns[i][j].grid(row=i+10, column=j+3)
        
""" =========================================================================================================================="""

def recvThread (c):
    global btns
    global my_turn
    while True:
        button_number = int(c.recv(1024).decode('utf-8'))
        row = int(button_number/3)
        column = int(button_number%3)
        btns[row][column]["text"]=opponent_simbol
        my_turn=1
        check(btns[row][column])
        
    
start_new_thread(recvThread, (c,))
    
window.mainloop()















