#!/usr/bin/env python3

from ev3dev2.auto import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, UltrasonicSensor
from time import sleep
from random import choice, randint

import os
import sys

PI = 3.141592653589793

def debug_print(*args, **kwargs):
    '''Print debug messages to stderr. This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)

class DiffRobot(object):
    """docstring for DiffRobot"""
    def __init__(self, diam=56, width=28, r_address=OUTPUT_A, l_address=OUTPUT_B):
        super(DiffRobot, self).__init__()
        self.diam = diam
        self.width = width
        self.motors = [LargeMotor(address) for address in (r_address, l_address)]
        self.reset_position()
        #self.infrared = UltrasonicSensor(address = '1')
        #self.infrared_side = UltrasonicSensor(address = '2')

        # Put the infrared sensor into proximity mode.
        #self.infrared.mode = 'US-DIST-CM'
        #self.infrared_side.mode = 'US-DIST-CM'

    def start(self):
        for m in self.motors:
            m.run_forever()
    
    def backup(self):
        # Sound backup alarm.
        Sound.tone([(1000, 500, 500)] * 3)

        # Stop both motors and reverse for 1.5 seconds.
        # `run-timed` command will return immediately, so we will have to wait
        # until both motors are stopped before continuing.
        for m in self.motors:
            m.stop(stop_action='brake')
            m.run_timed(speed_sp=-500, time_sp=1500)

        # When motor is stopped, its `state` attribute returns empty list.
        # Wait until both motors are stopped:
        while any(m.state for m in self.motors):
            sleep(0.1)

    def turn(self):

        # We want to turn the robot wheels in opposite directions from 1/4 to 3/4
        # of a second. Use `random.choice()` to decide which wheel will turn which
        # way.
        power = choice([(1, -1), (-1, 1)])
        t = randint(250, 750)

        for m, p in zip(self.motors, power):
            m.run_timed(speed_sp=p*500, time_sp=t)

        # Wait until both motors are stopped:
        while any(m.state for m in self.motors):
            sleep(0.1)


    def go_forward(self, distance=None, dc=60):
        print("[INFO] Moving forward...")
        debug_print("[INFO] Moving forward...")
        if distance != None:

            turns = distance/(self.diam * PI)

            for m in self.motors:
                m.duty_cycle_sp = dc
                m.position_sp = turns*360
                m.run_to_rel_pos()
            while 'running' in self.motors[0].state: sleep(0.01)

        else: 
            for m in self.motors:
                m.duty_cycle_sp = dc
                m.run_direct()

    def go_backwards(self, distance=None, dc=60):
        if distance != None: distance = -distance
        self.go_forward(distance, -dc)

    def turn_left(self, angle=None, dc=60):
        
        if angle != None:

            turns_per_spin = self.width/self.diam
            turns = (angle/360.0) * turns_per_spin

            for m in self.motors:
                m.duty_cycle_sp = dc
                m.position_sp = turns*360
                m.run_to_rel_pos()
                dc = -dc
                turns = -turns
            while 'running' in self.motors[0].state: sleep(0.01)

        else:
            for m in self.motors:
                m.duty_cycle_sp = dc
                m.run_direct()
                dc = -dc

    def turn_right(self, angle=None, dc=60):
        if angle != None: angle = -angle
        self.turn_left(angle, -dc)

    def stop(self):
        for m in self.motors:
            m.stop()

    def reset_position(self):
        for m in self.motors:
            m.position = 0