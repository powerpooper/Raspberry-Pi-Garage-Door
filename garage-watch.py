import RPi.GPIO as GPIO
import time
import sys
import getopt
import os
import signal
import argparse
import gc
import datetime
import string
import subprocess
import re
import fileinput
import ConfigParser

var=1
counter = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')


def now_rising(channel):

	if GPIO.input(24) == 0:
		os.system('smartthings_cli set contact \'Garage Door\' close')

	if GPIO.input(24) == 1:
		os.system('smartthings_cli set contact \'Garage Door\' open')


#GPIO.add_event_detect(24, GPIO.RISING, callback=now_rising, bouncetime=500)
GPIO.add_event_detect(24, GPIO.RISING, callback=now_rising)

# you can continue doing other stuff here
while True:
    time.sleep(0.02)
    pass
