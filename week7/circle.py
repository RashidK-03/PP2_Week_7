import pygame

screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Circle")
x,y = 300,200
while 1:
    screen.fill("white")
    circle = pygame.draw.circle(screen,("red"),(x,y),25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if 0 <= x <= 600 and 0 <= y <= 400:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= .25
        if pressed[pygame.K_DOWN]: y += .25
        if pressed[pygame.K_LEFT]: x-= .25
        if pressed[pygame.K_RIGHT]: x += .25
    else:
        if x <= 0:
            x += .1
        elif x >= 600:
            x -= .1
        if y <= 0:
            y += .1
        elif y >= 400:
            y -= .1
    pygame.display.update()