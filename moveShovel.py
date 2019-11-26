#!/usr/bin/env python3

from ev3dev2.auto import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from time import sleep
PI = 3.141592653589793

class Shovel(object):
    """docstring for DiffRobot"""
    def __init__(self, r_address=OUTPUT_C):
        super(Shovel, self).__init__()
        self.motors = LargeMotor(r_address)
       
    
    def moveShovel(self):
        self.motors.on_for_degrees(speed=70, degrees=-120, brake=True, block=True)
        sleep(1)
        self.motors.on_for_degrees(speed=20, degrees=120, brake=True, block=True)
    