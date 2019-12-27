#!/usr/bin/env python3

from ev3dev2.auto import LargeMotor,MoveSteering, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, GyroSensor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from time import sleep
import sys
PI = 3.141592653589793

def debug_print(*args, **kwargs):
    '''Print debug messages to stderr. This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)

class Drive_gyro(object):
    """docstring for DiffRobot"""
    def __init__(self, diam=56, width=28, r_address=OUTPUT_A, l_address=OUTPUT_B):
        super(Drive_gyro, self).__init__()
        self.motors = [LargeMotor(address) for address in (r_address, l_address)]
        self.tank_pair = MoveTank(r_address, l_address)
        self.steer_pair = MoveSteering(r_address, l_address)
        self.gs = GyroSensor()
        self.gs.mode = 'GYRO-RATE'
        self.gs.mode = 'GYRO-ANG'
        # self.gs.reset()
    
    def driveGyro(self):
        self.gs.reset()
        while True:
            angle = self.gs.value()
            debug_print(angle)
            # if angle >=-100 and angle<=100:
            #     self.steer_pair.on_for_rotations(angle, speed=30, rotations=10)
            #     self.steer_pair.off()
            sleep(2)

    def go_forward(self, distance=None, dc=60):
        print("[INFO] Moving forward...")
        debug_print("[INFO] Moving forward...")
        
        if distance != None:
            turns = distance/(self.diam * PI)
            for m in self.motors:
                m.duty_cycle_sp = dc
                m.position_sp = turns*360
                m.run_to_rel_pos()
            while 'running' in self.motors[0].state: 
                
                sleep(0.01)
        else: 
            for m in self.motors:
                m.duty_cycle_sp = dc
                m.run_direct()
        
    def turnLeft_Gyro(self,degree=90):
        angle = self.gs.value() - degree
        while self.gs.value() > angle:
            diff = self.gs.value() - angle
            self.steer_pair.on(-100, speed = -diff)
        debug_print(self.gs.value())
        self.steer_pair.off()

    def turnRight_Gyro(self, degree=90):
        angle = self.gs.value() + degree
        while self.gs.value() < angle:
            diff = angle - self.gs.value()
            self.steer_pair.on(100, speed = -diff)
        debug_print(self.gs.value())
        self.steer_pair.off()





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