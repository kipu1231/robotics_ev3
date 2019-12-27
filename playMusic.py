#!/usr/bin/env python3

from ev3dev2.auto import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from time import sleep
from ev3dev2.sound import Sound
PI = 3.141592653589793

class Music(object):
    """docstring for DiffRobot"""
    def __init__(self, r_address=OUTPUT_C):
        super(Music, self).__init__()
        self.sound = Sound()
       
    #fuerElise is already in another foulder on the robot. maybe we dont have to download it every time now.
    #  Change code therefore and maybe folder
    def playMusic(self):
        self.sound.play_file('/home/robot/robotics_ev3/Sounds/short_fuerElise.wav') 
        self.sound.beep()