import pygame
import random
import math
from pygame import  mixer

#Intialize the pygame
pygame.init()
dis_width=800
dis_height=600
#creating a screen
screen = pygame.display.set_mode((dis_width,dis_height))

#Backgroud
bg=pygame.image.load('background.png')

#backgound sound
mixer.music.load('background.wav')
mixer.music.play(-1)

#Title and Icone
pygame.display.set_caption('Space Invader')
icone =pygame.image.load('ufo.png')
pygame.display.set_icon(icone)

#Player
playerimg =pygame.image.load('player.png')
playerx=370
playery=480
playerx_cng=0

enemyimg =[]
enemyX=[]
enemyY=[]
enemyX_cng=[]
enemyY_cng=[]
num_of_enemies = 6
for i in range(num_of_enemies):
     enemyimg.append(pygame.image.load('enemy.png'))
     enemyX.append(random.randint(0,734))
     enemyY.append(random.randint(50,150))
     enemyX_cng.append(4)
     enemyY_cng.append(20)

#Bullte
#you cant see the screen
#fire - the bullte is moving
bullimg =pygame.image.load('bullet.png')
bullX=0
bullY=480
bullX_cng=0
bullY_cng=10
bull_state="ready"
#Score
score=0
font = pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10
#Game over text
game_font=pygame.font.Font('freesansbold.ttf',364)
def game_over_text():
    game_text = font.render("G A M E O V E R",True,(255,255,255))
    screen.blit(game_text, (200,250))
def show_score(x, y):
    score_t=font.render("Score:"+ str(score),True,(255,255,255))
    screen.blit(score_t, (x, y))
def player(x,y):
    screen.blit(playerimg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
def fire_bull(x,y):
    global bull_state
    bull_state="fire"
    screen.blit(bullimg,(x+16,y+10))  #(x+16,y+10) is use to set the bullte in the middel of ship

def isColl(enemyX,enemyY,bullX,bullY):
    distance = math.sqrt(math.pow(enemyX - bullX, 2) + (math.pow(enemyY - bullY, 2)))
    if distance<27:
        return  True
    else:
        return False


#Game Loop
running =True
while running:

    screen.fill((150, 0, 0))
    #backgorudn img
    screen.blit(bg,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    #if key stroke is press check
        if event.type==pygame.KEYDOWN:

            if event.key==pygame.K_LEFT:
                playerx_cng =-5
            if event.key==pygame.K_RIGHT:
                playerx_cng = 5
            if event.key==pygame.K_SPACE:
                bull_sound=mixer.Sound('laser.wav')
                bull_sound.play()
                #if bull_state is "ready":
                bullX=playerx
                fire_bull(bullX,bullY)
        if event.type== pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerx_cng = 0
#checking for boundaries
    playerx+=playerx_cng
    if playerx<=0:
        playerx=0
    elif playerx >=735:
        playerx=735

#Enemy Movement
    for i in range(num_of_enemies):
        #Game over
        if enemyY[i]>200:
            for j in i in range(num_of_enemies):
                enemyY[j]=200
                game_over_text()
                break
        enemyX[i]+= enemyX_cng[i]
        if enemyX[i]<= 0:
            enemyX_cng[i] =4
            enemyY[i]=enemyY_cng[i]
        elif enemyX[i] >= 735:
            enemyX_cng[i]  =-4
            enemyY[i]+= enemyY_cng[i]
        # Collution
        coll = isColl(enemyX[i], enemyY[i], bullX, bullY)
        if coll:
            exp_sound= mixer.Sound('explosion.wav')
            exp_sound.play()
            bullY = 480
            bull_state = "ready"
            score += 1

            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i],enemyY[i],i)

    #Bullet movement
    if bullY<=0:
        bullY=480
        bull_state="ready"
    if bull_state is "fire":
        fire_bull(bullX,bullY)
        bullY-=bullY_cng

    player(playerx,playery)
    show_score(textX,textY)
    pygame.display.update()