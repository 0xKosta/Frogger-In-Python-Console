##MADE BY Buxx0-github.com/Buxx0###
###################################
###____####################___#####
##|  _ \                  / _ \ ###
##| |_) |_   ___  ____  _| | | |###
##|  _ <| | | \ \/ /\ \/ / | | |###
##| |_) | |_| |>  <  >  <| |_| |###
##|____/ \__,_/_/\_\/_/\_\\___/####
###################################
###################################



import random
import time
import keyboard
import os


######################
### MAIN FUNCTIONS ###
######################
def win_check(grid):
    for i in range(len(grid[0])):
        if grid[0][i] == player:
            return True
    return False

def enemy2_locations(grid):
    enemy2_coords = []
    for i in range(len(grid)):
        for k in range(len(grid[0])):
            if grid[i][k] == enemy2:
                enemy2_coords.append([i, k])
    return enemy2_coords

def enemy_locations(grid):
    enemy_coords = []
    for i in range(len(grid)):
        for k in range(len(grid[0])):
            if grid[i][k] == enemy:
                enemy_coords.append([i, k])
    return enemy_coords

def player_location(grid):
    for i in range(len(grid)):
        for k in range(len(grid[0])):
            if grid[i][k] == player:
                return i, k
    return 99,99

def enemy_move(enemy_coords, grid, frame):
    for i in range(len(enemy_coords)):
        if frame % 10 == 0:
            grid[enemy_coords[i][0]][enemy_coords[i][1]] = grass
            if enemy_coords[i][1] < 29:
                grid[enemy_coords[i][0]][enemy_coords[i][1]+1] = enemy
                enemy_coords[i][1] += 1
            else:
                grid[enemy_coords[i][0]][0] = enemy
                enemy_coords[i][1] = 0

def enemy2_move(enemy_coords, grid, frame):
    for i in range(len(enemy_coords)):
        if frame % 5 == 0:
            grid[enemy_coords[i][0]][enemy_coords[i][1]] = grass
            if enemy_coords[i][1] < 29:
                grid[enemy_coords[i][0]][enemy_coords[i][1]+1] = enemy2
                enemy_coords[i][1] += 1
            else:
                grid[enemy_coords[i][0]][0] = enemy2
                enemy_coords[i][1] = 0

def movement_handler(x, y, grid):
    if keyboard.is_pressed("up") and x > 0:
        if grid[x-1][y] == enemy:
            return True
        grid[x][y] = grass
        grid[x-1][y] = player
        return False
    elif keyboard.is_pressed("down") and x < 29:
        if grid[x+1][y] == enemy:
            return True
        grid[x][y] = grass
        grid[x+1][y] = player
        return False
    elif keyboard.is_pressed("left") and y > 0:
        if grid[x][y - 1] == enemy:
            return True
        grid[x][y] = grass
        grid[x][y - 1] = player
        return False
    elif keyboard.is_pressed("right") and y < 29:
        if grid[x][y + 1] == enemy:
            return True
        grid[x][y] = grass
        grid[x][y + 1] = player
        return False



def grid_draw(grid):
    for i in range(len(grid)):
        for k in range(len(grid[0])):
            print("" + str(grid[i][k]) , end = '')
        print()

############################################
### INITIALISATION FOR GRID AND ENTITIES ###
############################################

grass = "\u001b[32;1m██\u001b[0m"
player = "\u001b[34m▓▓\u001b[0m"
enemy = "\u001b[31m██\u001b[0m"
enemy2 = "\u001b[33m██\u001b[0m"


grid = [
[grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
[grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
[grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
[grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
[grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
[grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
[grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
[grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
[grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
[grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
[grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
[grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
[grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
[grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
[grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
[grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
[grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
[grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
[grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
[grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
[enemy2,grass,grass,grass,enemy2,grass,grass,grass,enemy2,grass,grass,grass,enemy2,grass,grass,grass,enemy2,grass,grass,grass,enemy2,grass,grass,grass,enemy2,grass,grass,grass,enemy2,grass],
[grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
[grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
[grass,grass,enemy,grass,grass,enemy,grass,grass,enemy,grass,grass,enemy,grass,grass,enemy,grass,grass,enemy,grass,grass,enemy,grass,grass,enemy,grass,grass,enemy,grass,grass,enemy],
[grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
[grass,enemy,grass,enemy,grass,enemy,grass,enemy,grass,enemy,grass,enemy,grass,enemy,grass,enemy,grass,enemy,grass,enemy,grass,enemy,grass,enemy,grass,enemy,grass,enemy,grass,enemy],
[grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
[enemy,grass,enemy,grass,enemy,grass,enemy,grass,enemy,grass,enemy,grass,enemy,grass,enemy,grass,enemy,grass,enemy,grass,enemy,grass,enemy,grass,enemy,grass,enemy,grass,enemy,grass],
[grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
[player,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass]
]


enemy_coords = enemy_locations(grid)
enemy2_coords = enemy2_locations(grid)
frame = 0
death = False
win = False
#################
### MAIN LOOP ###
#################

while not death and not win:
    os.system('cls')
    grid_draw(grid)
    player_x, player_y = player_location(grid)
    if player_x == 99 or player_y == 99:
        death = True
        break
    enemy2_move(enemy2_coords, grid, frame)
    enemy_move(enemy_coords,grid, frame)
    death = movement_handler(player_x, player_y, grid)
    win = win_check(grid)
    frame += 1
    time.sleep(0.016)
if death:
    print('''
       _____          __  __ ______    ______      ________ _____  
      / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
     | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
     | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
     | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
      \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\
    ''')
    print("Press ESC to close.")
    keyboard.wait("esc")
elif win:
    print('''
 __     ______  _    _  __          _______ _   _ _ 
 \ \   / / __ \| |  | | \ \        / /_   _| \ | | |
  \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| | |
   \   /| |  | | |  | |   \ \/  \/ /   | | | . ` | |
    | | | |__| | |__| |    \  /\  /   _| |_| |\  |_|
    |_|  \____/ \____/      \/  \/   |_____|_| \_(_)''')
    print("Press ESC to close.")
    keyboard.wait("esc")
