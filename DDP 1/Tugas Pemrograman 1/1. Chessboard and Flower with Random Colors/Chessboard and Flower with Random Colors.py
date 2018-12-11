import turtle, random

#input the number of rows, size of the squares, and number of petals
rowNumber = int(turtle.numinput("Colorful Chessboard and Flower", "Enter the number of rows : ",
                            default=2, minval=2, maxval=15))    #InputTheNumberOfRows
squareSize = int(turtle.numinput("Colorful Chessboard and Flower", "Enter the square size: ",
                             default=5, minval=5, maxval=50))   #InputTheSquareSize
petals = int(turtle.numinput("Colorful Chessboard and Flower", "Enter the number of petals of the flower : ",
                         default=3, minval=1, maxval=100))      #InputTheNumberOfPetals
normalizer = int((squareSize*rowNumber)/2)  #ForHelpingTurtlePlacement


#speed and preparation so everything's centered
turtle.hideturtle()                 #HideTheTurtleSoItLooksGood
turtle.speed('fastest')
turtle.penup()
turtle.left(90)                     #MovesTheTurtleUp
turtle.forward(normalizer)          #UsesModulusSoThePxIsStraight
turtle.left(90)                     #MovesTheTurtleLeft
turtle.forward(normalizer)
turtle.left(180)
turtle.pendown()
turtle.colormode(255)


#Colorful chessboard
for a in range(0,rowNumber):                #DoesTheMovementToTheNextRow
    for b in range (0,rowNumber):           #DoesTheMovementToTheNextSquare
        randomColor1 = int(random.randrange(0, 255))    #SetColorCode1
        randomColor2 = int(random.randrange(0, 255))    #SetColorCode2
        randomColor3 = int(random.randrange(0, 255))    #SetColorCode3
        turtle.begin_fill()
        turtle.pencolor((randomColor1,randomColor2,randomColor3))
        turtle.fillcolor((randomColor1,randomColor2,randomColor3))
        for c in range(0,4):                #DoesTheMovementToDrawTheSquare
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

#movement to the petal so it's centered above the box
turtle.penup()
turtle.left(90)
turtle.forward(squareSize*rowNumber)
turtle.right(90)
turtle.forward(normalizer)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.pendown()

#Flower
for d in range(0, petals):
    turtle.pensize(2)
    randomColorF1 = int(random.randrange(0, 255))    #SetColorCodeforFlower1
    randomColorF2 = int(random.randrange(0, 255))    #SetColorCodeforFlower2
    randomColorF3 = int(random.randrange(0, 255))    #SetColorCodeforFlower3
    turtle.pencolor((randomColorF1,randomColorF2,randomColorF3))
    turtle.circle(60,60)
    turtle.left(120)
    turtle.circle(60,60)
    turtle.left(120-(360/petals))

#Text
turtle.penup()
turtle.right(90)
turtle.forward(200+ 2*normalizer)
turtle.left(180)
turtle.pencolor("blue")
turtle.write(("Colorful Chessboard of " + str(rowNumber**2) +
              " Squares and Flower of " + str(petals) + " Petals"),
             move=False, align="Center", font=("Arial", 16, "normal"))

#exit on click
print("press click to exit")
turtle.exitonclick()
