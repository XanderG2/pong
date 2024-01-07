import pygame, sys
pygame.init()

width = 900
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong by Xander")

white = (255,255,255)
black = (0,0,0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    screen.fill(black)
    pygame.display.flip()

pygame.quit()
