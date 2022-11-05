from tkinter import *
import random

grid = [0, 1, 2, 3, 4, 5, 6, 7, 8]
left = [0, 1, 2, 3, 4, 5, 6, 7, 8]
xpla = ""
opla = ""
img = ""
turn = 0
game = True

pchoice = random.choice(range(1,3))

if pchoice == 2:
    xpla = "Computer"
    opla = "Player"
else:
    xpla = "Player"
    opla = "Computer"

def start():

    global pchoice

    butn.config(state = DISABLED)
    canvas.create_line(175, 50, 175, 450, fill = "black", width = 5)
    canvas.create_line(325, 50, 325, 450, fill = "black", width = 5)
    canvas.create_line(50, 175, 450, 175, fill = "black", width = 5)
    canvas.create_line(50, 325, 450, 325, fill = "black", width = 5)

    but1win = canvas.create_window(75, 75, anchor = NW, window = but1)
    but2win = canvas.create_window(210, 75, anchor = NW, window = but2)
    but3win = canvas.create_window(350, 75, anchor = NW, window = but3)
    but4win = canvas.create_window(75, 210, anchor = NW, window = but4)
    but5win = canvas.create_window(210, 210, anchor = NW, window = but5)
    but6win = canvas.create_window(350, 210, anchor = NW, window = but6)
    but7win = canvas.create_window(75, 350, anchor = NW, window = but7)
    but8win = canvas.create_window(210, 350, anchor = NW, window = but8)
    but9win = canvas.create_window(350, 350, anchor = NW, window = but9)

    if pchoice == 2:
        click(random.choice(left))
        pick = Label(win, text = "You play with the O's").grid(row = 1)
    else:
        pick = Label(win, text = "You play with the X's").grid(row = 1)

def reset():
    
    global grid 
    global left
    global turn
    global xpla
    global opla
    global game
    global pchoice

    pick = Label(win, text = "                                                   ").grid(row = 1)
    mes = Label(win, text = "                                                   ").grid(row = 2)

    but1.config(image = "", state = NORMAL)
    but2.config(image = "", state = NORMAL)
    but3.config(image = "", state = NORMAL)
    but4.config(image = "", state = NORMAL)
    but5.config(image = "", state = NORMAL)
    but6.config(image = "", state = NORMAL)
    but7.config(image = "", state = NORMAL)
    but8.config(image = "", state = NORMAL)
    but9.config(image = "", state = NORMAL)
    butr.config(state = DISABLED)

    grid = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    left = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    turn = 0
    game = True

    pchoice = random.choice(range(1,3))

    if pchoice == 2:
        xpla = "Computer"
        opla = "Player"
        click(random.choice(left))
        pick = Label(win, text = "You play with the O's").grid(row = 1)
    else:
        xpla = "Player"
        opla = "Computer"
        pick = Label(win, text = "You play with the X's").grid(row = 1)

def wincheck():
    
    global game
    #horizontal lines
    if grid[0] == grid[1] == grid[2]:
        if grid[0] == "x":
            mes = Label(win, text = xpla + " wins with the X's").grid(row = 2)
        if grid[0] == "o":
            mes = Label(win, text = opla + " wins with the O's").grid(row = 2)
        butr.config(state = NORMAL)
        game = False

    elif grid[3] == grid[4] == grid[5]:
        if grid[3] == "x":
            mes = Label(win, text = xpla + " wins with the X's").grid(row = 2)
        if grid[3] == "o":
            mes = Label(win, text = opla + " wins with the O's").grid(row = 2)
        butr.config(state = NORMAL)
        game = False

    elif grid[6] == grid[7] == grid[8]:
        if grid[6] == "x":
            mes = Label(win, text = xpla + " wins with the X's").grid(row = 2)
        if grid[6] == "o":
            mes = Label(win, text = opla + " wins with the O's").grid(row = 2)
        butr.config(state = NORMAL)
        game = False

    #vertical lines
    elif grid[0] == grid[3] == grid[6]:
        if grid[0] == "x":
            mes = Label(win, text = xpla + " wins with the X's").grid(row = 2)
        if grid[0] == "o":
            mes = Label(win, text = opla + " wins with the O's").grid(row = 2)
        butr.config(state = NORMAL)
        game = False
        
    elif grid[1] == grid[4] == grid[7]:
        if grid[1] == "x":
            mes = Label(win, text = xpla + " wins with the X's").grid(row = 2)
        if grid[1] == "o":
            mes = Label(win, text = opla + " wins with the O's").grid(row = 2)
        butr.config(state = NORMAL)
        game = False
        
    elif grid[2] == grid[5] == grid[8]:
        if grid[2] == "x":
            mes = Label(win, text = xpla + " wins with the X's").grid(row = 2)
        if grid[2] == "o":
            mes = Label(win, text = opla + " wins with the O's").grid(row = 2)
        butr.config(state = NORMAL)
        game = False
        
    #diagonal lines
    elif grid[0] == grid[4] == grid[8]:
        if grid[0] == "x":
            mes = Label(win, text = xpla + " wins with the X's").grid(row = 2)
        if grid[0] == "o":
            mes = Label(win, text = opla + " wins with the O's").grid(row = 2)
        butr.config(state = NORMAL)
        game = False
        
    elif grid[2] == grid[4] == grid[6]:
        if grid[2] == "x":
            mes = Label(win, text = xpla + " wins with the X's").grid(row = 2)
        if grid[2] == "o":
            mes = Label(win, text = opla + " wins with the O's").grid(row = 2) 
        butr.config(state = NORMAL)
        game = False
        
    elif turn == 9:
        mes = Label(win, text = "Draw").grid(row = 2)
        butr.config(state = NORMAL)
        game = False
        
def choice(num):
    
    global turn
    global pchoice
    
    left.remove(num)

    if turn % 2 == 0:
        img = x
        grid[num] = "x"
    else:
        img = o  
        grid[num] = "o"
        
    if num == 0:
        but1.config(image = img, state = DISABLED)
    elif num == 1:
        but2.config(image = img, state = DISABLED)
    elif num == 2:
        but3.config(image = img, state = DISABLED)
    elif num == 3:
        but4.config(image = img, state = DISABLED)
    elif num == 4:
        but5.config(image = img, state = DISABLED)
    elif num == 5:
        but6.config(image = img, state = DISABLED)
    elif num == 6:
        but7.config(image = img, state = DISABLED)
    elif num == 7:
        but8.config(image = img, state = DISABLED)
    else:
        but9.config(image = img, state = DISABLED)

    turn += 1
        
    wincheck()

def click(val):
     
    global xpla
    global pchoice

    if pchoice == 2:
        choice(val)
        pchoice = 0
    elif pchoice != 2 and game:
        choice(val)
        if game:
            choice(random.choice(left))
    
win = Tk()
win.title("Tic Tac Toe")

win.geometry("500x600")

canvas = Canvas(win, height=500, width=500)
canvas.grid()

#the images are 512x512
x = PhotoImage(file = r"x.png").subsample(7, 7)
o = PhotoImage(file = r"o.png").subsample(7, 7)

butn = Button(canvas, padx = 10, pady = 5, text = "New game", command = lambda: start())
butnwin = canvas.create_window(25, 10, anchor = NW, window = butn)
butr = Button(canvas, padx = 10, pady = 5, text = "Reset board", state = DISABLED, command = lambda: reset())
butrwin = canvas.create_window(125, 10, anchor = NW, window = butr)

but1 = Button(canvas, padx = 30, pady = 27, highlightthickness = 1, bd = 1, command = lambda: click(0))
but2 = Button(canvas, padx = 30, pady = 27, highlightthickness = 1, bd = 1, command = lambda: click(1))
but3 = Button(canvas, padx = 30, pady = 27, highlightthickness = 1, bd = 1, command = lambda: click(2))
but4 = Button(canvas, padx = 30, pady = 27, highlightthickness = 1, bd = 1, command = lambda: click(3))
but5 = Button(canvas, padx = 30, pady = 27, highlightthickness = 1, bd = 1, command = lambda: click(4))
but6 = Button(canvas, padx = 30, pady = 27, highlightthickness = 1, bd = 1, command = lambda: click(5))
but7 = Button(canvas, padx = 30, pady = 27, highlightthickness = 1, bd = 1, command = lambda: click(6))
but8 = Button(canvas, padx = 30, pady = 27, highlightthickness = 1, bd = 1, command = lambda: click(7))
but9 = Button(canvas, padx = 30, pady = 27, highlightthickness = 1, bd = 1, command = lambda: click(8))

win.mainloop()
