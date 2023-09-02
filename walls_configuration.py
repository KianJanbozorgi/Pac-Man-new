import pygame
import json
import sys
import os
file = open( "walls.json" , "r")
s = [1,2]
walls = json.load(file)
file.close()


wall_1 = pygame.Rect(walls["wall_1_json"])
wall_2 = pygame.Rect(walls["wall_2_json"])
wall_3 = pygame.Rect(walls["wall_3_json"])
wall_4 = pygame.Rect(walls["wall_4_json"])
wall_5 = pygame.Rect(walls["wall_5_json"])
wall_6 = pygame.Rect(walls["wall_6_json"])
wall_7 = pygame.Rect(walls["wall_7_json"])
wall_8 = pygame.Rect(walls["wall_8_json"])
wallss = [wall_1,wall_2,wall_3,wall_4,wall_5,wall_6,wall_7,wall_8]

