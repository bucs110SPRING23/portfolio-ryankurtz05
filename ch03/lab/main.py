import turtle #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
michelangelo.forward(random.randrange(1,101))
leonardo.forward(random.randrange(1,101))
#Reset
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)


for i in range(3):
    michelangelo.forward(random.randrange(1,101))
    leonardo.forward(random.randrange(1,101))
#Reset
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# PART B - complete part B here
pygame.init()
display = pygame.display.set_mode()

points = list()
numSides = int()


window.exitonclick()
