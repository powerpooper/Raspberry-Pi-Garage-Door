import RPi.GPIO as GPIO
from doorvar import *
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

try:
   file_name =  os.path.basename(sys.argv[0])
   garagedoor = sys.argv[1]
   action = sys.argv[2]
except:
    print

GPIO.setmode(GPIO.BCM)
#chan_list = [22,27]
#GPIO.setup(chan_list, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

def quit_gracefully(*args):
	sys.exit(0)

def updateDoorStatus():
        newDoorstate = str(doorstate)
        with open("/home/pi/script-testing/doorvar.py") as f:
                for line in f:
                        if "doorstate =" in line:
                                curval=line
                                s = open("/home/pi/script-testing/doorvar.py").read()
                                s = s.replace('%s' % curval, "doorstate = " + newDoorstate + "\n")
                                f = open("/home/pi/script-testing/doorvar.py", 'w')
                                f.write(s)
                                f.close()
	return newDoorstate

def htmlUpdate():
	newstate = currentstate
	with open('/var/www/html/garagedoor.html') as f:
		for line in f:
			curval=line
			s = open('/var/www/html/garagedoor.html').read()
			s = s.replace('%s' % curval, newstate + "\n")
			f = open('/var/www/html/garagedoor.html', 'w')
			f.write(s)
			f.close

def garageDoor():
	# On
	GPIO.output(27,0)
	time.sleep(0.2)

	# Off
	GPIO.output(27,1)
	time.sleep(0.2)

if __name__ == "__main__":

	input_state = GPIO.input(24)
	# Open
	if action == "open":
		if input_state == False:
			garageDoor()
			currentstate = "Closed"
			if input_state != doorstate:
				doorstate = not doorstate
				updateDoorStatus()
				htmlUpdate()

	# Close
	if action == "close":
		if input_state == True:
			garageDoor()
			currentstate = "Open"
			if input_state != doorstate:
				doorstate = not doorstate
				updateDoorStatus()
				htmlUpdate()
	GPIO.cleanup()
