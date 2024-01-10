import pygame, sys, math
pygame.init()
pygame.font.init()

pfont = pygame.font.SysFont('comicsans', 15) # point font


def calculate_movement(degrees): # generated by chatgpt
    radians = math.radians(degrees)
    x = math.cos(radians)
    y = math.sin(radians)
    return x, y

def calculate_angle(x, y): #generated by chatgpt when i asked it to reverse the last function
    radians = math.atan2(y, x)
    degrees = math.degrees(radians)
    return degrees


width = 900
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong by Xander")

white = (255,255,255)
black = (0,0,0)

pw = 15 # player width
ph = 50 # player height
pm = height//2-ph//2 # player middle (where the players start) (halfway throught the screen - half of the player height)
pg = 25 # player gap (from the side)

p1 = pygame.Rect(0+pg,pm,pw,ph) # player 1
p1p = 0 # player 1 points
p2 = pygame.Rect(width-pw-pg,pm,pw,ph) # player 2
p2p = 0 # player 2 points

ballx = width//2 # ball x coord
ballxd10 = ballx*10 # ball x divided by 10
bally = height//2 # ball y coord
ballyd10 = bally*10 # ball y divided by 10
ballr = 10 # ball radius
balld = 0 # ball direction
ballw = 10 # ball line width (fill ball)
ballhb = pygame.Rect(ballx-ballr, bally-ballr, ballr*2, ballr*2) # ball hitbox
pballs = 2 # player and ball speed

p1yd10 = p1.y*10 # player 1 y divided by 10
p2yd10 = p2.y*10 # player 2 y divided by 10

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    keys = pygame.key.get_pressed() # list of pressed keys, used so held keys count
    if keys:
        if keys[pygame.K_UP] and p2.y > 0: # if up arrow is pressed and p2 y is greater than 0 (top of screen)
            p2yd10 -= pballs # player 2 y divided by 10 is subtracted (up) by player speed
        if keys[pygame.K_DOWN] and p2.y < height-p2.height: # if down arrow is pressed and p2 y is less than height of screen - p2 height (bottom of screen)
            p2yd10 += pballs # player 2 y divided by 10 is added (down) to player speed
        if keys[pygame.K_w] and p1.y > 0: # if w key is pressed and p1 y is greater than 0 (top of screen)
            p1yd10 -= pballs # player 1 y divided by 10 is subtracted (up) by player speed
        if keys[pygame.K_s] and p1.y < height-p1.height: # if s key is pressed and p1 y is less than height of screen - p1 height (bottom of screen)
            p1yd10 += pballs # player 1 y divided by 10 is added (down) to player speed
    p1.y = p1yd10//10 # p1 y is p1 y divided by 10 divided by 10
    p2.y = p2yd10//10 # p2 y is p2 y divided by 10 divided by 10
    if ballhb.colliderect(p1): # if ball is touching p1
        dfm = bally - p1.centery # distance from middle
        my = dfm//10 # movement y
        if my < 0.5:
            my = 0.5
        if mx > -0.5: # movement x
            mx = -0.5
        mx = -mx
        balld = calculate_angle(mx, my)
    if ballhb.colliderect(p2): # same thing but p2
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
    mx, my = [x*pballs for x in calculate_movement(balld)] # movement y, x
    ballxd10 += mx
    ballyd10 += my
    if ballx == 0: # player 2 point if ball is touching left side
        p2p += 1
        ballxd10 = width//2 * 10
        ballyd10 = height//2 * 10
    if ballx == width-ballr: # player 1 point if ball is touching right side
        p1p += 1
        ballxd10 = width//2 * 10
        ballyd10 = height//2 * 10
    ballx = ballxd10//10
    bally = ballyd10//10
    ballhb = pygame.Rect(ballx-ballr, bally-ballr, ballr*2, ballr*2)
    screen.fill(black)
    pygame.draw.rect(screen, white, p1) # draw player 1
    pygame.draw.rect(screen, white, p2) # draw player 2
    pygame.draw.circle(screen, (255,255,255), (ballx, bally), ballr, ballw) # draw ball
    pointtext1 = pfont.render(str(p1p), False, (white)) # player 1s points rendered
    pointtext2 = pfont.render(str(p2p), False, (white)) # player 1s points rendered
    screen.blit(pointtext1, (0,0)) # blit player 1s points onto screen
    screen.blit(pointtext2, (width-pointtext2.get_width(), 0)) # blit player 2s points onto screen
    pygame.display.flip()

pygame.quit()
