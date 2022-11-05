import os
import fnmatch
from tkinter import *

def search():

   global name
   global fpath
   global send

   cri = name.get()
   path = fpath.get()
   result = []
   count = 0
   index = 0
   y = 225
   
   for root, dirs, files in os.walk(path):
      for cri in files:
         if fnmatch.fnmatch(cri, cri):
               result.append(os.path.join(root, cri))
               count += 1
         if count == 15:
            break
      if count == 15:
         break

   for x in result:
      res = Label(canvas, text = result[index], bg = "white")
      canvas.create_window(30, y, window = res, anchor = "w")
      y += 25
      index += 1
      if index == 15:
         break

   if len(result) != 0:

      but1 = Button(canvas, padx = 30, pady = 2, text = "Open", command = lambda: click(0))
      but2 = Button(canvas, padx = 30, pady = 2, text = "Open", command = lambda: click(1))
      but3 = Button(canvas, padx = 30, pady = 2, text = "Open", command = lambda: click(2))
      but4 = Button(canvas, padx = 30, pady = 2, text = "Open", command = lambda: click(3))
      but5 = Button(canvas, padx = 30, pady = 2, text = "Open", command = lambda: click(4))
      but6 = Button(canvas, padx = 30, pady = 2, text = "Open", command = lambda: click(5))
      but7 = Button(canvas, padx = 30, pady = 2, text = "Open", command = lambda: click(6))
      but8 = Button(canvas, padx = 30, pady = 2, text = "Open", command = lambda: click(7))
      but9 = Button(canvas, padx = 30, pady = 2, text = "Open", command = lambda: click(8))
      but10 = Button(canvas, padx = 30, pady = 2, text = "Open", command = lambda: click(9))
      but11 = Button(canvas, padx = 30, pady = 2, text = "Open", command = lambda: click(10))
      but12 = Button(canvas, padx = 30, pady = 2, text = "Open", command = lambda: click(11))
      but13 = Button(canvas, padx = 30, pady = 2, text = "Open", command = lambda: click(12))
      but14 = Button(canvas, padx = 30, pady = 2, text = "Open", command = lambda: click(13))
      but15 = Button(canvas, padx = 30, pady = 2, text = "Open", command = lambda: click(14))
      
      canvas.create_window(1010, 215, anchor = NW, window = but1)   
      canvas.create_window(1010, 240, anchor = NW, window = but2)  
      canvas.create_window(1010, 265, anchor = NW, window = but3)  
      canvas.create_window(1010, 290, anchor = NW, window = but4)  
      canvas.create_window(1010, 315, anchor = NW, window = but5)  
      canvas.create_window(1010, 340, anchor = NW, window = but6)  
      canvas.create_window(1010, 365, anchor = NW, window = but7)  
      canvas.create_window(1010, 390, anchor = NW, window = but8)  
      canvas.create_window(1010, 415, anchor = NW, window = but9)  
      canvas.create_window(1010, 440, anchor = NW, window = but10)  
      canvas.create_window(1010, 465, anchor = NW, window = but11)  
      canvas.create_window(1010, 490, anchor = NW, window = but12)  
      canvas.create_window(1010, 515, anchor = NW, window = but13)  
      canvas.create_window(1010, 540, anchor = NW, window = but14)  
      canvas.create_window(1010, 565, anchor = NW, window = but15)  

      resbut.config(state = NORMAL)
      send = result

def click(ind):
   
   test = list(send[ind])
   test.insert(2, "\\")
   test.reverse()
   rem = len(test) - test.index('\\', 0, len(test)) - 1
   test.reverse()
   str1 = ''.join(test[:rem])
   command = 'explorer.exe ' + str1
   os.system(command)

def reset():

   canvas.delete("all")
   name = Entry(canvas, width = 100) 
   canvas.create_window(500, 50, window = name)
   nlab = Label(canvas, text = "Enter the name of the file", bg = "gray")
   canvas.create_window(100, 50, window = nlab)

   fpath = Entry(canvas, width = 100) 
   canvas.create_window(500, 75, window = fpath)
   flab = Label(canvas, text = "Enter the directory to search", bg = "gray")
   canvas.create_window(108, 75, window = flab)

   searchbut = Button(canvas, padx = 20, text = "Search", command = lambda: search())
   canvas.create_window(240, 125, window = searchbut)

   resbut = Button(canvas, padx = 20, text = "Reset", state = DISABLED, command = lambda: reset())
   canvas.create_window(350, 125, window = resbut)

   olab = Label(canvas, text = "Output", bg = "gray", anchor = "w")
   canvas.create_window(50, 180, window = olab)

   canvas.create_rectangle(25, 200, 1000, 600, fill = "white")

win = Tk()
win.title("File Search Utility")

win.geometry("1920x1080")

canvas = Canvas(win, width = 1920, height = 1080, bg = "gray")
canvas.grid()

name = Entry(canvas, width = 100) 
canvas.create_window(500, 50, window = name)
nlab = Label(canvas, text = "Enter the name of the file", bg = "gray")
canvas.create_window(100, 50, window = nlab)

fpath = Entry(canvas, width = 100) 
canvas.create_window(500, 75, window = fpath)
flab = Label(canvas, text = "Enter the directory to search", bg = "gray")
canvas.create_window(108, 75, window = flab)

searchbut = Button(canvas, padx = 20, text = "Search", command = lambda: search())
canvas.create_window(240, 125, window = searchbut)

resbut = Button(canvas, padx = 20, text = "Reset", state = DISABLED, command = lambda: reset())
canvas.create_window(350, 125, window = resbut)

olab = Label(canvas, text = "Output", bg = "gray", anchor = "w")
canvas.create_window(50, 180, window = olab)

canvas.create_rectangle(25, 200, 1000, 600, fill = "white")

win.mainloop()