#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_StepperMotor #, Adafruit_DCMotor, Adafruit_StepperMotor

from math import pi
from sys import exit
from time import sleep, time
from datetime import datetime
import atexit

spool_radius = 3 #cm
shield_length = 20 #cm
overshoot = 5 #cm

def ynExit():
	response = raw_input("Would you like to continue? ")
	response = response.lower()
	if response == 'y' or response == 'yes':
		return
	elif response == 'n' or response == 'no':
		exit()
	else:
		print "Invalid response; try again"
		ynExit()

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT()

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

myStepper = mh.getStepper(200, 1)  	# 200 steps/rev, motor port #1
myStepper.setSpeed(2)  		# RPM

def runInShield():
    runCycle(615)

def runCycle(steps):
    print "Starting motor cycle at", datetime.fromtimestamp(time()).strftime('%H:%M:%S')

    myStepper.step(steps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.MICROSTEP)
    sleep(2.5)
    print "Center of cycle at", datetime.fromtimestamp(time()).strftime('%H:%M:%S')
    sleep(2.5)
    myStepper.step(steps, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
    print "Stopping motor cycle at", datetime.fromtimestamp(time()).strftime('%H:%M:%S')
    turnOffMotors()

