import RPi.GPIO as GPIO
from time import sleep
from termcolor import colored

class Sensor(object):
    def setup():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4,GPIO.IN)

    def get_status(debug=False):
        if debug:
            message = colored('On', 'green') if GPIO.input(4) == 0 else colored('Off', 'red')
            print(message)
            sleep(1)
        return GPIO.input(4)

    def tear_down():
        GPIO.cleanup()

