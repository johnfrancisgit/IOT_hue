import RPi.GPIO as GPIO

from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

while True:
    message = True if GPIO.input(4) == 0 else False
    print(message)
    sleep(1)
