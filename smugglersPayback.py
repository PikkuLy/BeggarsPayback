import sys
from random import randint, choice
from math import sin, cos, radians
import os
import pygame
from pygame.sprite import Sprite
from pygame.locals import *


playerPic = pygame.image.load('falcon.png')
credits = pygame.image.load("bountyLoot.png")
player_rect = playerPic.get_rect()
credit_rect = credits.get_rect()
credit_count = 0


pygame.init()
screen = pygame.display.set_mode((1500, 1000), 0, 32)
clock = pygame.time.Clock()
pygame.display.set_caption('Smugglers Payback')

font = pygame.font.SysFont("monospace",30)

def checkCollision(rect1,rect2):
    return rect1.colliderect(rect2)

def winner():
    screen_w, screen_h = 1500, 1000
    background = 0, 0, 0

    screen = pygame.display.set_mode(
                (screen_w, screen_h), 0, 32)

    font = pygame.font.SysFont("monospace",60)
    font2 = pygame.font.SysFont("monospace",30)
    
    
    while True:
        time_passed = clock.tick(50)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

        if(pygame.key.get_pressed()[pygame.K_ESCAPE]):
            exit_game()

        
        label = font.render("You Won!! You paid Jabba in Full.",1,(255,255,0))
        label_pos = label.get_rect(centerx=screen.get_width()/2,centery = screen.get_height()/2+120)
        label2 = font2.render("Looks like Jabba will have to find a new wall decoration...",1,(255,255,0))
        label2_pos = label.get_rect(centerx = screen.get_width()/2 +40,centery = screen.get_height()/2 + 200) 

        screen.fill(background)
        screen.blit(label,label_pos)
        screen.blit(label2,label2_pos)
        screen.blit(playerPic, (screen.get_width()/2, screen.get_height()/2 - 50))
        

        pygame.display.flip()

def welcome():
    screen_w, screen_h = 1500, 1000
    background = 0, 0, 0

    screen = pygame.display.set_mode((screen_w, screen_h), 0, 32)

    font = pygame.font.SysFont("monospace",30)
    
    
    while True:
        time_passed = clock.tick(50)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

        if(pygame.key.get_pressed()[pygame.K_ESCAPE]):
            exit_game()

        
        label = font.render("You have a debt on your head. Pick up the coins to pay Jabba the Hutt back.",1,(255,255,0))
        label_pos = label.get_rect(centerx=screen.get_width()/2,centery = screen.get_width()/2)
        label2 = font.render("Each level you need to pick up 25 coins to move onto the next level." ,1, (255,255,0))
        label2_pos = label2.get_rect(centerx=screen.get_width()/2,centery = screen.get_width()/2 + 35)
        label25 = font.render("Use the arrow keys to fly your ship around",1,(255,255,0))
        label25_pos = label25.get_rect(centerx=screen.get_width()/2,centery = screen.get_width()/2 + 70)
        label3 = font.render("Press enter to start the game." ,1, (255,255,0))
        label3_pos = label3.get_rect(centerx=screen.get_width()/2,centery = screen.get_width()/2 + 110)

        if(pygame.key.get_pressed()[pygame.K_RETURN]):
            levelOne(pygame.image.load('worm.png'))

        screen.fill(background)
        screen.blit(label,label_pos)
        screen.blit(label2,label2_pos)
        screen.blit(label25,label25_pos)
        screen.blit(label3,label3_pos)
        screen.blit(playerPic, (screen.get_width()/2, screen.get_height()/2 - 50))
        

        pygame.display.flip()

# ---------------------------------------------------level 1 -----------------------------------------------------------------
def levelOne(badGuy):
    screen_w, screen_h = 1500, 1000
    background = 0, 0, 0

    credit_count = 0

    enemyPic = badGuy

    enemy_rect = enemyPic.get_rect()
    enemyStartX = 500
    enemyStartY = 500
    
    enemy_rect.x=enemyStartX
    enemy_rect.y=enemyStartY

    screen = pygame.display.set_mode((screen_w, screen_h), 0, 32)
    clock = pygame.time.Clock()

    playerStartX = screen.get_width()/2
    playerStartY = screen.get_height()/2 -50
    
    player_rect.x=playerStartX
    player_rect.y=playerStartY

    creditX = randint(0, screen_w -10)
    creditY = randint(0, screen_h-20)
    credit_rect.x = creditX
    credit_rect.y = creditY
    
    
        
    while True:
        time_passed = clock.tick(50)
        label = font.render("Level 1: Credits: "+ str(credit_count),1,(255,255,0))
        label_pos = label.get_rect(centerx=screen.get_width()/2)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

        if(credit_count == 25):
            levelTwo(pygame.image.load('tie.png'))
        
        
        enemyStartX +=10
        enemy_rect.x +=10
        if(enemyStartX >= screen.get_width()):
            enemyStartX = 0 - enemyStartX
            enemy_rect.x = enemyStartX
            enemyStartY = randint(0,screen_h-80)
            enemy_rect.y = enemyStartY
            
        if checkCollision(enemy_rect,player_rect):
            credit_count = 0
            screen.blit(label,(label_pos))
            
        if checkCollision(enemy_rect,credit_rect):
            credit_count -= 1
            screen.blit(label,(label_pos))
            creditX = randint(0, screen_w-50)
            creditY = randint(0, screen_h-80)
            credit_rect.x = creditX
            credit_rect.y = creditY
            screen.blit(credits, (creditX,creditY),credit_rect)
            screen.blit(credits,credit_rect)
        
        if(pygame.key.get_pressed()[pygame.K_UP] !=0):
            playerStartY -=9
            player_rect.y -=9
            if checkCollision(credit_rect,player_rect):
                credit_count +=1
                screen.blit(label,(label_pos))
                creditX = randint(0, screen_w-50)
                creditY = randint(0, screen_h-80)
                credit_rect.x = creditX
                credit_rect.y = creditY
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)
            
        if(pygame.key.get_pressed()[pygame.K_DOWN] !=0):
            playerStartY +=9
            player_rect.y +=9
            if checkCollision(credit_rect,player_rect):
                credit_count +=1
                screen.blit(label,(label_pos))
                creditX = randint(0, screen_w-50)
                creditY = randint(0, screen_h-80)
                credit_rect.x = creditX
                credit_rect.y = creditY
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)
            
        if(pygame.key.get_pressed()[pygame.K_LEFT] !=0):
            playerStartX -=9
            player_rect.x -=9
            if checkCollision(credit_rect,player_rect):
                credit_count +=1
                screen.blit(label,(label_pos))
                creditX = randint(0, screen_w-50)
                creditY = randint(0, screen_h-80)
                credit_rect.x = creditX
                credit_rect.y = creditY
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)
            
        if(pygame.key.get_pressed()[pygame.K_RIGHT] !=0):
            playerStartX +=9
            player_rect.x +=9
            if checkCollision(credit_rect,player_rect):
                credit_count +=1
                screen.blit(label,(label_pos))
                creditX = randint(0, screen_w-50)
                creditY = randint(0, screen_h-80)
                credit_rect.x = creditX
                credit_rect.y = creditY
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)

        if(pygame.key.get_pressed()[pygame.K_ESCAPE]):
            exit_game()

        
        screen.fill(background)
        screen.blit(playerPic, (playerStartX,playerStartY))
        screen.blit(enemyPic,(enemyStartX,enemyStartY))
        screen.blit(label,label_pos)
        screen.blit(playerPic, player_rect)
    

        screen.blit(credits, (creditX,creditY))
        screen.blit(credits,credit_rect)
        screen.blit(label,label_pos)
        

        pygame.display.flip()
    
#----------------------------------- level 2 --------------------------------------------------------------------
def levelTwo(badGuy):
    screen_w, screen_h = 1500, 1000
    background = 0, 0, 0

    credit_count = 0

    enemyPic = badGuy
    enemy2 = enemyPic
    enemy3 = enemyPic
    enemy_rect = enemyPic.get_rect()
    enemy2_rect = enemy2.get_rect()
    enemy3_rect = enemy3.get_rect()

    screen = pygame.display.set_mode(
                (screen_w, screen_h), 0, 32)
    clock = pygame.time.Clock()


    playerStartX = 260
    playerStartY = 300
    
    player_rect.x=playerStartX
    player_rect.y=playerStartY

    enemyStartX = randint(0,screen_w -80)
    enemyStartY = randint(0,screen_h -50)
    
    enemy_rect.x=enemyStartX
    enemy_rect.y=enemyStartY

    enemy2X = randint(0,screen_w -80)
    enemy2Y = randint(0,screen_h -50)
    enemy2_rect.x = enemy2X
    enemy2_rect.y = enemy2Y

    enemy3X = randint(0,screen_w -80)
    enemy3Y = randint(0,screen_h -50)
    enemy3_rect.x = enemy3X
    enemy3_rect.y = enemy3Y 

    creditX = randint(0, screen_w -50)
    creditY = randint(0, screen_h-80)
    credit_rect.x = creditX
    credit_rect.y = creditY

    
    while True:
        time_passed = clock.tick(50)
        label = font.render("Level 2: Credits: "+ str(credit_count),1,(255,255,0))
        label_pos = label.get_rect(centerx=screen.get_width()/2)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

        if(credit_count == 25):
            levelThree(pygame.image.load('sd.png'))
        
        enemyStartX +=9
        enemy_rect.x +=9
        if(enemyStartX >= screen.get_width()):
            enemyStartX = 0 - enemyStartX
            enemy_rect.x = enemyStartX
            enemyStartY = randint(0,screen_h-80)
            enemy_rect.y = enemyStartY

        enemy2X +=9
        enemy2_rect.x +=9
        if(enemy2X >= screen.get_width()):
            enemy2X = 0 - enemy2X
            enemy2_rect.x = enemy2X
            enemy2Y = randint(0,screen_w-80)
            enemy2_rect.y = enemy2Y

        enemy3X +=9
        enemy3_rect.x +=9
        if(enemy3X >= screen.get_width()):
            enemy3X = 0 - enemy3X
            enemy3_rect.x = enemy3X
            enemy3Y = randint(0,screen_w-80)
            enemy3_rect.y = enemy3Y

        if checkCollision(enemy_rect,player_rect):
            credit_count = 0
            screen.blit(label,(label_pos))

        if checkCollision(enemy_rect,credit_rect):
            credit_count -= 1
            creditX = randint(0, screen_w-50)
            creditY = randint(0, screen_h-80)
            credit_rect.x = creditX
            credit_rect.y = creditY
            screen.blit(label,(label_pos))
            screen.blit(credits, (creditX,creditY),credit_rect)
            screen.blit(credits,credit_rect)

        if checkCollision(enemy2_rect,player_rect):
            credit_count = 0
            screen.blit(label,(label_pos))
            screen.blit(credits, (creditX,creditY),credit_rect)
            screen.blit(credits,credit_rect)

        if checkCollision(enemy2_rect,credit_rect):
            credit_count -= 1
            creditX = randint(0, screen_w-50)
            creditY = randint(0, screen_h-80)
            credit_rect.x = creditX
            credit_rect.y = creditY
            screen.blit(label,(label_pos))
            screen.blit(credits, (creditX,creditY),credit_rect)
            screen.blit(credits,credit_rect)

        if checkCollision(enemy3_rect,player_rect):
            credit_count = 0
            screen.blit(label,(label_pos))
            screen.blit(credits, (creditX,creditY),credit_rect)
            screen.blit(credits,credit_rect)

        if checkCollision(enemy3_rect,credit_rect):
            credit_count -= 1
            creditX = randint(0, screen_w-50)
            creditY = randint(0, screen_h-80)
            credit_rect.x = creditX
            credit_rect.y = creditY
            screen.blit(label,(label_pos))
            screen.blit(credits, (creditX,creditY),credit_rect)

        if(pygame.key.get_pressed()[pygame.K_UP] !=0):
            playerStartY -=10
            player_rect.y -=10
            #print player_rect.y
            if checkCollision(credit_rect,player_rect):
                credit_count +=1
                screen.blit(label,(label_pos))
                creditX = randint(0, screen_w-50)
                creditY = randint(0, screen_h-80)
                credit_rect.x = creditX
                credit_rect.y = creditY
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)
            
        if(pygame.key.get_pressed()[pygame.K_DOWN] !=0):
            playerStartY +=10
            player_rect.y +=10
            if checkCollision(credit_rect,player_rect):
                credit_count +=1
                screen.blit(label,(label_pos))
                creditX = randint(0, screen_w-50)
                creditY = randint(0, screen_h-80)
                credit_rect.x = creditX
                credit_rect.y = creditY
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)
            
        if(pygame.key.get_pressed()[pygame.K_LEFT] !=0):
            playerStartX -=10
            player_rect.x -=10
            if checkCollision(credit_rect,player_rect):
                credit_count +=1
                screen.blit(label,(label_pos))
                creditX = randint(0, screen_w-50)
                creditY = randint(0, screen_h-80)
                credit_rect.x = creditX
                credit_rect.y = creditY
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)
            
        if(pygame.key.get_pressed()[pygame.K_RIGHT] !=0):
            playerStartX +=10
            player_rect.x +=10
            if checkCollision(credit_rect,player_rect):
                credit_count +=1
                screen.blit(label,(label_pos))
                creditX = randint(0, screen_w-50)
                creditY = randint(0, screen_h-80)
                credit_rect.x = creditX
                credit_rect.y = creditY
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)

        if(pygame.key.get_pressed()[pygame.K_ESCAPE]):
            exit_game()

        
        screen.fill(background)
        screen.blit(playerPic, (playerStartX,playerStartY))
        screen.blit(label,label_pos)
        screen.blit(playerPic, player_rect)

        screen.blit(enemyPic,(enemyStartX,enemyStartY))
        screen.blit(enemyPic,enemy_rect)

        screen.blit(enemy2, (enemy2X,enemy2Y))
        screen.blit(enemy2,enemy2_rect)

        screen.blit(enemy3, (enemy3X,enemy3Y))
        screen.blit(enemy3,enemy3_rect)

        screen.blit(credits, (creditX,creditY),credit_rect)
        screen.blit(credits,credit_rect)
        screen.blit(label,label_pos)
        

        pygame.display.flip()

#--------------------------------- LEVEL 3 ------------------------------------------------
def levelThree(badGuy):
    screen_w, screen_h = 1500, 1000
    background = 0, 0, 0
    credit_count = 0

    enemyPic = badGuy
    enemy2 = enemyPic
    enemy_rect = enemyPic.get_rect()
    enemy2_rect = enemy2.get_rect()

    playerStartX = 260
    playerStartY = 300
    
    player_rect.x=playerStartX
    player_rect.y=playerStartY

    enemyStartX = 260
    enemyStartY = 100
    
    enemy_rect.x=enemyStartX
    enemy_rect.y=enemyStartY

    enemy2X = 500
    enemy2Y = 800
    enemy2_rect.x = enemy2X
    enemy2_rect.y = enemy2Y 

    creditX = randint(0, screen_w -50)
    creditY = randint(0, screen_h-80)
    credit_rect.x = creditX
    credit_rect.y = creditY
    
    while True:
        time_passed = clock.tick(50)
        label = font.render("Level 3: Credits: "+ str(credit_count),1,(255,255,0))
        label_pos = label.get_rect(centerx=screen.get_width()/2)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

        if credit_count == 25:
            winner()
            
        enemyStartX +=12
        enemy_rect.x +=12
        if(enemyStartX >= screen.get_width()):
            enemyStartX = 0 - enemyStartX
            enemy_rect.x = enemyStartX
            enemyStartY = randint(0,screen_w-80)
            enemy_rect.y = enemyStartY

        enemy2X +=12
        enemy2_rect.x +=12
        if(enemy2X >= screen.get_width()):
            enemy2X = 0 - enemy2X
            enemy2_rect.x = enemy2X
            enemy2Y = randint(0,screen_w-80)
            enemy2_rect.y = enemy2Y

        if checkCollision(enemy_rect,player_rect):
            credit_count = 0
            screen.blit(label,(label_pos))

        if checkCollision(enemy_rect,credit_rect):
            credit_count -= 1
            creditX = randint(0, screen_w-50)
            creditY = randint(0, screen_h-80)
            credit_rect.x = creditX
            credit_rect.y = creditY
            screen.blit(label,(label_pos))
            screen.blit(credits, (creditX,creditY),credit_rect)
            screen.blit(credits,credit_rect)

        if checkCollision(enemy2_rect,player_rect):
            credit_count = 0
            screen.blit(label,(label_pos))
            screen.blit(credits, (creditX,creditY),credit_rect)
            screen.blit(credits,credit_rect)

        if checkCollision(enemy2_rect,credit_rect):
            credit_count -= 1
            creditX = randint(0, screen_w-50)
            creditY = randint(0, screen_h-80)
            credit_rect.x = creditX
            credit_rect.y = creditY
            screen.blit(label,(label_pos))
            screen.blit(credits, (creditX,creditY),credit_rect)
            screen.blit(credits,credit_rect)

        if(pygame.key.get_pressed()[pygame.K_UP] !=0):
            playerStartY -=12
            player_rect.y -=12
            if checkCollision(credit_rect,player_rect):
                credit_count +=1
                screen.blit(label,(label_pos))
                creditX = randint(0, screen_w-50)
                creditY = randint(0, screen_h-80)
                credit_rect.x = creditX
                credit_rect.y = creditY
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)
            
        if(pygame.key.get_pressed()[pygame.K_DOWN] !=0):
            playerStartY +=12
            player_rect.y +=12
            if checkCollision(credit_rect,player_rect):
                credit_count +=1
                screen.blit(label,(label_pos))
                creditX = randint(0, screen_w-50)
                creditY = randint(0, screen_h-80)
                credit_rect.x = creditX
                credit_rect.y = creditY
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)
            
        if(pygame.key.get_pressed()[pygame.K_LEFT] !=0):
            playerStartX -=12
            player_rect.x -=12
            if checkCollision(credit_rect,player_rect):
                credit_count +=1
                screen.blit(label,(label_pos))
                creditX = randint(0, screen_w-50)
                creditY = randint(0, screen_h-80)
                credit_rect.x = creditX
                credit_rect.y = creditY
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)
            
        if(pygame.key.get_pressed()[pygame.K_RIGHT] !=0):
            playerStartX +=12
            player_rect.x +=12
            if checkCollision(credit_rect,player_rect):
                credit_count +=1
                screen.blit(label,(label_pos))
                creditX = randint(0, screen_w-50)
                creditY = randint(0, screen_h-80)
                credit_rect.x = creditX
                credit_rect.y = creditY
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)

        if(pygame.key.get_pressed()[pygame.K_ESCAPE]):
            exit_game()

        
        screen.fill(background)
        screen.blit(playerPic, (playerStartX,playerStartY))
        screen.blit(label,label_pos)
        screen.blit(playerPic, player_rect)

        screen.blit(enemyPic,(enemyStartX,enemyStartY))
        screen.blit(enemyPic,enemy_rect)

        screen.blit(enemy2, (enemy2X,enemy2Y))
        screen.blit(enemy2,enemy2_rect)

        screen.blit(credits, (creditX,creditY),credit_rect)
        screen.blit(credits,credit_rect)
        screen.blit(label,label_pos)
        

        pygame.display.flip()


def exit_game():
    sys.exit()

welcome()
