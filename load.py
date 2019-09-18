#! /usr/bin/python2

import time
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecobrick.settings")
django.setup()

from eb.models import *
weight,created = Sensor.objects.get_or_create(weight=0)
EMULATE_HX711=False

referenceUnit = -115

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

def cleanAndExit():
    print("Cleaning...")

    if not EMULATE_HX711:
        GPIO.cleanup()
        
    print("Bye!")
    sys.exit()

hx = HX711(10, 9)
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(referenceUnit)

hx.reset()

hx.tare()

print("Tare done! Add weight now...")
while True:
    try:
        val = max(0, int(hx.get_weight(5)))
        print(val)
        weight.weight=val
        weight.save()
        hx.power_down()
        hx.power_up()
        time.sleep(0.1)

    except (KeyboardInterrupt, SystemExit):
        weight.weight=0
        weight.save()
        cleanAndExit()
