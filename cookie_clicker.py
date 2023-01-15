from random import randint
import time
import pygame

HEIGHT = 1010
WIDTH = 1850
punkty = 0
color = (0, 0, 0)
randomx = 255
randomy = 255
bok = 50

def narysuj_kwadrat(punkt_poczatkowy):
    #global bok
    wymiar = (bok, bok)
    prostokat = Rect(punkt_poczatkowy, wymiar)
    screen.draw.rect(prostokat, color=(255, 0, 0))
    screen.draw.text(f"punkty:{punkty}",top=10, left=250)

def czy_trafilismy(x, y):

    if x < randomx:    
        return False

    if y < randomy:
        return False
    
    if x > randomx + bok:
        return False

    if y > randomy + bok:
        return False

    return True


def on_key_down(key):
    global randomx
    global randomy
    global punkty
    
    if key == keys.SPACE:
        print("radio maryja")
        x, y = pygame.mouse.get_pos()
        if czy_trafilismy(x, y):
            punkty = punkty + 1
        else:
            print("ty durniu")
    
        randomy = randint(0, HEIGHT - bok)
        randomx = randint(0, WIDTH - bok)




def draw():
    screen.fill(color)
    narysuj_kwadrat((randomx, randomy))
   
    