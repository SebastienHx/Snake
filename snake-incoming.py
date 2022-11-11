import keyboard
import numpy as np
from time import time
from time import sleep
import os
import random
field = np.empty((18,18), dtype=str)
field = np.full_like(field, " ", dtype=str)
for i in range(18):
    field[0][i] = "#"
    field[i][0] = "#"
    field[-1][i] = "#"
    field[i][-1] = "#"

"""pos_x = 10
pos_y = 10
positions= [(pos_x, pos_y)]
apple = "o"
debut = time()
manger = False
apple_y = 7
apple_x = 3
compteur = 0
field[apple_y][apple_x] = apple
heading ='d'"""
debut = time()
compteur = [0]
def mouvement(pos_x, pos_y, positions, apple_x, apple_y):
    if pos_x > 16 or pos_x < 1 or pos_y > 16 or pos_y < 1:
        mort(debut)
        return(False)        
        #compteur += 1

    if (pos_x, pos_y) in positions:
        mort(debut)
        return(False)
    positions.append((pos_x, pos_y))
    field[positions[0][1]][positions[0][0]] = " "
    del(positions[0])

    if pos_x == apple_x and pos_y == apple_y:
        positions.append((pos_x, pos_y))
        apple_y = random.randrange(2,16)
        apple_x = random.randrange(2,16)
        apple = (apple_y, apple_x)
        compteur[0] += 1
        while apple in positions:
            apple_y = random.randrange(2,16)
            apple_x = random.randrange(2,16)
            apple = (apple_y, apple_x)
        field[apple_y][apple_x] = "o"
    return(apple_y, apple_x)

def mort(debut):
    fin = time()
    os.system("cls")
    print(f"Vous êtes mort! Vous avez survécu : {fin-debut} secondes! ( avec {compteur[0]} point(s)! d'accumulés!) ")
    while(True):
        sleep(10)

def gameplay():

    pos_x = 10
    pos_y = 10
    positions= [(pos_x, pos_y)]
    apple_y = 7
    apple_x = 3
    field[apple_y][apple_x] = "o"
    heading ='u'
    apple = (apple_y, apple_x)
    while(True):
        #print(debut)
        
        print(positions)
        print(apple_x, apple_y)
        for i in range(len(positions)):
            field[positions[i][1]][positions[i][0]] = "@"
        field[apple_y][apple_x] = "o"
        print(field)
        
        sleep(1/12)
        os.system("cls")

        if keyboard.is_pressed("w") or heading == 'w':
            pos_y -= 1
            apple = mouvement(pos_x,pos_y, positions, apple_x, apple_y)
            heading = 'w'

        if keyboard.is_pressed("s") or heading == 's':
            pos_y += 1
            apple = mouvement(pos_x,pos_y, positions, apple_x, apple_y)
            heading = 's'

        if keyboard.is_pressed("d") or heading == 'd':
            pos_x += 1
            apple = mouvement(pos_x,pos_y, positions, apple_x, apple_y)
            heading = 'd'

        if keyboard.is_pressed("a") or heading == 'a':
            pos_x -= 1
            apple =mouvement(pos_x,pos_y, positions, apple_x, apple_y)
            heading = 'a'
        apple_x, apple_y = apple[1], apple[0]
gameplay()
