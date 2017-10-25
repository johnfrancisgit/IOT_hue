#!/usr/bin/python

from phue import Bridge
from main import Sensor

b = Bridge('tobedefined')
b.connect()
b.get_api()
try:
    Sensor.setup()
    debug = (sys.argv(1) == 'debug')
    old_light = true
    while True:
        light = Sensor.get_status(debug)
        if old_light != light:
            if !Sensor.get_status(debug):
                command =  {'transitiontime' : 50, 'on' : True, 'bri' : 254}
                b.set_light(1, command)
            else:
                command =  {'transitiontime' : 50, 'on' : False, 'bri' : 254}
                b.set_light(1, command)
        old_light = light



finally:
    Sensor.tear_down()
