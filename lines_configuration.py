import pygame
import json
import sys
import os

file = open("lines.json" , "r")
line = json.load(file)
file.close()

wall_9 = line["wall_9"]
wall_10 = line["wall_10"]
wall_11 = line["wall_11"]
wall_12 = line["wall_12"]

lines = [wall_9,wall_10,wall_11,wall_12]