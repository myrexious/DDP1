import turtle
import random
import math

"""Prompts user to choose file to load via GUI-based modal window."""
def choose_file(): 
    import tkinter
    from tkinter import filedialog
    root_window = tkinter.Tk()
    root_window.withdraw()
    return filedialog.askopenfilename()

def colorize():
    turtle.colormode(255)
    r = int(random.randrange(0, 255))       #SetColorRed
    g = int(random.randrange(0, 255))       #SetColorGreen
    b = int(random.randrange(0, 255))       #SetColorBlue
    return r, g, b

"""File Terpilih"""
selected_file = choose_file()
print("Your selected file is : {}".format(selected_file))
file = open(selected_file, "r")
filelines = file.readlines()

"""Mengatur Title"""
npm_nama = str(filelines[0])
npm = npm_nama.split()
npm = str(npm[-1])
nama = npm_nama[:npm_nama.find(npm)]
turtle.title(nama + " | " + npm)


turtle.colormode(255)
turtle.speed("fastest")


"""Main Functions"""
for a in range(len(filelines)-1):
    readline = filelines[a+1]
    readline = readline.split()
    turtle.pendown
    turtle.colormode(255)
    call_funct = readline[0]
    turtle.bgcolor(colorize())
    
    
    if len(readline)<3:
        print("Your input file has a wrong input in line", (a+1))
        continue


    try:
        x = int(readline[1])
        y = int(readline[2])
    except ValueError:
        print("Your input file has a wrong input in line", (a+1))
        continue

    
    if call_funct == "color":
        if len(readline)!=4:
            print("Your input file has a wrong input in line", (a+1))
            continue
        r = int(readline[1])
        g = int(readline[2])
        b = int(readline[3])
        turtle.color((r, g, b))
        
    elif call_funct == "square":
        if len(readline)!=4:
            print("Your input file has a wrong input in line", (a+1))
            continue
        turtle.goto(x,y)
        turtle.pendown()
        for i in range(4):
            turtle.forward(int(readline[3]))
            turtle.right(90)
            
    elif call_funct == "rectangle":
        if len(readline)!=5:
            print("Your input file has a wrong input in line", (a+1))
            continue
        turtle.goto(x,y)
        turtle.pendown()
        for j in range(2):
            turtle.forward(int(readline[3]))
            turtle.right(90)
            turtle.forward(int(readline[4]))
            turtle.right(90)
            
    elif call_funct == "circle":
        if len(readline)!=4:
            print("Your input file has a wrong input in line", (a+1))
            continue
        turtle.goto(x,y)
        turtle.pendown()
        turtle.circle(int(readline[3]))

    
    elif call_funct == "flower":
        if len(readline)!=4:
            print("Your input file has a wrong input in line", (a+1))
            continue
        turtle.goto(x,y)
        turtle.pendown()
        petals = int(readline[3])
        for d in range(0, petals):
            turtle.pencolor(colorize())
            turtle.circle(60,75)
            turtle.left(105)
            turtle.circle(60,75)
            turtle.left(105-(360/petals))

    #Checkerboard
    elif call_funct == "checkerboard":
        if len(readline)!=5:
            print("Your input file has a wrong input in line", (a+1))
            continue
        turtle.goto(x,y)
        turtle.pendown()
        rowNumber = int(readline[3])
        squareSize = int(readline[4])
        for a in range(rowNumber):              #DoesTheMovementToTheNextRow
            for b in range (rowNumber):         #DoesTheMovementToTheNextSquare
                turtle.color(colorize())
                turtle.begin_fill()
                for c in range(0,4):            #DoesTheMovementToDrawTheSquare
                    turtle.forward(squareSize)
                    turtle.right(90)
                turtle.forward(squareSize)
                turtle.end_fill()
            turtle.penup()
            turtle.right(90)
            turtle.forward(squareSize)
            turtle.right(90)
            turtle.forward(squareSize*rowNumber)
            turtle.right(180)
            turtle.pendown()

    #Polygon
    elif call_funct == "polygon":
        if len(readline)!=5:
            print("Your input file has a wrong input in line", (a+1))
            continue
        turtle.goto(x,y)
        turtle.pendown()
        side = int(readline[3])
        for n in range(side):
            turtle.forward(int(readline[4]))
            turtle.right(360/side)
            
    #Wrong Input        
    else:
        print("Your input file has a wrong input in line", (a+1))
    turtle.penup()
    turtle.bgcolor('white')
