#code for reading button
import RPi.GPIO as GPIO
import time
inPin = 8

GPIO.setwarnings(False)		## Switch connected to pin 8
GPIO.setmode(GPIO.BOARD)	## Turn off warnings
GPIO.setup(inPin, GPIO.IN)	## Set pin 8 to input
while True:
   value = GPIO.input(inPin)	## Read input
   if value:
	print("Pressed")
   else:
	print("Not Pressed")
   time.sleep(0.1)

GPIO.cleanup()
