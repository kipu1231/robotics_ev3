#!/usr/bin/env python3
'''Hello to the world from ev3dev.org'''

import os
import sys
import time
from time import sleep
import drive
import moveShovel
import playMusic
from ev3dev2.motor import LargeMotor, OUTPUT_C
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from threading import Thread
import drive_gyro
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

    drive = drive_gyro.Drive_gyro()
    drive.turnRight_Gyro()
    #drive.turnLeft_Gyro()
    drive.driveGyro()
    #robot = drive.DiffRobot()
    #shovel = moveShovel.Shovel()
    #print(robot.motors)
    #while True:
     # robot.go_forward()
      #shovel.moveShovel()
      #time.sleep(5)

  
      
      
      
    #robot.turn_left()

    #time.sleep(1)

    # Run the robot until a button is pressed.
    #robot.start()
    # while not btn.any():   NOT WORKING
    # while True:    # Stop program with Ctrl-C
    #     # Infrared sensor in proximity mode will measure distance to the closest
    #     # object in front of it.
    #     distance = robot.infrared.value()
    #     distance_side = robot.infrared_side.value()
    #     dc_turn = 0
    #     dc = 0

    #     if distance_side < 100:
    #         dc = 0
    #         dc_turn = 80
         
    #     elif distance > 200:
    #         # Path is clear, run at full speed.
    #         dc = 90
    #         dc_turn = 0
    #     elif distance < 150:
    #         dc = 0
    #         dc_turn = 80
    #     else:
    #         # Obstacle ahead, slow down.
    #         dc = 40
    #         dc_turn = 0

    #     for m in robot.motors:
    #         robot.go_forward(distance=None, dc=dc)
            
    #         if dc_turn > 0:
    #             robot.go_forward(distance=None, dc=dc)
    #             robot.turn_right(angle=None, dc=dc_turn)
            
    #         #m.speed_sp = dc
    #         #m.duty_cycle_sp = dc

    #     sleep(0.1)
        
         

    # Stop the motors before exiting.
    #for m in robot.motors:
    #   m.stop()
    
           

    #debug_print('Test')
    

    time.sleep(5) 


if __name__ == '__main__':
    main()
    #debug_print('Hello VS Code!')

    #robot = drive.DiffRobot()
    #shovel = moveShovel.Shovel()

    #t = Thread(target=shovel.moveShovel())
    #ts = Thread(target=robot.go_backwards())
    #t.start()
    #ts.start()
    #t.join()
    #ts.join()
