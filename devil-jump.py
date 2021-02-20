import pygame, sys
from pygame.locals import *
import teddysfunctions

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

WIDTH = 1200
HEIGHT = 400
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Devil Jump")

BLACK = (  0,  0,  0)
WHITE = (255,255,255)
RED   = (255,  0,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)
AQUA  = (  0,255,255)
OLIVE = (128,128,  0)
SKYBL = (128,128,255)
YELLOW= (255,255,  0)

# pygame.draw.polygon(DISPLAYSURF, BLACK, ((146,0),(291,106),(236,277),(56,277),(0,106)))
#
# pygame.draw.polygon(DISPLAYSURF, WHITE, teddysfunctions.spike(200,300))
# pygame.draw.polygon(DISPLAYSURF, WHITE, teddysfunctions.spike(100,400))
# pygame.draw.circle(DISPLAYSURF, YELLOW, (225,200), 30, 0)

ballImg = pygame.image.load('smileyball2.png')
ballX = 250
ballY = 200
ballD = 'right'
ballS = 12

devilImg = pygame.image.load('devil.png')
devilX = 0
devilY = 200
devilD = 'right'
devilStartS = 12
devilS = devilStartS


# Words using fonts
fontObj = pygame.font.Font('PressStart2P-Regular.ttf', 24)
textSurfaceObj = fontObj.render('Start', True, WHITE, None)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (250, 100)
text2SurfaceObj = fontObj.render('press <- ^ -> ', True, WHITE, None)
text2RectObj = text2SurfaceObj.get_rect()
text2RectObj.center = (250, 150)

# Sounds
jumpSound = pygame.mixer.Sound('zapsplat.wav')
bkgSound = pygame.mixer.Sound('background-sound.wav')
bkgSound.play(-1, 0)

# Gravity
isJump = False
jumpHeight = 10
ballMass = 1

# Sides and Score
score = 0
if ballX < devilX:
    currentSide = 'left'
    previousSide = 'left'
else:
    currentSide = 'right'
    previousSide = 'right'

while True: # main game loop

    DISPLAYSURF.fill(SKYBL)
    pygame.draw.rect(DISPLAYSURF, GREEN, (0, HEIGHT-100, WIDTH, 100))

    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    DISPLAYSURF.blit(text2SurfaceObj, text2RectObj)

    scoreSurfaceObj = fontObj.render(str(score), True, WHITE, None)
    scoreRectObj = scoreSurfaceObj.get_rect()
    scoreRectObj.center = (WIDTH-50, 50)
    DISPLAYSURF.blit(scoreSurfaceObj, scoreRectObj)

    # BALL SCROLLING
    # if ballX == 400:
    #     jumpSound.play()

    if (ballX >= WIDTH) and (ballD == 'right'):
        ballX = -40
    elif (ballX <= -40) and (ballD == 'left'):
        ballX = WIDTH
    else:
        ballX += ballS * (1 if ballD == 'right' else -1)

    if (devilX >= WIDTH) and (devilD == 'right'):
        devilX = -40
    elif (devilX <= -40) and (devilD == 'left'):
        devilX = WIDTH
    else:
        devilX += devilS * (1 if devilD == 'right' else -1)

    # BALL MOVING AROUND
    # if ballD == 'right':
    #     ballX += ballS
    #     if ballX >= 300:
    #         ballD = 'down'
    # elif ballD == 'down':
    #     ballY += ballS
    #     if ballY >= 300:
    #         ballD = 'left'
    # elif ballD == 'left':
    #     ballX -= ballS
    #     if ballX <= 100:
    #         ballD = 'up'
    # elif ballD == 'up':
    #     ballY -= ballS
    #     if ballY <= 100:
    #         ballD = 'right'

    DISPLAYSURF.blit(ballImg, (ballX, ballY))
    DISPLAYSURF.blit(devilImg, (devilX, devilY))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key in (K_LEFT, K_a):
                ballD = 'left'
            elif event.key in (K_RIGHT, K_d):
                ballD = 'right'
            elif event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key in (K_UP, K_SPACE, K_w):
                isJump = True

    if isJump:
        F = (1/2) * m * (v**2)
        ballY -= F
        v = v-1
        if v < 0:
            m=-1
        if v < -jumpHeight:
            isJump = False
        jumpSound.play()
    if not isJump:
            v = jumpHeight
            m = ballMass

    ballRect = ballImg.get_rect(x=ballX, y=ballY)
    devilRect = devilImg.get_rect(x=devilX, y=devilY)
    # print(ballRect, devilRect)
    if ballRect.colliderect(devilRect):
        print("We collided!")
        ballX = 250
        ballY = 200
        ballD = 'right'

        devilX = 0
        devilY = 200
        devilD = 'right'

        isJump = False
        score = 0
        devilS = devilStartS

        if ballX < devilX:
            currentSide = 'left'
            previousSide = 'left'
        else:
            currentSide = 'right'
            previousSide = 'right'

    # Detect Jump Over
    if ballX < devilX:
        currentSide = 'left'
    else:
        currentSide = 'right'

    if ballX < devilX:
        currentSide = 'left'
    else:
        currentSide = 'right'

    if isJump and (previousSide != currentSide):
        score += 1
        devilS += 1

    # else:
    #     print("We didn't collide")
    previousSide = currentSide

    pygame.display.update()
    fpsClock.tick(FPS)