import pygame, sys
pygame.init()

width = 900
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong by Xander")

white = (255,255,255)
black = (0,0,0)

pw = 15
ph = 50
pm = height//2-ph//2
pg = 25

p1 = pygame.Rect(0+pg,pm,pw,ph)
p2 = pygame.Rect(width-pw-pg,pm,pw,ph)

p1yd10 = p1.y*10
p2yd10 = p2.y*10

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys:
        if keys[pygame.K_UP] and p2.y > 0:
            p2yd10 -= 1
        if keys[pygame.K_DOWN] and p2.y < height-p2.height:
            p2yd10 += 1
        if keys[pygame.K_w] and p1.y > 0:
            p1yd10 -= 1
        if keys[pygame.K_s] and p1.y < height-p1.height:
            p1yd10 += 1
    p1.y = p1yd10//10
    p2.y = p2yd10//10
    screen.fill(black)
    pygame.draw.rect(screen, white, p1)
    pygame.draw.rect(screen, white, p2)
    pygame.display.flip()

pygame.quit()
