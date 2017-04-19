# Python 2 library for running interactions with the virtual machine
# all VM interactions are done with mouse + key controls using xdotool
# don't move the mouse while it's going
# also all of them start with the mouse on the middle of the start button logo, # at (503, 519), with the vm window not focused

from os import system
from time import sleep

def saveInputs(): 
    system('vmcontrols/savein1')
    sleep(60)
    system('vmcontrols/savein2')
    sleep(30)

def startSpectramag6():
    system('vmcontrols/startsm6')
    sleep(5)

def hostClearTransferDir():
    system('rm -f /home/gradio/transferdir/*')

def guestClearTransferDir():
    system('vmcontrols/cleartransferdir') 

def startTest():
    system('vmcontrols/startscan')
