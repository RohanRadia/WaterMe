import RPi.GPIO as GPIO
import time

channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

while True:
    if GPIO.input(channel):
        print('No Water Detected')
    else:
        print('Water Detected')

    time.sleep(1)
