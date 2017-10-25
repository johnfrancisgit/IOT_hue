import RPi.GPIO as GPIO

from time import sleep
from termcolor import import colored

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

while True:
    message = colored('On', 'green') if GPIO.input(4) == 0 else colored('Off', 'red')
    print(message)
    sleep(1)
