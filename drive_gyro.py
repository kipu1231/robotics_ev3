#!/usr/bin/env python3

from ev3dev2.auto import LargeMotor,MoveSteering, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, GyroSensor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from time import sleep
PI = 3.141592653589793

def debug_print(*args, **kwargs):
    '''Print debug messages to stderr. This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)

class Drive_gyro(object):
    """docstring for DiffRobot"""
    def __init__(self, r_address=OUTPUT_A, l_address=OUTPUT_B):
        super(Drive_gyro, self).__init__()
        #self.motors = LargeMotor(r_address)
        #self.tank_pair = MoveTank(r_address, l_address)
        self.steer_pair = MoveSteering(r_address, l_address)
        self.gs = GyroSensor()
       
    
    def driveGyro(self):
        while True:
            angle = self.gs.value()
            debug_print(angle)
            # if angle >=-100 and angle<=100:
            #     self.steer_pair.on_for_rotations(angle, speed=30, rotations=10)
            #     self.steer_pair.off()
            sleep(4)
        #self.motors.on_for_degrees(speed=70, degrees=-120, brake=True, block=True)
        #sleep(1)
        #self.motors.on_for_degrees(speed=20, degrees=120, brake=True, block=True)

    
        #self.motors.on_for_degrees(speed=70, degrees=-120, brake=True, block=True)
        #sleep(1)
        #self.motors.on_for_degrees(speed=20, degrees=120, brake=True, block=True)

        #self.motors.on_for_degrees(speed=70, degrees=-120, brake=True, block=True)
        #sleep(1)
        #self.motors.on_for_degrees(speed=20, degrees=120, brake=True, block=True)
       
       
       #i = 3

        #while i > 0:
            
       
        #i = i-1
    
if __name__ == '__main__':
    gyro = Drive_gyro()
    gyro.driveGyro()