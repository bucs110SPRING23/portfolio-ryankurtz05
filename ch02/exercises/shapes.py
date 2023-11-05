import pygame

pygame.init()

while True:
    for event in pygame.event.get():
        pass


    screen = pygame.display.set_mode([1000,1000])

    pygame.draw.circle(screen,"red",[500,200],50)
    pygame.draw.circle(screen,"red",[500,300],75)
    pygame.draw.circle(screen,"red",[500,415],100)
    pygame.display.flip()
    pygame.time.wait(3000)

    break
