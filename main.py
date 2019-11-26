#!/usr/bin/env python3
'''Hello to the world from ev3dev.org'''

import os
import sys
import time
import drive
import moveShovel
import playMusic
from ev3dev2.motor import LargeMotor, OUTPUT_C
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM

# from ev3dev2.motor import LargeMotor, OUTPUT_D, OUTPUT_B, SpeedPercent, MoveTank

# state constants
ON = True
OFF = False


def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.

    This shows up in the output panel in VS Code.
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
    '''Sets the console font

    A full list of fonts can be found with `ls /usr/share/consolefonts`
    '''
    os.system('setfont ' + name)


def main():
    '''The main function of our program'''

    # set the console just how we want it
    #reset_console()
    #set_cursor(OFF)
    #set_font('Lat15-Terminus24x12')

    # print something to the screen of the device
    #print('Hello World!')

    # print something to the output panel in VS Code
    debug_print('Hello VS Code!')

    # wait a bit so you have time to look at the display before the program
    # exits
    time.sleep(1)

<<<<<<< HEAD
    #robot = drive.DiffRobot()
    #robot.go_forward()
    shovel = moveShovel.Shovel()
    shovel.moveShovel()
    time.sleep(1)
    
<<<<<<< HEAD
=======
    robot = drive.DiffRobot()
    #print(robot.motors)
    #robot.go_forward()
>>>>>>> changes in drive

    #time.sleep(1)

    #robot.turn_left()

    #time.sleep(1)

    robot.go_backwards():

    
=======
    music = playMusic.Music()
    music.playMusic()
>>>>>>> play Music funtion (important)

    #debug_print('Test')
    

    time.sleep(5) 


if __name__ == '__main__':
    main()
