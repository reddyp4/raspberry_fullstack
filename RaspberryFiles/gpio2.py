import RPi.GPIO as GPIO

pin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.HIGH)
GPIO.output(pin, GPIO.LOW)
GPIO.output(pin, GPIO.HIGH)
GPIO.output(pin, GPIO.LOW)
