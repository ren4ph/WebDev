import random as rd
import pygame as pg
import time, sys, os

display = pg.display()
display.title("Platformer")


while True:

    for event in pg.events:
        if event == pg.events.EXIT:
            break

    pg.display.update()

sys.exit()
