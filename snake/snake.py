# Snake Tutorial

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object) :
    rows = 0
    w = 0
    def __init__(self,start,dirnx=1, dirny=0, color=(255, 0, 0)):
        pass
    def move(self, dirnx, dirny):
        pass
    def draw(self, surface, eyes=False):
        pass

class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1
        
    
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            keys = pygame.key.get_pressed()
            
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    
                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    
                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    
                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        
        # Enumerate over the cubes in the body list            
        for i, cube in enumerate(self.body):
            # Get the position of the cube
            p = cube.pos[:]
            # If the position is in the dictionary of turns 
            if p in self.turns:
                # Get the turn from the turns dictionary
                turn = self.turns[p]
                # Call the move function with the turn
                cube.move(turn[0], turn[1])
                # If the index is the end of the body list, remove the turn from the list
                if i == len(self.body)-1:
                    self.turns.pop()    
            
    
    def reset(self, pos):
        pass
    
    def addCube(self):
        pass
    
    def draw(self, surface):
        pass
    
def drawGrid(w, rows, surface):
    sizeBtwn = w // rows
    
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
        
        pygame.draw.line(surface, (255, 255, 255), (x,0),(x,w))
        pygame.draw.line(surface, (255, 255, 255), (0,y),(w,y))
    pass

def redrawWindow(surface):
    global rows, width
    surface.fill((0, 0, 0))
    drawGrid(width, rows, surface)
    pygame.display.update()
    pass

def randomSnack(rows, items):
    pass

def message_box(subject, content):
    pass

def main():
    global width, rows
    width = 600
    rows = 30
    win = pygame.display.set_mode((width, width))
    s = snake ((255, 0, 0), (10, 10))
    flag = True
    
    clock = pygame.time.Clock()
    
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(win)        
        
    pass



main()








