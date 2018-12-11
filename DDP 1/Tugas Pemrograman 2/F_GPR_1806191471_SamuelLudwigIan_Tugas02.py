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


def main():
    """Opens the file"""
    selected_file = choose_file()
    print("Your selected file is : {}".format(selected_file))
    file = open(selected_file, "r")
    filelines = file.readlines()

    """Sets the title"""
    npm_nama = str(filelines[0])
    npm = npm_nama.split()
    npm = str(npm[-1])
    nama = npm_nama[:npm_nama.find(npm)]
    turtle.title(nama + " | " + npm)

    turtle.speed('fastest')
    
    """Calls the function to draw something"""
    for a in range(1,len(filelines)):
        """If there is an empty line"""
        try:
            readlines = filelines[a]
            readline = readlines.split()
        except:
            print("Your file has an error in line", a+1)
            continue
        

        turtle.bgcolor(colorize())

        """If there is no X and Y coordinate in input"""
        if len(readline) < 3:
            print("Your file has an error in line", a+1)
            continue
        
        call_funct = readline[0]
        
        try:
            x = int(readline[1])
            y = int(readline[2])
        except:
            print("Your file has an error in line", a+1)
            continue
        
        try:
            #Input:Color
            if call_funct == "color":
                if len(readline) != 4:
                    print("Your file has an error in line", a+1)
                    continue
                color(readline)
            
            #Input:Square
            elif call_funct == "square":
                if len(readline) != 4:
                    print("Your file has an error in line", a+1)
                    continue
                square(readline, x, y)
            
            #Input:Rectangle
            elif call_funct == "rectangle":
                if len(readline) != 5:
                    print("Your file has an error in line", a+1)
                    continue
                rectangle(readline, x, y)
            
            #Input:Circle
            elif call_funct == "circle":
                if len(readline) != 4:
                    print("Your file has an error in line", a+1)
                    continue
                circle(readline, x, y)
            
            #Input:Flower
            elif call_funct == "flower":
                if len(readline) != 4:
                    print("Your file has an error in line", a+1)
                    continue
                flower(readline, x, y)
            
            #Input:Checkerboard
            elif call_funct == "checkerboard":
                if len(readline) != 5:
                    print("Your file has an error in line", a+1)
                    continue
                checkerboard(readline, x, y)
            
            #Input:Polygon
            elif call_funct == "polygon":
                if len(readline) != 5:
                    print("Your file has an error in line", a+1)
                    continue
                polygon(readline, x, y)

            else:
                print("Your file has an error in line", a+1)
        
        except:
            print("Your file has an error in line", a+1)
            turtle.penup()
            continue    

        turtle.penup()
        turtle.bgcolor('white')
    turtle.exitonclick()

"""Random color"""
def colorize():
    turtle.colormode(255)
    r = int(random.randrange(0, 255))       #SetColorRed
    g = int(random.randrange(0, 255))       #SetColorGreen
    b = int(random.randrange(0, 255))       #SetColorBlue
    return r, g, b

"""Color Set"""
def color(line_to_read):
    r = int(line_to_read[1])
    g = int(line_to_read[2])
    b = int(line_to_read[3])
    turtle.color((r,g,b))

"""Square"""
def square(line_to_read, x_coordinate, y_coordinate):
    turtle.goto(x_coordinate, y_coordinate)
    turtle.pendown()
    for a in range(4):
        turtle.forward(int(line_to_read[3]))
        turtle.right(90)

"""Rectangle"""
def rectangle(line_to_read, x_coordinate, y_coordinate):
    turtle.goto(x_coordinate, y_coordinate)
    turtle.pendown()
    for a in range(2):
        turtle.forward(int(line_to_read[3]))
        turtle.right(90)
        turtle.forward(int(line_to_read[4]))
        turtle.right(90)

"""Circle"""
def circle(line_to_read, x_coordinate, y_coordinate):
    turtle.goto(x_coordinate, y_coordinate)
    turtle.pendown()
    turtle.circle(int(line_to_read[3]))

"""Flower"""
def flower(line_to_read, x_coordinate, y_coordinate):
    turtle.goto(x_coordinate, y_coordinate)
    turtle.pendown()
    petals = int(line_to_read[3])
    for x in range(petals):
        turtle.pencolor(colorize())
        turtle.circle(60,75)
        turtle.left(105)
        turtle.circle(60,75)
        turtle.left(105-(360/petals))

"""Checkerboard"""
def checkerboard(line_to_read, x_coordinate, y_coordinate):
    turtle.goto(x_coordinate, y_coordinate)
    turtle.pendown()
    rowNumber = int(line_to_read[3])
    squareSize = int(line_to_read[4])
    for a in range(rowNumber):              #DoesTheMovementToTheNextRow
        for b in range (rowNumber):         #DoesTheMovementToTheNextSquare
            turtle.color(colorize())
            turtle.begin_fill()
            for c in range(4):            #DoesTheMovementToDrawTheSquare
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

"""Polygon"""
def polygon(line_to_read, x_coordinate, y_coordinate):
    turtle.goto(x_coordinate, y_coordinate)
    turtle.pendown()
    side = int(line_to_read[3])
    for a in range(side):
        turtle.forward(int(line_to_read[4]))
        turtle.right(360/side)

"""Checks"""
def check(line_to_read):
    for x in range(len(line_to_read)):
        try:
            x = int(line_to_read[x])
        except:
            return False

if __name__ == '__main__':
    main()