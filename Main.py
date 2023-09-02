import pygame
import sys
import os
from pygame.locals import *
import json
from walls_configuration import wallss
from lines_configuration import lines
import image
import random


pygame.init()
n = 12
z1 , z2 , z3 , z4 = 0 , 0 , 0 , 0
z5 , z6 , z7 , z8 = 0 ,0 , 0 , 0
z9 , z10 , z11 ,z12 = 0, 0 ,0 ,0
dis_x = 500
dis_y = 500
dis = pygame.display.set_mode((dis_x, dis_y))
pygame.display.set_caption('Pac-Man!')
pygame.display.update()
clock = pygame.time.Clock()
red = (255, 0, 0)
black = (0, 0, 0)
green = (0,255,0)
transparent= (0,0,0,0)
file = open("cherry.json" , "r")
cherrys = json.load(file)
file.close

x_change, y_change = 0, 0

x_change_sprite = 0
y_change_sprite = 0
x_change_sprite2 = 0
y_change_sprite2 = 0
pygame.mixer.init()
pygame.mixer.music.load("pacman.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

player_pos = [100, 70]
sprite1_pos = [250 , 250]
sprite2_pos = [100 , 400]
cherry1_rect = image.cherry1.get_rect(topleft = cherrys["cherry1"] )
cherry2_rect =image.cherry2.get_rect(topleft = cherrys["cherry2"] )
cherry3_rect = image.cherry3.get_rect(topleft = cherrys["cherry3"] )
cherry4_rect = image.cherry4.get_rect(topleft = cherrys["cherry4"] )
cherry5_rect = image.cherry5.get_rect(topleft = cherrys["cherry5"] )
cherry6_rect = image.cherry6.get_rect(topleft = cherrys["cherry6"] )
cherry7_rect = image.cherry7.get_rect(topleft = cherrys["cherry7"] )
cherry8_rect = image.cherry8.get_rect(topleft = cherrys["cherry8"] )
cherry9_rect = image.cherry9.get_rect(topleft = cherrys["cherry9"] )
cherry10_rect = image.cherry10.get_rect(topleft = cherrys["cherry10"] )
cherry11_rect = image.cherry11.get_rect(topleft = cherrys["cherry11"] )
cherry12_rect = image.cherry12.get_rect(topleft = cherrys["cherry12"] )

cherrys_rect = [cherry1_rect,cherry2_rect,cherry3_rect,cherry4_rect
                ,cherry5_rect,cherry6_rect,cherry7_rect,cherry8_rect,
            cherry9_rect,cherry10_rect ,cherry11_rect ,cherry12_rect]



game = True


while game:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        
        
      

        if event.type == pygame.KEYDOWN:  # Event: Key pressed
            if event.key == pygame.K_LEFT:
                x_change = -7
                y_change = 0
                player_pos[0] = player_pos[0] + x_change
                player_pos[1] = player_pos[1] + y_change
                

            elif event.key == pygame.K_RIGHT:
                x_change = 7
                y_change = 0
                player_pos[0] = player_pos[0] + x_change
                player_pos[1] = player_pos[1] + y_change
            elif event.key == pygame.K_UP:
                x_change = 0
                y_change = -7
                player_pos[0] = player_pos[0] + x_change
                player_pos[1] = player_pos[1] + y_change
            elif event.key == pygame.K_DOWN:
                x_change = 0
                y_change = 7
                player_pos[0] = player_pos[0] + x_change
                player_pos[1] = player_pos[1] + y_change


    

    if player_pos[0] > sprite1_pos[0] :
        x_change_sprite = 1
       
        if player_pos[0]-4 < sprite1_pos[0] < player_pos[0]+4 :
            x_change_sprite = 0
            
    if player_pos[0] < sprite1_pos[0] :
        x_change_sprite = -1
        
        if player_pos[0]-4 < sprite1_pos[0] < player_pos[0]+4 :
            x_change_sprite = 0
           
            
    if player_pos[1] < sprite1_pos[1] :
        
        y_change_sprite = -1
        if player_pos[1]-4 < sprite1_pos[1] < player_pos[1]+4 :
            
            y_change_sprite = 0
    if player_pos[1] > sprite1_pos[1] :
        
        y_change_sprite = 1
        if player_pos[1]-4 < sprite1_pos[1] < player_pos[1]+4 :
                
            y_change_sprite = 0

   


    if player_pos[0] > sprite2_pos[0] :
        x_change_sprite2 = random.randint(0,2)
       
        if player_pos[0]-4 < sprite2_pos[0] < player_pos[0]+4 :
            x_change_sprite2 = 0
           
    if player_pos[0] < sprite2_pos[0] :
        x_change_sprite2 = random.randint(-2 , 0)
        
        if player_pos[0]-4 < sprite2_pos[0] < player_pos[0]+4 :
            x_change_sprite2 = 0
          
            
    if player_pos[1] < sprite2_pos[1] :
       
        y_change_sprite2 = random.randint(-2,0)
        if player_pos[1]-4 < sprite2_pos[1] < player_pos[1]+4 :
            
            y_change_sprite2 = 0
    if player_pos[1] > sprite2_pos[1] :
        
        y_change_sprite2 = random.randint(0,2)
        if player_pos[1]-4 < sprite2_pos[1] < player_pos[1]+4 :
           
            y_change_sprite2 = 0

   

# ino mishe class kard
    
    if player_pos[0] < 0 :
        player_pos[0] = dis_x
    if player_pos[0] > dis_x :
        player_pos[0] = 0
    if player_pos[1] < 0 :
        player_pos[1] = dis_y
    if player_pos[1] > dis_y :
        player_pos[1] = 0
    

    if sprite1_pos[0] < 0 :
        sprite1_pos[0] = dis_x
    if sprite1_pos[0] > dis_x :
        sprite1_pos[0] = 0
    if sprite1_pos[1] < 0 :
        sprite1_pos[1] = dis_y
    if sprite1_pos[1] > dis_y :
        sprite1_pos[1] = 0

    if sprite2_pos[0] < 0 :
        sprite2_pos[0] = dis_x
    if sprite2_pos[0] > dis_x :
        sprite2_pos[0] = 0
    if sprite2_pos[1] < 0 :
        sprite2_pos[1] = dis_y
    if sprite2_pos[1] > dis_y :
        sprite2_pos[1] = 0
    dis.fill(black)
      
    
    player_rect = image.player.get_rect(topleft = player_pos)
    if any (player_rect.colliderect(w) for w in wallss):
        
        x_change = 0
        y_change = 0
        player_pos = list(prev_pos)
    
   

    player_rect = image.player.get_rect(topleft = player_pos)    
    if any (player_rect.clipline(w) for w in lines) : 
        x_change = 0
        y_change = 0
        player_pos = list(prev_pos)
    sprite1_rect = image.sprite1.get_rect(topleft = sprite1_pos)
    if player_rect.colliderect(sprite1_rect) :
       

        pygame.quit()
        while True :
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load("gameover.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play()
        
            dis = pygame.display.set_mode((300, 300))
            pygame.display.set_caption('Gameover')
            gameover = pygame.image.load("gameover.png")
            gameover_pos = [20 , 20 ]
            dis.blit(gameover , gameover_pos)
            pygame.display.update()
            while True :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()

        
    sprite2_rect = image.sprite2.get_rect(topleft = sprite2_pos)
    if player_rect.colliderect(sprite2_rect) :
        pygame.quit()
        while True :
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load("gameover.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play()
            dis = pygame.display.set_mode((300, 300))
            pygame.display.set_caption('Gameover')
            gameover = pygame.image.load("gameover.png")
            gameover_pos = [20 , 20 ]
            dis.blit(gameover , gameover_pos)
            pygame.display.update()
            while True :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
    for c in cherrys_rect :
        if player_rect.colliderect(c) :
            
            if c is cherry12_rect :
                z12 = 12
            if c is cherry11_rect :
                z11 = 11
            if c is cherry10_rect :
                z10 = 10
            if c is cherry9_rect :
                z9 = 9
            if c is cherry8_rect :
                z8 = 8
            if c is cherry7_rect :
                z7 = 7
            if c is cherry6_rect :
                z6 = 6
            if c is cherry5_rect :
                z5 = 5
            if c is cherry4_rect :
                z4 = 4
            if c is cherry3_rect :
                z3 = 3
            if c is cherry2_rect :
                z2 = 2
            if c is cherry1_rect :
                z1 = 1
            n = n-1
            i = player_pos
            player_pos = list(prev_pos)
           
            
            
            # pygame.display.update()
            cherrys_rect.remove(c)
            if n == 0 :
                pygame.quit()
                while True :
                    pygame.init()
                    pygame.mixer.init()
                    pygame.mixer.music.load("victory.mp3")
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play()
                    dis = pygame.display.set_mode((300, 300))
                    pygame.display.set_caption('Victory')
                    victory = pygame.image.load("victory.png")
                    victory_pos = [20 , 20 ]
                    dis.blit(victory , victory_pos)
                    pygame.display.update()
                    while True :
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                 quit()


    
         
    prev_pos = list(player_pos)
    player_pos[0] = player_pos[0] + x_change
    player_pos[1] = player_pos[1] + y_change

    sprite1_pos[0] = sprite1_pos[0] + x_change_sprite
    sprite1_pos[1] = sprite1_pos[1] + y_change_sprite
    sprite2_pos[0] = sprite2_pos[0] + x_change_sprite2
    sprite2_pos[1] = sprite2_pos[1] + y_change_sprite2



    dis.blit(
        image.cherry1 , cherrys["cherry1"])
    dis.blit( 
        image.cherry2, cherrys["cherry2"])
    dis.blit(
        image.cherry3 , cherrys["cherry3"])
    dis.blit(
        image.cherry4 , cherrys["cherry4"])
    dis.blit(
        image.cherry5 , cherrys["cherry5"])
    dis.blit(
        image.cherry6 , cherrys["cherry6"])
    dis.blit(
        image.cherry7 , cherrys["cherry7"])
    dis.blit(
        image.cherry8 , cherrys["cherry8"])
    dis.blit(
        image.cherry9 , cherrys["cherry9"])
    dis.blit(
        image.cherry10 , cherrys["cherry10"])
    dis.blit(
        image.cherry11 , cherrys["cherry11"])
    dis.blit(
        image.cherry12 , cherrys["cherry12"])
    
    
    if z12 == 12 :
        pygame.draw.rect(dis, transparent , [  455,235  , 30 , 30 ] )
    if z11 == 11 :
        pygame.draw.rect(dis, transparent , [  22, 235 , 30 , 30 ] )
    if z10 == 10 :
        pygame.draw.rect(dis, transparent , [ 210 , 270 , 30 , 30 ] )
    if z9 == 9 :
        pygame.draw.rect(dis, transparent, [ 270 , 270 , 30 , 30 ] )
    if z8 == 8 :
        pygame.draw.rect(dis, transparent , [ 270 , 210 , 30 , 30 ] )
    if z7 == 7 :
        pygame.draw.rect(dis, transparent , [ 210 , 210 , 30 , 30 ] )
    if z6 == 6 :
        pygame.draw.rect(dis, transparent , [ 23 , 22 , 30 , 30 ] )    
    if z5 == 5 :
        pygame.draw.rect(dis, transparent , [  250,  22, 30 , 30 ] )
    if z4 == 4 :
        pygame.draw.rect(dis, transparent , [ 450 , 20 , 30 , 30 ] )
    if z3 == 3 :
        pygame.draw.rect(dis, transparent , [ 450 , 450 , 30 , 30 ] )
    if z2 == 2 :     
        pygame.draw.rect(dis, transparent , [ 22 ,450 , 30 , 30 ] )
    if z1 == 1 :
        pygame.draw.rect(dis, transparent, [ 220 , 450 , 30 , 30 ] )
    
    dis.blit(image.sprite2 , sprite2_pos)
    dis.blit(image.sprite1 , sprite1_pos)
    dis.blit(image.player, player_pos)
    
    pygame.draw.rect(dis, green , wallss[-2] ) 
    pygame.draw.rect(dis, green , wallss[-1] )
    pygame.draw.line(dis, green , (dis_x,200),(300,80) , 20 )
    pygame.draw.line(dis, green , (0,200),(200,80) , 20 )
    pygame.draw.line(dis, green , (dis_x,300),(300,420) , 20 )
    pygame.draw.line(dis, green , (0,300),(200,420) , 20 )
    pygame.draw.rect(dis, green , wallss[5] )
    pygame.draw.rect(dis, green ,  wallss[2] )
    pygame.draw.rect(dis, green , wallss[4] )
    pygame.draw.rect(dis, green , wallss[3] )
    pygame.draw.rect(dis, green , wallss[1] )
    pygame.draw.rect(dis, green , wallss[0] )
    
    
   
    
    pygame.display.update()
    
    clock.tick(20)

pygame.quit()

quit()
