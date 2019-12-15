#!/usr/bin/env python3

# In this demo an Explor3r robot with touch sensor attachment drives
# autonomously. It drives forward until an obstacle is bumped (determined by
# the touch sensor), then turns in a random direction and continues. The robot
# slows down when it senses obstacle ahead (with the infrared sensor).
#
# The program may be stopped by pressing any button on the brick.
#
# This demonstrates usage of motors, sound, sensors, buttons, and leds.

from time   import sleep
from random import choice, randint

from ev3dev.ev3 import *

# Connect two large motors on output ports B and C:
motors = [LargeMotor(address) for address in (OUTPUT_B, OUTPUT_C)]

# Connect infrared and touch sensors.
ir = InfraredSensor()
ts = TouchSensor()

# Put the infrared sensor into proximity mode.
ir.mode = 'IR-PROX'

# We will need to check EV3 buttons state.
# btn = Button()   NOT WORKING

def start():
    """
    Start both motors. `run_forever` command will allow to vary motor
    performance on the fly by adjusting `speed_sp` attribute.
    """
    for m in motors:
        m.run_forever()

def backup():
    """
    Back away from an obstacle.
    """

    # Sound backup alarm.
    Sound.tone([(1000, 500, 500)] * 3)

    # Turn backup lights on:
    for light in (Leds.LEFT, Leds.RIGHT):
        Leds.set_color(light, Leds.RED)

    # Stop both motors and reverse for 1.5 seconds.
    # `run-timed` command will return immediately, so we will have to wait
    # until both motors are stopped before continuing.
    for m in motors:
        m.stop(stop_action='brake')
        m.run_timed(speed_sp=-500, time_sp=1500)

    # When motor is stopped, its `state` attribute returns empty list.
    # Wait until both motors are stopped:
    while any(m.state for m in motors):
        sleep(0.1)

    # Turn backup lights off:
    for light in (Leds.LEFT, Leds.RIGHT):
        Leds.set_color(light, Leds.GREEN)

def turn():
    """
    Turn the robot in random direction.
    """

    # We want to turn the robot wheels in opposite directions from 1/4 to 3/4
    # of a second. Use `random.choice()` to decide which wheel will turn which
    # way.
    power = choice([(1, -1), (-1, 1)])
    t = randint(250, 750)

    for m, p in zip(motors, power):
        m.run_timed(speed_sp=p*500, time_sp=t)

    # Wait until both motors are stopped:
    while any(m.state for m in motors):
        sleep(0.1)

# Run the robot until a button is pressed.
start()
# while not btn.any():   NOT WORKING
while True:    # Stop program with Ctrl-C
    if ts.value():
        # We bumped an obstacle.
        # Back away, turn and go in other direction.
        backup()
        turn()
        start()

    # Infrared sensor in proximity mode will measure distance to the closest
    # object in front of it.
    distance = ir.value()

    if distance > 60:
        # Path is clear, run at full speed.
        dc = 90
    else:
        # Obstacle ahead, slow down.
        dc = 40

    for m in motors:
        m.speed_sp = dc

    sleep(0.1)

# Stop the motors before exiting.
for m in motors:
    m.stop()