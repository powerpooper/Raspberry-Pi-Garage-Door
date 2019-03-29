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
except:
    print

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

def quit_gracefully(*args):
	print ("")
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

if __name__ == "__main__":
	# Cleanup
	signal.signal(signal.SIGINT, quit_gracefully)

	try:

		while True:
			input_state = GPIO.input(24)
			if input_state == False:
				print('Closed')
				time.sleep(1)
				os.system('cls' if os.name == 'nt' else 'clear')

			if input_state == True:
				print('Open')
				time.sleep(1)
				os.system('cls' if os.name == 'nt' else 'clear')

			pass

	except KeyboardInterrupt:
		if quit_gracefully():
			print("Done \n")

