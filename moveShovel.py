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
        self.shovel_up = 0
       
    
    def moveShovel(self):
        self.motors.on_for_degrees(speed=10, degrees=-40, brake=True, block=True)
        sleep(1)
        self.motors.on_for_degrees(speed=80, degrees=-100, brake=True, block=True)
        sleep(1)
        self.motors.on_for_degrees(speed=20, degrees=140, brake=True, block=True)
    
    def moveShovel_Up(self):
        if self.shovel_up == 0:
            self.motors.on_for_degrees(speed=80, degrees=-140, brake=True, block=True)
            self.shovel_up = 1
            sleep(0.5)
    
    def moveShovel_Down(self):
        if self.shovel_up == 1:
            self.motors.on_for_degrees(speed=50, degrees=140, brake=True, block=True)
            self.shovel_up = 0
            sleep(0.5)
        #self.motors.on_for_degrees(speed=70, degrees=-120, brake=True, block=True)
        #sleep(1)
        #self.motors.on_for_degrees(speed=20, degrees=120, brake=True, block=True)

        #self.motors.on_for_degrees(speed=70, degrees=-120, brake=True, block=True)
        #sleep(1)
        #self.motors.on_for_degrees(speed=20, degrees=120, brake=True, block=True)
       
       
       #i = 3

        #while i > 0:
            
       
        #i = i-1
    