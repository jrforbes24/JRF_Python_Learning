# Snake Tutorial

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object) :
    rows = 20
    w = 500
    def __init__(self,start,dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color        
        
    
    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
        
    def draw(self, surface, eyes=False):
        dis = self.w // self.rows 
        i = self.pos[0]
        j = self.pos[1]
        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2))
        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis - radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)          
            

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
                    self.turns.pop(p)    
            else:
              if cube.dirnx == -1 and cube.pos[0] <= 0: cube.pos = (cube.rows-1, cube.pos[1]) 
              elif cube.dirnx == 1 and cube.pos[0] >= cube.rows-1: cube.pos = (0, cube.pos[1])
              elif cube.dirny == 1 and cube.pos[1] >= cube.rows-1: cube.pos = (cube.pos[0], 0)
              elif cube.dirny == -1 and cube.pos[1] <= 0: cube.pos = (cube.pos[0], cube.rows-1)
              else: cube.move(cube.dirnx,cube.dirny)
    
    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1
    
    def addCube(self):
        tail = self.body[-1]
        dx = tail.dirnx
        dy = tail.dirny
        
        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1, tail.pos[1])))        
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0], tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0], tail.pos[1]+1)))
        
        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy
            
    def draw(self, surface):
        for i, cube in enumerate(self.body):
            if i == 0:
                cube.draw(surface, True)
            else:
                cube.draw(surface)
        
    
def drawGrid(w, rows, surface):
    sizeBtwn = w // rows
    
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
        
        pygame.draw.line(surface, (255, 255, 255), (x,0),(x,w))
        pygame.draw.line(surface, (255, 255, 255), (0,y),(w,y))
    
    
def redrawWindow(surface):
    global rows, width, snake, snack
    surface.fill((0, 0, 0))
    snake.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()
    pass

def randomSnack(rows, item):  
    positions = item.body
    
    while True:        
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions)))> 0:
            continue
        else:
            break
        
    return (x, y)
            

def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy
    except:
        pass

def main():
    global width, rows, snake, snack
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    snake = snake ((255, 0, 0), (10, 10))
    snack = cube(randomSnack(rows, snake), color=(0, 255, 0))
    flag = True
    
    clock = pygame.time.Clock()
    
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        snake.move()
        if snake.body[0].pos == snack.pos:
            snake.addCube()
            snack = cube(randomSnack(rows, snake), color=(0, 255, 0))
        
        for x in range(len(snake.body)):
            if snake.body[x].pos in list(map(lambda z:z.pos, snake.body[x+1:])):
                print('Score: ', len(snake.body))
                message_box('Game Over', 'Your score was: ' + str(len(snake.body)) + '. Play again ...')
                snake.reset((10,10))
                break
                
        
        redrawWindow(win)
                
        
   



main()








