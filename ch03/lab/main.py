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


#Race 1
michelangelo.forward(random.randrange(1,101))
leonardo.forward(random.randrange(1,101))
#Reset
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)



#Race 2
for i in range(3):
    michelangelo.forward(random.randrange(1,101))
    leonardo.forward(random.randrange(1,101))
#Reset
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)


# PART B - complete part B here
pygame.init()
display = pygame.display.set_mode([500,500])

sideLength = 40
xpos = 250
ypos = 250
points = list()

#Triangle
numSides = 3

for i in range(numSides):
    angle = 360/numSides
    radians = math.radians(angle * i)
    x = xpos + sideLength * math.cos(radians)
    y = ypos + sideLength * math.sin(radians)
    points.append([x,y])

pygame.draw.polygon(display,"red",points)
pygame.display.flip()

pygame.time.wait(1000)




#Clear screen
display.fill("black")
pygame.display.flip()

#Square
points = []
numSides = 4

for i in range(numSides):
    angle = 360/numSides
    radians = math.radians(angle * i)
    x = xpos + sideLength * math.cos(radians)
    y = ypos + sideLength * math.sin(radians)
    points.append([x,y])

pygame.draw.polygon(display,"blue",points)
pygame.display.flip()

pygame.time.wait(1000)




#Clear screen
display.fill("black")
pygame.display.flip()

#Hexagon
points = []
numSides = 6

for i in range(numSides):
    angle = 360/numSides
    radians = math.radians(angle * i)
    x = xpos + sideLength * math.cos(radians)
    y = ypos + sideLength * math.sin(radians)
    points.append([x,y])

pygame.draw.polygon(display,"green",points)
pygame.display.flip()

pygame.time.wait(1000)




#Clear screen
display.fill("black")
pygame.display.flip()

#Icosagon
points = []
numSides = 20

for i in range(numSides):
    angle = 360/numSides
    radians = math.radians(angle * i)
    x = xpos + sideLength * math.cos(radians)
    y = ypos + sideLength * math.sin(radians)
    points.append([x,y])

pygame.draw.polygon(display,"blue",points)
pygame.display.flip()
pygame.time.wait(1000)




#Clear screen
display.fill("black")
pygame.display.flip()

#Hectagon
points = []
numSides = 100

for i in range(numSides):
    angle = 360/numSides
    radians = math.radians(angle * i)
    x = xpos + sideLength * math.cos(radians)
    y = ypos + sideLength * math.sin(radians)
    points.append([x,y])

pygame.draw.polygon(display,"white",points)
pygame.display.flip()
pygame.time.wait(1000)




#Clear screen
display.fill("black")
pygame.display.flip()

#Circle
points = []
numSides = 360

for i in range(numSides):
    angle = 360/numSides
    radians = math.radians(angle * i)
    x = xpos + sideLength * math.cos(radians)
    y = ypos + sideLength * math.sin(radians)
    points.append([x,y])

pygame.draw.polygon(display,"pink",points)
pygame.display.flip()

window.exitonclick()