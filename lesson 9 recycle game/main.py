import pgzrun
import random

WIDTH = 800
HEIGHT = 600

START_SPEED = 10
ITEMS = ["bag","battery","bottle","chips"]

FINAL_LEVEL = 6
current_level = 1

game_over = False
game_complete = False

items = []
animations = []

def draw():
    global items, current_level, game_over, game_complete
    screen.clear()
    screen.blit("bground",(0,0))

    if game_over:
        display_message("GAME OVER","Try again")

    elif game_complete:
        display_message("WELL DONE","You won")

    else:
        for item in items:
            item.draw()

def display_message(heading,subheading):
    screen.draw.text(heading, fontsize = 60, center = (400,300), color = "black")
    screen.draw.text(subheading, fontsize = 30, center = (400,330), color = "black")

def update():
    global items
    if len(items) == 0:
        items = make_items(current_level)

#Make items
# get item from ITEMS list - random
#create actors and add to items list
# display items with equal spacing    
    





































pgzrun.go()
