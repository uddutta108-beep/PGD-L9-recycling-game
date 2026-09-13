import pgzrun
import random

WIDTH = 800
HEIGHT = 600

START_SPEED = 10
ITEMS = ["apple","pizza","fries","burger"]

FINAL_LEVEL = 6
current_level = 1

game_over = False
game_complete = False

items = []
animations = []

def draw():
    global items, current_level, game_complete, game_over

    screen.clear()
    screen.blit("bg",(0,0))

    if game_over:
        display_message("GAME OVER. Try again")

    elif game_complete:
        display_message("YOU WON")

    else:
        for item in items:
            item.draw()

def display_message(heading,subheading):
    screen.draw.text (heading, fontsize = 60, center = (400,300), color = "black")
    screen.draw.text (subheading, fontsize = 30, center = (400,330), color = "black" )

def update():
    global items
    if len(items) == 0:
        items = make_items(current_level)

def make_items(number_of_extra_items):
    items_to_create = get_option_to_create(number_of_extra_items)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_option_to_create(number_of_extra_items):
    items_to_create = ["apple"]
    for i in range(0,number_of_extra_items):
        item = random.choice(ITEMS)
        items_to_create.append(item)
    return items_to_create

def create_items(items_to_create):
    new_items = []
    for i in items_to_create:
        item = actor(i)
        new_items.nd(item)
    return new_items

def layout_items(new_items):
    gaps = len(new_items) + 1
    gap_size = WIDTH / gaps
    random.shuffle(new_items)

    for index, item in enumerate(new_items):
        x = (index + 1) * gap_size
        item.x = x

def animate_items(new_items):
    global animations
    for item in new_items:
        duration = START_SPEED - current_level
        animation = animate(item,duration=duration, on_finished=handle_game_over, y=HEIGHT)
        animations.append(animation)

pgzrun.go()