import sys
sys.path.append('..')
import keyboard
import time
import os
os.system('mode con: cols=202 lines=60')
import land

current_map = land.main_map()
 
def print_land():
    for i in current_map:
        print (i)
def shift_up():
    y = current_map[0]
    current_map = current_map[1:]
    current_map.append(y)
def shift_down():
    y = current_map[len(current_map) - 1]
    current_map = current_map[:len(current_map) - 1]
    current_map.insert(0, y)



while True:
    print_land()
    
    if keyboard.is_pressed('s'):
        y = current_map[0]
        current_map = current_map[1:]
        current_map.append(y)
        
    if keyboard.is_pressed('w'):
        y = current_map[len(current_map) - 1]
        current_map = current_map[:len(current_map) - 1]
        current_map.insert(0, y)
        
    if keyboard.is_pressed('d'):
        for index, i in enumerate(current_map):
            x = list(i)
            y = x[0]
            x = x[1:]
            x.append(y)
            x = ''.join(x)
            current_map[index] = x
    if keyboard.is_pressed('a'):
        for index, i in enumerate(current_map):
            x = list(i)
            y = x[len(i) - 1]
            x = x[:len(i) - 1]
            x.insert(0, y)
            x = ''.join(x)
            current_map[index] = x
    
    os.system('cls')
