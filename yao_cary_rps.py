# This file was created by Cary Yao on 9/21/23

# import package
import turtle
from turtle import *
# The os module allows us to access the current directory in order to access assets
import os
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')

# computer generated random choice
from random import randint
choices = ["rock","paper","scissors"]
# Storing random choice in variable to compare with user choice
computer_choice = (choices[randint(0,2)])

# setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

# all images heights and widths to determine hitboxes
rock_w = 256
rock_h = 280
paper_w = 256
paper_h = 204
scissors_w = 256
scissors_h = 170

# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="orange")


# canvas object
cv = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)

# created welcome text 
welcometext = turtle.Turtle()
welcometext.penup()
welcometext.setposition(-180,150)
welcometext.write("Please choose rock, paper, or scissors:", font=("Verdana",15, "normal"))

# setup the rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')
# instantiate (create an instance of) the Turtle class for the rock
rock_instance = turtle.Turtle()
# add the rock image as a shape
screen.addshape(rock_image)
# attach the rock_image to the rock_instance
rock_instance.shape(rock_image)
# remove the pen option from the rock_instance so it doesn't draw lines when moved
rock_instance.penup()
# assign vars for rock position
rock_pos_x = -300
rock_pos_y = 0
# set the position of the rock_instance
rock_instance.setpos(rock_pos_x,rock_pos_y)


paper_image = os.path.join(images_folder, 'paper.gif')
paper_instance = turtle.Turtle()
screen.addshape(paper_image)
paper_instance.shape(paper_image)
paper_instance.penup()
paper_pos_x = 0
paper_pos_y = 0
paper_instance.setpos(paper_pos_x,paper_pos_y)

scissors_image = os.path.join(images_folder, 'scissors.gif')
scissors_instance = turtle.Turtle()
screen.addshape(scissors_image)
scissors_instance.shape(scissors_image)
scissors_instance.penup()
scissors_pos_x = 300
scissors_pos_y = 0
scissors_instance.setpos(scissors_pos_x,scissors_pos_y)

# instantiate a generic turtle
t = turtle.Turtle()
# instantiate a turtle for writing text
text = turtle.Turtle()
text.color('deep pink')
text.hideturtle()

# hide that turtle
t.hideturtle()

# this function uses and x y value, an obj
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] -  w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False

# created turtles for all outcomes
rock_outcomes = turtle.Turtle()
rock_win = turtle.Turtle()
rock_tie = turtle.Turtle()
rock_lose = turtle.Turtle()

paper_outcomes = turtle.Turtle()
paper_win = turtle.Turtle()
paper_tie = turtle.Turtle()
paper_lose = turtle.Turtle()

scissors_outcomes = turtle.Turtle()
scissors_win = turtle.Turtle()
scissors_tie = turtle.Turtle()
scissors_lose = turtle.Turtle()

# function that passes through wn onlick
def mouse_pos(x, y):
    # clears welcome text so no clutter
    welcometext.clear()
    # outcomes if clicks on rock
    if (collide(x,y,rock_instance,rock_w,rock_h)):
        # hides paper and scissors
        paper_instance.hideturtle()
        scissors_instance.hideturtle()
        # places text saying what you and computer chose
        rock_outcomes.penup()
        rock_outcomes.setposition(-180,150)
        rock_outcomes.write("You chose rock, " + "and computer chose" + " " + computer_choice, font=("Verdana",15, "normal"))
        # compares player choice and computer choice
        if computer_choice == "rock":
            # adds second rock image because computer chose rock
            cpu_rock_image = os.path.join(images_folder, 'cpurock.gif')
            cpu_rock_instance = turtle.Turtle()
            screen.addshape(cpu_rock_image)
            cpu_rock_instance.shape(cpu_rock_image)
            cpu_rock_instance.penup()
            cpu_rock_pos_x = 300
            cpu_rock_pos_y = 0
            cpu_rock_instance.setpos(cpu_rock_pos_x,cpu_rock_pos_y)
            # displays end result 
            rock_tie.penup()
            rock_tie.setposition(0,0)
            rock_tie.write("It's a tie!", font=("Verdana",15, "normal"))
        elif computer_choice == "paper":
            # adds paper image because computer chose paper
            cpu_paper_image = os.path.join(images_folder, 'cpupaper.gif')
            cpu_paper_instance = turtle.Turtle()
            screen.addshape(cpu_paper_image)
            cpu_paper_instance.shape(cpu_paper_image)
            cpu_paper_instance.penup()
            cpu_paper_pos_x = 300
            cpu_paper_pos_y = 0
            cpu_paper_instance.setpos(cpu_paper_pos_x,cpu_paper_pos_y)
            # displays end result
            rock_lose.penup()
            rock_lose.setposition(0,0)
            rock_lose.write("You lose!", font=("Verdana",15, "normal"))
        elif computer_choice == "scissors":
            # adds scissors image because computer chose scissors
            cpu_scissors_image = os.path.join(images_folder, 'cpuscissors.gif')
            cpu_scissors_instance = turtle.Turtle()
            screen.addshape(cpu_scissors_image)
            cpu_scissors_instance.shape(cpu_scissors_image)
            cpu_scissors_instance.penup()
            cpu_scissors_pos_x = 300
            cpu_scissors_pos_y = 0
            cpu_scissors_instance.setpos(cpu_scissors_pos_x,cpu_scissors_pos_y)\
            # displays end result
            rock_win.penup()
            rock_win.setposition(0,0)
            rock_win.write("You win!", font=("Verdana",15, "normal"))
        else:
            # just in case
            return False
    # outcomes if clicks on paper
    elif (collide(x,y,paper_instance,paper_w,paper_h)):
        paper_pos_x = -300
        paper_pos_y = 0
        paper_instance.setpos(paper_pos_x,paper_pos_y) 
        rock_instance.hideturtle()
        scissors_instance.hideturtle()
        paper_outcomes.penup()
        paper_outcomes.setposition(-180,150)
        paper_outcomes.write("You chose paper, " + "and computer chose" + " " + computer_choice, font=("Verdana",15, "normal"))
        paper_outcomes.penup()
        if computer_choice == "rock":
            cpu_rock_image = os.path.join(images_folder, 'cpurock.gif')
            cpu_rock_instance = turtle.Turtle()
            screen.addshape(cpu_rock_image)
            cpu_rock_instance.shape(cpu_rock_image)
            cpu_rock_instance.penup()
            cpu_rock_pos_x = 300
            cpu_rock_pos_y = 0
            cpu_rock_instance.setpos(cpu_rock_pos_x,cpu_rock_pos_y)
            paper_win.penup()
            paper_win.setposition(0,0)
            paper_win.write("You win!", font=("Verdana",15, "normal"))
        elif computer_choice == "paper":
            cpu_paper_image = os.path.join(images_folder, 'cpupaper.gif')
            cpu_paper_instance = turtle.Turtle()
            screen.addshape(cpu_paper_image)
            cpu_paper_instance.shape(cpu_paper_image)
            cpu_paper_instance.penup()
            cpu_paper_pos_x = 300
            cpu_paper_pos_y = 0
            cpu_paper_instance.setpos(cpu_paper_pos_x,cpu_paper_pos_y)
            paper_tie.penup()
            paper_tie.setposition(0,0)
            paper_tie.write("It's a tie!", font=("Verdana",15, "normal"))
        elif computer_choice == "scissors":
            cpu_scissors_image = os.path.join(images_folder, 'cpuscissors.gif')
            cpu_scissors_instance = turtle.Turtle()
            screen.addshape(cpu_scissors_image)
            cpu_scissors_instance.shape(cpu_scissors_image)
            cpu_scissors_instance.penup()
            cpu_scissors_pos_x = 300
            cpu_scissors_pos_y = 0
            cpu_scissors_instance.setpos(cpu_scissors_pos_x,cpu_scissors_pos_y)
            paper_lose.penup()
            paper_lose.setposition(0,0)
            paper_lose.write("You lose!", font=("Verdana",15, "normal"))
        else:
            return False
    # outcomes if clicks on scissors
    elif (collide(x,y,scissors_instance,scissors_w,scissors_h)):
        scissors_pos_x = -300
        scissors_pos_y = 0
        scissors_instance.setpos(scissors_pos_x,scissors_pos_y)
        paper_instance.hideturtle()
        rock_instance.hideturtle()
        scissors_outcomes.penup()
        scissors_outcomes.setposition(-180,150)
        scissors_outcomes.write("You chose scissors, " + "and computer chose" + " " + computer_choice, font=("Verdana",15, "normal"))
        if computer_choice == "rock":
            cpu_rock_image = os.path.join(images_folder, 'cpurock.gif')
            cpu_rock_instance = turtle.Turtle()
            screen.addshape(cpu_rock_image)
            cpu_rock_instance.shape(cpu_rock_image)
            cpu_rock_instance.penup()
            cpu_rock_pos_x = 300
            cpu_rock_pos_y = 0
            cpu_rock_instance.setpos(cpu_rock_pos_x,cpu_rock_pos_y)
            scissors_lose.penup()
            scissors_lose.setposition(0,0)
            scissors_lose.write("You lose!", font=("Verdana",15, "normal"))
        elif computer_choice == "paper":
            cpu_paper_image = os.path.join(images_folder, 'cpupaper.gif')
            cpu_paper_instance = turtle.Turtle()
            screen.addshape(cpu_paper_image)
            cpu_paper_instance.shape(cpu_paper_image)
            cpu_paper_instance.penup()
            cpu_paper_pos_x = 300
            cpu_paper_pos_y = 0
            cpu_paper_instance.setpos(cpu_paper_pos_x,cpu_paper_pos_y)
            scissors_win.penup()
            scissors_win.setposition(0,0)
            scissors_win.write("You win!", font=("Verdana",15, "normal"))
        elif computer_choice == "scissors":
            cpu_scissors_image = os.path.join(images_folder, 'cpuscissors.gif')
            cpu_scissors_instance = turtle.Turtle()
            screen.addshape(cpu_scissors_image)
            cpu_scissors_instance.shape(cpu_scissors_image)
            cpu_scissors_instance.penup()
            cpu_scissors_pos_x = 300
            cpu_scissors_pos_y = 0
            cpu_scissors_instance.setpos(cpu_scissors_pos_x,cpu_scissors_pos_y)
            scissors_tie.penup()
            scissors_tie.setposition(0,0)
            scissors_tie.write("It's a tie!", font=("Verdana",15, "normal"))
        else:
            return False
    else:
        # if user doesn't pick something
        turtle.write("pick something fool...", font=("Verdana",20, "normal"))

screen.onclick(mouse_pos)
# runs mainloop for Turtle - required to be last
screen.mainloop()

