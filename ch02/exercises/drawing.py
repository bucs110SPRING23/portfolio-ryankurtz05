import turtle

numSides = int(input("Enter the number of sides."))
lenSides = int(input("Enter the length of sides."))

internalAngle = 360/numSides

thomas = turtle.Turtle()
thomas.color("green")

for i in range(numSides):
    thomas.forward(lenSides)
    thomas.right(internalAngle)

thomas.screen.exitonclick() 