#!/usr/bin/env python3
import random
import time
import os
import sys
import time
from time import sleep
import drive_gyro
import moveShovel
import playMusic
import drive_gyro
from ev3dev2.motor import LargeMotor, OUTPUT_C
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from threading import Thread
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2
# from ev3dev2.motor import LargeMotor, OUTPUT_D, OUTPUT_B, SpeedPercent, MoveTank

# state constants
ON = True
OFF = False

from drive import *
from moveShovel import *
from playMusic import *
from robot import Robot
from sweeper import Sweeper
from dfs_sweeper import DFSSweeper

def debug_print(*args, **kwargs):
    '''Print debug messages to stderr. This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)

def reset_console():
    '''Resets the console to the default state'''
    print('\x1Bc', end='')

def set_cursor(state):
    '''Turn the cursor on or off'''
    if state:
        print('\x1B[?25h', end='')
    else:
        print('\x1B[?25l', end='')

def set_font(name):
    '''Sets the console font. A full list of fonts can be found with `ls /usr/share/consolefonts`
    '''
    os.system('setfont ' + name)


def random_matrix(no_rows, no_cols, no_obs):
    arr = []
    for i in range(no_rows * no_cols):
        if i < no_obs:
            arr.append(1)
        else:
            arr.append(0)

    random.shuffle(arr)

    start_position = {'x': 0, 'y': 0}
    rand_pos = random.randint(0, no_rows * no_cols - no_obs - 1)

    matrix = []
    count = 0
    for i in range(no_rows):
      matrix.append(row)
    return matrix, start_position

def fixed_matrix(no_rows, no_cols, no_obs):
    arr = []
    for i in range(no_rows * no_cols):
        if i < no_obs:
            arr.append(1)
        else:
            arr.append(0)

    random.Random(4).shuffle(arr)

    start_position = {'x': 0, 'y': 0}
    rand_pos = random.Random(4).randint(0, no_rows * no_cols - no_obs - 1)

    matrix = []
    count = 0
    for i in range(no_rows):
        row = []
        for j in range(no_cols):
            row.append(arr[i * no_cols + j])
            if arr[j] == 0:
                if count == rand_pos:
                    start_position = {'x': j, 'y': i}
                count += 1
        matrix.append(row)
    return matrix, start_position

def custom_map(no_rows, no_cols, no_obs):
    arr = []
    for i in range(no_rows * no_cols):
        if i < 0:
            arr.append(1)
        else:
            arr.append(0)

    #define position of obstacles
    #main demo
    arr[6] = 1
    arr[13] = 1
    #arr[18] = 1

    start_position = {'x': 0, 'y': 0}
    rand_pos = 8

    matrix = []
    count = 0
    for i in range(no_rows):
        row = []
        for j in range(no_cols):
            row.append(arr[i * no_cols + j])
            # if arr[i * no_cols + j] == 0:
            if count == rand_pos:
                start_position = {'x': j, 'y': i}
            count += 1
        matrix.append(row)
    return matrix, start_position


def main():
    no_rows = 3
    no_cols = 5
    no_obs = 2
    no_matrix = 1

    total_elapsed_bfs = 0
    total_steps_bfs = 0
    total_turns_bfs = 0

    total_elapsed_dfs = 0
    total_steps_dfs = 0
    total_turns_dfs = 0

    for i in range(no_matrix):
        ''' Initialize Matrix, robot and start position '''
        ############ HERE Add initialization of EV3
       

        print("[INFO] Initialising Matrix...")
        debug_print("[INFO] Initialising Matrix...")
        #matrix, start_position = random_matrix(no_rows, no_cols, no_obs)
        #matrix, start_position = fixed_matrix(no_rows, no_cols, no_obs)
        matrix, start_position = custom_map(no_rows, no_cols, no_obs)
        start_direction = random.Random(4).randint(0, 3)

        print("[INFO] Initialising Robot and Sweeper...")
        debug_print("[INFO] Initialising Robot and Sweeper...")
        # initialise robot
        shovel = moveShovel.Shovel()
        music = playMusic.Music()
        music.playMusic()
        diffRobot = drive_gyro.Drive_gyro(shovel)

        print("[INFO] Initialising the respective Algorithm...")
        debug_print("[INFO] Initialising the respective Algorithm...")
        #algo = "dfs"
        algo = "bfs"

        robot = Robot(matrix, start_position, start_direction, diffRobot, shovel, algo)
        robot.log()

        #sweeper = DFSSweeper(robot)
        sweeper = Sweeper(robot)

        sweeper.loggable = False
        robot.loggable = True

        print("[INFO] Starting DFS sweep...")
        debug_print("[INFO] Starting DFS sweep...")

        start = time.time()
        sweeper.sweep()
        elapsed = time.time() - start

        print("[INFO] Finished DFS sweep...")
        debug_print("[INFO] Finished DFS sweep...")

        #print("[INFO] Move to home position...")
        #debug_print("[INFO] Move to home position...")

        #x_move = start_position['x']-sweeper.current_position['x']
        #y_move = start_position['y'] - sweeper.current_position['y']

        'move robot to correct x position'
        #debug_print('move robot to x position')
        #if x_move > 0:
        #    left_turns = 0 - sweeper.current_direction
        #    current = 0
        #elif x_move < 0:
        #    left_turns = 2 - sweeper.current_direction
        #    current = 2

        #if left_turns < 0:
        #    left_turns += 4
        #    debug_print('keine drehung notwendig')
        #if left_turns == 3:
        #    debug_print('roboter dreht sich einmal nach rechts')
               #bewege roboter 1x nach rechts
        #    diffRobot.turn_right()
        #else:
        #    for i in range(left_turns):
        #        debug_print('roboter nach links')
               #bewege roboter entsprechend oft nach links
        #        diffRobot.turn_left()

        #debug_print('so viele schritte macht der roboter')
        #for steps in range(abs(x_move)):
        #    debug_print(steps)
            #bewege den roboter jeweils eins nach vorne
        #    diffRobot.driveGyro(10)

        #'move robot to correct y position'
        #debug_print('move robot zu y position')
        #if y_move > 0:
        #    left_turns = 3 - current
        #elif y_move < 0:
        #    left_turns = 1 - current

        #if left_turns < 0:
        #    left_turns += 4
        #    debug_print('keine drehung notwendig')
        #if left_turns == 3:
        #    debug_print('bewege einmal nach links')
            # bewege roboter 1x nach rechts
        #    diffRobot.turn_right()
        #else:
        #    for i in range(left_turns):
        #        debug_print('bewege roboter nach links')
                # bewege roboter entsprechend oft nach links
        #        diffRobot.turn_left()

        #print('so viele schritte macht der roboter')
        #for steps in range(abs(y_move)):
        #    debug_print(steps)
            #bewege den roboter jeweils eins nach vorne
        #    diffRobot.driveGyro(10)

        total_elapsed_dfs += elapsed
        total_steps_dfs += robot.move_count
        total_turns_dfs += robot.turn_count

        print('steps taken by dfs: %d, turns taken: %d, time taken: %.2fms'
              % (robot.move_count, robot.turn_count, elapsed * 1000))

        # run with bfs
        #print("[INFO] Starting BFS sweep...")
        #debug_print("[INFO] Starting BFS sweep...")
        
        #robot = Robot(matrix, start_position, start_direction, diffRobot)
        #sweeper = Sweeper(robot)
        #sweeper.loggable = False
        #robot.loggable = True

        #start = time.time()
        #sweeper.sweep()
        #elapsed = time.time() - start

        #total_elapsed_bfs += elapsed
        #total_steps_bfs += robot.move_count
        #total_turns_bfs += robot.turn_count

        #print('steps taken by planned bfs: %d, turns taken: %d, time taken: %.2fms'
        #      % (robot.move_count, robot.turn_count, elapsed * 1000))

        # sweeper.print_map()
        # robot.log()

    print('DFS: average steps taken: %d, turns taken: %d, time taken: %.2fms'
         % (int(total_steps_dfs / no_matrix), int(total_turns_dfs / no_matrix), total_elapsed_dfs * 1000 / no_matrix))

    print('Planned BFS: average steps taken: %d, turns taken: %d, time taken: %.2fms'
         % (int(total_steps_bfs / no_matrix), int(total_turns_bfs / no_matrix), total_elapsed_bfs * 1000 / no_matrix))
    music.playMusic()
    
if __name__ == '__main__':
    # set the console just how we want it
    reset_console()
    set_cursor(False)
    set_font('Lat15-Terminus24x12')
    main()
    # shovel = moveShovel.Shovel()
    # drive = drive_gyro.Drive_gyro(shovel)
    # drive.test()
