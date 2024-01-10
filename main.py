import pygame, sys, math
pygame.init()


def calculate_movement(degrees):
    radians = math.radians(degrees)
    x = math.cos(radians)
    y = math.sin(radians)
    return x, y

def calculate_angle(x, y):
    radians = math.atan2(y, x)
    degrees = math.degrees(radians)
    return degrees


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
p1p = 0
p2 = pygame.Rect(width-pw-pg,pm,pw,ph)
p2p = 0

ballx = width//2
ballxd10 = ballx*10
bally = height//2
ballyd10 = bally*10
ballr = 10
balld = 0
ballw = 10
ballhb = pygame.Rect(ballx-ballr, bally-ballr, ballr*2, ballr*2)
pballs = 2

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
            p2yd10 -= pballs
        if keys[pygame.K_DOWN] and p2.y < height-p2.height:
            p2yd10 += pballs
        if keys[pygame.K_w] and p1.y > 0:
            p1yd10 -= pballs
        if keys[pygame.K_s] and p1.y < height-p1.height:
            p1yd10 += pballs
    p1.y = p1yd10//10
    p2.y = p2yd10//10
    if ballhb.colliderect(p1):
        dfm = bally - p1.centery
        my = dfm//10
        if my < 0.5:
            my = 0.5
        if mx > -0.5:
            mx = -0.5
        mx = -mx
        balld = calculate_angle(mx, my)
    if ballhb.colliderect(p2):
        dfm = bally - p2.centery
        my = dfm//10
        if my < 0.5:
            my = 0.5
        if mx < 0.5:
            mx = 0.5
        mx = -mx
        balld = calculate_angle(mx, my)
    if bally == 0 or bally == height-ballr:
        balld = 360 - balld
    mx, my = [x*pballs for x in calculate_movement(balld)]
    ballxd10 += mx
    ballyd10 += my
    if ballx == 0:
        p2p += 1
        ballxd10 = width//2 * 10
        ballyd10 = height//2 * 10
    if ballx == width-ballr:
        p1p += 1
        ballxd10 = width//2 * 10
        ballyd10 = height//2 * 10
    ballx = ballxd10//10
    bally = ballyd10//10
    ballhb = pygame.Rect(ballx-ballr, bally-ballr, ballr*2, ballr*2)
    screen.fill(black)
    pygame.draw.rect(screen, white, p1)
    pygame.draw.rect(screen, white, p2)
    pygame.draw.circle(screen, (255,255,255), (ballx, bally), ballr, ballw)
    pygame.display.flip()
    print(f"Player 1 points: {p1p}, Player 2 points: {p2p}")

pygame.quit()
