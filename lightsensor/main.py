#!/usr/bin/python

import sys

from time import sleep
from phue import Bridge, PhueRegistrationException
from state import Sensor

BRIDGE_WAIT = 30  # seconds

def connect_to_bridge():
    """ Connect a phue bridge object
    """
    try:
        b = Bridge('192.168.1.3')
        b.connect()
        return b
    except PhueRegistrationException:
        return False

for i in range(BRIDGE_WAIT):
    print("Please press the button on the hue bridge to connect")
    sleep(1)
    BRIDGE_WAIT -= 1
    if BRIDGE_WAIT > 0:
        print("Time remaining: {} seconds".format(BRIDGE_WAIT))
        b = connect_to_bridge()
        if b:
            print("Bridge successfully connected")
            break
        else:
            continue
    else:
         print("Couldn't connect. The button wasn't pressed in time")
         sys.exit(1)

b.get_api()

try:
    Sensor.setup()
    debug = False 
    old_light = True
    while True:
        sleep(1)
        light = Sensor.get_status(debug)
        light_state = b.get_light(1, 'on')
        print("light sensor is: {}".format(light))
        print("light is: {}".format(light_state))
        if light_state != int(light):
            if light_state == 0:
                command =  {'transitiontime' : 50, 'on' : True, 'bri' : 254}
                b.set_light(1, 'on', True)
            else:
                command =  {'transitiontime' : 50, 'on' : False, 'bri' : 254}
                b.set_light(1, 'on', False)
        old_light = light



finally:
    Sensor.tear_down()




