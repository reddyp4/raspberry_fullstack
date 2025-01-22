#program to control LED based on button
import RPi.GPIO as GPIO
import time

inPin = 8
ledPin = 7

GPIO.setwarnings(False)     ## Turn off warnings
GPIO.setmode(GPIO.BOARD)    ## Use BOARD pin numbering
GPIO.setup(inPin, GPIO.IN)  ## Set pin 8 to input
GPIO.setup(ledPin, GPIO.OUT)## Set pin 7 to output
while True:
    value = GPIO.input(inPin)   ## Read input from switch
    print(value)
    if value:
        print("Pressed")
        GPIO.output(ledPin, GPIO.HIGH)  ## Turn LED on
    else:
        print("Not Pressed")
        GPIO.output(ledPin, GPIO.LOW)   ## Turn LED off
    time.sleep(0.1)

GPIO.cleanup()
