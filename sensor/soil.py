import RPi.GPIO as GPIO
import time


def monitor():
    channel = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.IN)

    if GPIO.input(channel):
        pass
        return("1")
        time.sleep(1)
    else:
        time.sleep(1)
        return("0")
