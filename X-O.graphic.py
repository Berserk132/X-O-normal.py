from tkinter import*
from tkinter import ttk
from tkinter import messagebox

player=1
p1=[]
p2=[]


root=Tk()
root.title("Tic Tac Toe:player 1")

#Add Buttons

button1=ttk.Button(root,text=" ")
button1.grid(row=0,column=0,sticky='snew',ipadx=20,ipady=20)
button1.config(command=lambda: ButtonClick(1))

button2=ttk.Button(root,text=" ")
button2.grid(row=0,column=1,sticky='snew',ipadx=20,ipady=20)
button2.config(command=lambda: ButtonClick(2))

button3=ttk.Button(root,text=" ")
button3.grid(row=0,column=2,sticky='snew',ipadx=20,ipady=20)
button3.config(command=lambda: ButtonClick(3))

button4=ttk.Button(root,text=" ")
button4.grid(row=1,column=0,sticky='snew',ipadx=20,ipady=20)
button4.config(command=lambda: ButtonClick(4))

button5=ttk.Button(root,text=" ")
button5.grid(row=1,column=1,sticky='snew',ipadx=20,ipady=20)
button5.config(command=lambda: ButtonClick(5))

button6=ttk.Button(root,text=" ")
button6.grid(row=1,column=2,sticky='snew',ipadx=20,ipady=20)
button6.config(command=lambda: ButtonClick(6))

button7=ttk.Button(root,text=" ")
button7.grid(row=2,column=0,sticky='snew',ipadx=20,ipady=20)
button7.config(command=lambda: ButtonClick(7))

button8=ttk.Button(root,text=" ")
button8.grid(row=2,column=1,sticky='snew',ipadx=20,ipady=20)
button8.config(command=lambda: ButtonClick(8))

button9=ttk.Button(root,text=" ")
button9.grid(row=2,column=2,sticky='snew',ipadx=20,ipady=20)
button9.config(command=lambda: ButtonClick(9))



def ButtonClick(id):
    global player
    global p1
    global p2
    if player==1:
        setlayout(id,'X')
        p1.append(id)
        root.title("Tic Tac Toe:player 2")
        player=2
        print("p1:{}".format(p1))
    elif player==2:
        setlayout(id,'O')
        p2.append(id)
        root.title("Tic Tac Toe:player 1")
        player=1
        print("p2:{}".format(p2))

    check_winner()


    
def setlayout(id,playersymbol):
    if id==1:
        button1.config(text=playersymbol)
        button1.state(['disabled'])
        
    elif id==2:
        button2.config(text=playersymbol)
        button2.state(['disabled'])
        
    elif id==3:
        button3.config(text=playersymbol)
        button3.state(['disabled'])
        
    elif id==4:
        button4.config(text=playersymbol)
        button4.state(['disabled'])
    elif id==5:
        
        button5.config(text=playersymbol)
        button5.state(['disabled'])
        
    elif id==6:
        button6.config(text=playersymbol)
        button6.state(['disabled'])
        
    elif id==7:
        button7.config(text=playersymbol)
        button7.state(['disabled'])
        
    elif id==8:
        button8.config(text=playersymbol)
        button8.state(['disabled'])
        
    elif id==9:
        button9.config(text=playersymbol)
        button9.state(['disabled'])

def check_winner():
    winner=0
    if ((1 in p1) and (2 in p1) and (3 in p1)):
        winner=1
    if ((1 in p2) and (2 in p2) and (3 in p2)):
        winner=2
        
    if ((4 in p1) and (5 in p1) and (6 in p1)):
        winner=1
    if ((4 in p2) and (5 in p2) and (6 in p2)):
        winner=2
        
    if ((7 in p1) and (8 in p1) and (9 in p1)):
        winner=1
    if ((7 in p2) and (8 in p2) and (9 in p2)):
        winner=2
        
    if ((1 in p1) and (4 in p1) and (7 in p1)):
        winner=1
    if ((1 in p2) and (4 in p2) and (7 in p2)):
        winner=2
        
    if ((1 in p1) and (5 in p1) and (9 in p1)):
        winner=1
    if ((1 in p2) and (5 in p2) and (9 in p2)):
        winner=2
        
    if ((3 in p1) and (5 in p1) and (7 in p1)):
        winner=1
    if ((3 in p2) and (5 in p2) and (7 in p2)):
        winner=2
        
    if ((3 in p1) and (6 in p1) and (9 in p1)):
        winner=1
    if ((3 in p2) and (6 in p2)  and (9 in p2)):
        winner=2
        
    if ((2 in p1) and (5 in p1) and (8 in p1)):
        winner=1
    if ((2 in p2) and (5 in p2)  and (8 in p2)):
        winner=2

    if winner==1:
        messagebox.showinfo(title="Congratulation",message="Player 1 is the winner")
    elif winner==2:
        messagebox.showinfo(title="Congratulation",message="Player 2 is the winner")
        


        
    
root.mainloop()











    
