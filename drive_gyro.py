#!/usr/bin/env python3

from ev3dev2.auto import LargeMotor,MoveSteering, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, GyroSensor, UltrasonicSensor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from time import sleep
import time
import sys
import moveShovel 
PI = 3.141592653589793
THRESHOLD = 200

def debug_print(*args, **kwargs):
    '''Print debug messages to stderr. This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)

class Drive_gyro(object):
    """docstring for DiffRobot"""
    def __init__(self, shovel, diam=56, width=28, r_address=OUTPUT_A, l_address=OUTPUT_B):
        super(Drive_gyro, self).__init__()
        self.diam = diam
        self.width = width
        self.motors = [LargeMotor(address) for address in (r_address, l_address)]
        self.tank_pair = MoveTank(r_address, l_address)
        self.steer_pair = MoveSteering(r_address, l_address)
        self.gs = GyroSensor()
        self.gs.mode = 'GYRO-RATE'
        self.gs.mode = 'GYRO-ANG'
        self.shovel = shovel
        self.current_angle = self.gs.value()
        ultrasonic_sensor = UltrasonicSensor()
        ultrasonic_sensor.mode = 'US-DIST-CM'
        self.ultrasonic_sensor = ultrasonic_sensor
        
    
    def driveGyro(self,distance=None, dc=40, target=None):
        debug_print("[INFO] Moving forward...")
        self.shovel.moveShovel_Down()
        angle = self.gs.value()
        # debug_print(angle)
        if distance != None:
            turns = distance/(self  .diam * PI)
            # debug_print(turns)
            now = time.time()
            future = now + 2.5
            while time.time() < future:
                angle2 = self.gs.value()
                # distance = self.ultrasonic_sensor.value()
                # if distance < THRESHOLD:
                #     break
                angle_drive = angle2-angle
                self.steer_pair.on(angle_drive, speed=dc)
            self.steer_pair.off()
            
        
    def turn_left(self,degree=89):
        debug_print("[INFO] Turn left ...")
        self.shovel.moveShovel_Up()
        self.current_angle -= degree
        while self.gs.value() > self.current_angle:
            diff = self.gs.value() - self.current_angle
            self.steer_pair.on(-100, speed = -diff)
        #debug_print(self.gs.value())
        self.steer_pair.off()

    def turn_right(self, degree=89):
        debug_print("[INFO] Turn right ...")
        self.shovel.moveShovel_Up()
        self.current_angle += degree
        while self.gs.value() < self.current_angle:
            diff = self.current_angle - self.gs.value()
            self.steer_pair.on(100, speed = -diff)
        #debug_print(self.gs.value())
        self.steer_pair.off()


    def test(self):
        while True:
            distance = self.ultrasonic_sensor.value()
            debug_print(distance)
            sleep(3)

            # def go_forward(self, distance=None, dc=60):
    #     print("[INFO] Moving forward...")
    #     debug_print("[INFO] Moving forward...")
        
    #     if distance != None:
    #         turns = distance/(self.diam * PI)
    #         for m in self.motors:
    #             m.duty_cycle_sp = dc
    #             m.position_sp = turns*360
    #             m.run_to_rel_pos()
    #             m.run_to_rel_pos(position_sp = turns*360, speed_sp=200)
    #         while 'running' in self.motors[0].state: 
                
    #             sleep(0.01)
    #     else: 
    #         for m in self.motors:
    #             m.duty_cycle_sp = dc
    #             m.run_direct()

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