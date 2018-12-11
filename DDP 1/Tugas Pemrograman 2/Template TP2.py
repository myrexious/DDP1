#!/usr/bin/env python3
"""Template Assignment #2."""
import turtle
import random
import math


def choose_file():
    """Prompts user to choose file to load via GUI-based modal window."""
    import tkinter
    from tkinter import filedialog

    root_window = tkinter.Tk()
    root_window.withdraw()

    return filedialog.askopenfilename()



def main():
    """Executes main program."""
    # The program starts by asking user to select a file to read
    selected_file = choose_file()

    # debug:
    print ("Selected file: {}".format (selected_file))
    # in your assignment, you should open this selected file and
    # read the drawing commands

    # Create the canvas where shapes will be draw onto
    canvas = turtle.Screen()

    # Create the pen object that will be used for drawing shapes
    pen = turtle.Turtle()

    width = 50
    height = 40
    
    #draw a squares
    pen.down()
    pen.forward(width)
    pen.right(90)
    pen.forward(height)
    pen.right(90)
    pen.forward(width)
    pen.right(90)
    pen.forward(height)
    pen.right(90)
    pen.up()


    canvas.exitonclick()


if __name__ == '__main__':
    main()
