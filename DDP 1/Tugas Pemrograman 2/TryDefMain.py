import turtle
import random
import math

"""Prompts user to open file via GUI"""
def choose_file(): 
    import tkinter
    from tkinter import filedialog
    root_window = tkinter.Tk()
    root_window.withdraw()
    return filedialog.askopenfilename()

"""Functions"""
def colorize():                             #function to set color in checkerboard
    turtle.colormode(255)
    r = int(random.randrange(0, 255))       #SetColorRed
    g = int(random.randrange(0, 255))       #SetColorGreen
    b = int(random.randrange(0, 255))       #SetColorBlue
    return r, g, b

def color(line_to_read):                                #function to set color
    r = int(line_to_read[1])
    g = int(line_to_read[2])
    b = int(line_to_read[3])
    turtle.color((r, g, b))

def square(line_to_read,x,y):                               #function to make a square
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(4):
        turtle.forward(int(line_to_read[3]))
        turtle.right(90)

def rectangle(line_to_read,x,y):                            #function to make a rectangle
    turtle.goto(x,y)
    turtle.pendown()
    for j in range(2):
        turtle.forward(int(line_to_read[3]))
        turtle.right(90)
        turtle.forward(int(line_to_read[4]))
        turtle.right(90)

def circle(line_to_read,x,y):                               #function to make a circle
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(int(line_to_read[3]))

def flower(line_to_read,x,y):                               #function to make a flower
    turtle.goto(x,y)
    turtle.pendown()
    petals = int(line_to_read[3])
    for d in range(0, petals):
        turtle.pencolor(colorize())     #random color
        turtle.circle(60,75)
        turtle.left(105)
        turtle.circle(60,75)
        turtle.left(105-(360/petals))

def checkerboard(line_to_read,x,y):                         #function to make checkerboard
    turtle.goto(x,y)
    turtle.pendown()
    rowNumber = int(line_to_read[3])
    squareSize = int(line_to_read[4])
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

def polygon(line_to_read,x,y):                              #function to make a polygon
    turtle.goto(x,y)
    turtle.pendown()
    side = int(line_to_read[3])
    for n in range(side):
        turtle.forward(int(line_to_read[4]))
        turtle.right(360/side)

def checker(check):
    for l in range(1,len(check)):
        try:
            z = int(check[l])
        except:
            return False


"""Main Functions"""
def main():
    """Splits the selected file to a series of lists"""
    selected_file = choose_file()
    print("Your selected file is : {}".format(selected_file))
    file = open(selected_file, "r")
    filelines = file.readlines()


    """Set the title"""
    npm_nama = str(filelines[0])
    npm = npm_nama.split()
    npm = str(npm[-1])
    nama = npm_nama[:npm_nama.find(npm)]
    turtle.title(nama + " | " + npm)
    turtle.screensize(canvwidth=1000, canvheight=1000)
    turtle.hideturtle()


    turtle.colormode(255)
    turtle.speed("fastest")
    for a in range(1, len(filelines)):
        try:
            readline = filelines[a]
            readline = readline.split()
            turtle.colormode(255)
            turtle.bgcolor(colorize())          #colors the background if the program is still running

            call_funct = readline[0]

            x = int(readline[1])
            y = int(readline[2])
            if x>=1000 or y>=1000:
                print("Your input file has a wrong input in line", (a))
                continue


            #setcolor
            if call_funct == "color":
                if len(readline)!=4:
                    print("Your input file has a wrong input in line", (a))
                    continue
                else:
                    color(readline)

            #square
            elif call_funct == "square":
                if len(readline)!=4:
                    print("Your input file has a wrong input in line", (a))
                    continue
                else:
                    square(readline,x,y)

            #rectangle
            elif call_funct == "rectangle":
                if len(readline)!=5:
                    print("Your input file has a wrong input in line", (a))
                    continue
                else:
                    rectangle(readline,x,y)

            #circle
            elif call_funct == "circle":
                if len(readline)!=4:
                    print("Your input file has a wrong input in line", (a))
                    continue
                else:
                    circle(readline,x,y)

            #flower
            elif call_funct == "flower":
                if len(readline)!=4:
                    print("Your input file has a wrong input in line", (a))
                    continue
                else:
                    flower(readline,x,y)

            #Checkerboard
            elif call_funct == "checkerboard":
                if len(readline)!=5:
                    print("Your input file has a wrong input in line", (a))
                    continue
                else:
                    checkerboard(readline,x,y)

            #Polygon
            elif call_funct == "polygon":
                if len(readline)!=5:
                    print("Your input file has a wrong input in line", (a))
                    continue
                else:
                    polygon(readline,x,y)
                    
            #Wrong Input        
            else:
                print("Your input file has a wrong input in line", (a))
            
        except:
            print("Your input file has a wrong input in line", (a))
            turtle.penup()

        turtle.penup()
        turtle.bgcolor('white')

if __name__ == '__main__':
    main()

turtle.exitonclick()
