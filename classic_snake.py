from asyncio import Event
import math 
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube (object):
    rows=20
    w=500
    def __init__(self, start, dirnx=1,dirny=0, color=(255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color= color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos(self.pos[0]+self.dirnx, self.pos[1]+self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.w// self.rows
        i= self.pos[0]
        j= self.pos[1]

        pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2))

        if eyes:
            center = dis//2
            radius= 3
            circle_middle = (i*dis+center-radius, j*dis+8)
            circle2_middle = (i*dis+dis-radius*2, j*dis+8)

            pygame.draw.circle(surface,(0,0,0), circle_middle, radius)
            pygame.draw.circle(surface, (0,0,0), circle2_middle, radius)

class snake(object):
    body=[]
    turns={}

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move_snake(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx= -1
                    self.dirny= 0
                    self.turns[self.head.pos[:]]= [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx= 1
                    self.dirny= 0
                    self.turns[self.head.pos[:]]= [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx= 0
                    self.dirny= -1
                    self.turns[self.head.pos[:]]= [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx= 0
                    self.dirny= 1
                    self.turns[self.head.pos[:]]= [self.dirnx, self.dirny]

        
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)

                else:
                    if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                    elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0, c.pos[1])
                    elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                    elif c.dirny == -1 and c.pos[1] <= 0: c.po = (c.pos[0], c.rows-1)
                    else: c.move(c.dirnx, c.dirny)

    def reset(self, pos):
        pass

    def add_cube(self):
        pass

    def draw_snake(self, surface):
        for i, c in enumerate(self.body):
            if i==0:
                c.draw(surface, True)
            else:
                c.draw(surface)


def draw_grid (w,rows, surface):
    size_btw= w// rows                                               #gap between the grids

    x=0
    y=0
    for l in range(rows):
        x= x + size_btw
        y= y + size_btw

        pygame.draw.line(surface, (255,255,255), (x,0), (x,w))     #drawing line with pygame (this line is drawing vertical)
        pygame.draw.line(surface, (255,255,255), (0,y), (w,y))     #going to draw two lines every for loop (this line is drawing horizontal)

def redraw_window(surface):
    global width, rows, s
    width=500
    rows=20
    
    surface.fill((0,0,0))
    s.draw_snake(surface)
    draw_grid(width, rows, surface)
    pygame.display.update()

def random_snack(rows,items):
    pass

def message_box(subject, content):
    pass

def main():
    global width, rows, s
    width=500
    height=500
    rows=20
    win = pygame.display.set_mode((width, height))
    s = snake((255,0,0), (10,10))                   #color and position paramenters for snake
    flag = True

    clock= pygame.time.Clock()                      #makes sure that the game doesn't run more than 10 frames a second/ snake would be able to move 10 blocks in 1s.
    while flag:
        pygame.time.delay(50)                       #delay the program by 50 ms so that the program doesn't run too fast
        clock.tick(10)                              #lower the value in time.delay()--> faster the game, lower the no.in clock.tick()--> slower the game
        redraw_window(win)


main()