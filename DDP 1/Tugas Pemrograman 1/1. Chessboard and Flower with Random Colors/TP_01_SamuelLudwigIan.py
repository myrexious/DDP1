import turtle, random

#sets the window
turtle.screensize(canvwidth=1000, canvheight=1000)

#input the number of rows, size of the squares, and number of petals
rowNumber = int(turtle.numinput("Colorful Chessboard and Flower", "Enter the number of rows : ",
                            default=3, minval=3, maxval=10))                                        #Input The Number Of Rows
squareSize = int(turtle.numinput("Colorful Chessboard and Flower", "Enter the square size: ",
                             default=5, minval=5, maxval=int(500/rowNumber)))                       #InputThe Square Size
petals = int(turtle.numinput("Colorful Chessboard and Flower", "Enter the number of petals of the flower : ",
                         default=3, minval=1, maxval=360))                                          #InputThe Number Of Petals
normalizer = int((squareSize*rowNumber)/2)                                                          #For Helping Turtle Placement

turtle.title("Colorful Chessboard and Flower")      #Sets The Title Of The Program

#speed and preparation so everything's centered
turtle.hideturtle()                                 #Hide The Turtle So It Looks Good
turtle.speed('fastest')
turtle.penup()
turtle.goto(-normalizer,normalizer)
turtle.pendown()

#define the function for the random color
turtle.colormode(255)                       
def colorize():
    r = int(random.randrange(0, 255))       #SetColorRed
    g = int(random.randrange(0, 255))       #SetColorGreen
    b = int(random.randrange(0, 255))       #SetColorBlue
    return r, g, b

#Colorful chessboard
for a in range(0,rowNumber):                            #DoesTheMovementToTheNextRow
    for b in range (0,rowNumber):                       #DoesTheMovementToTheNextSquare
        turtle.color(colorize())
        turtle.begin_fill()        
        for c in range(0,4):                            #DoesTheMovementToDrawTheSquare
            turtle.forward(squareSize)
            turtle.right(90)
            turtle.bgcolor(colorize())
        turtle.forward(squareSize)
        turtle.end_fill()
    turtle.penup()
    turtle.right(90)
    turtle.forward(squareSize)
    turtle.right(90)
    turtle.forward(squareSize*rowNumber)
    turtle.right(180)
    turtle.pendown()
    turtle.bgcolor('white')

#movement to the petal so it's centered above the box
turtle.penup()
turtle.goto(0,(100+int(squareSize*rowNumber/2)))
turtle.pendown()


#Flower
for d in range(0, petals):
    turtle.pencolor(colorize())
    turtle.circle(60,75)
    turtle.left(105)
    turtle.circle(60,75)
    turtle.left(105-(360/petals))
    turtle.bgcolor(colorize())
turtle.bgcolor('white')


#Text
turtle.penup()
turtle.goto(0,(-(normalizer)-75))                                           #Moves The Turtle To Position
turtle.pencolor("blue")
turtle.write(("Colorful Chessboard of " + str(rowNumber**2) +               #The Text
              " Squares and Flower of " + str(petals) + " Petals"),
             move=False, align="Center", font=("Arial", 16, "normal"))

#exit on click
print("press click to exit")
turtle.exitonclick()
