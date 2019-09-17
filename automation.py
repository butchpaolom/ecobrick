import sys, os
import django
import time
import RPi.GPIO as rl

EMULATE_HX711=False

referenceUnit = -125

if not EMULATE_HX711:
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

hx = HX711(5, 6)
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(referenceUnit)
hx.reset()
hx.tare()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecobrick.settings")
django.setup()

from eb.models import *

#model is 'Setting'
#automation for ecobrick is written here, from settings.
compressor = 31 #pin 31 compressor (in4)
wiper = 33      #pin 33 wiper
shredder = 35   #pin 35 shredder 
extra_pin = 37

rl.setmode(rl.BOARD)
rl.setup(compressor,rl.OUT)
rl.setup(wiper,rl.OUT) 
rl.setup(shredder,rl.OUT) 
rl.setup(extra_pin,rl.OUT) 

rl.setup(compressor,rl.HIGH)
rl.setup(wiper,rl.HIGH)
rl.setup(shredder,rl.HIGH)
rl.setup(extra_pin,rl.HIGH)

seconds = 0


while True:
    val = max(0, int(hx.get_weight(5))) #get loadcell value
    hx.power_down()
    hx.power_up()
    try:
        ms = Setting.objects.get(setting_name='machine_switch')
    except:
        ms = None
    try:
        ct = Setting.objects.get(setting_name='compressor_trigger') #time to trigger compressor in seconds
    except:
        ct = None
    try:
        bs = Setting.objects.get(setting_name='bottle_size')
    except:
        bs = None
    while ms.value==1 and val < bs.value*0.33:
        rl.setup(shredder,rl.LOW) #might put if statement if shredder is turned on
        rl.setup(wiper,rl.LOW) #same to this one
        try:
            ms = Setting.objects.get(setting_name='machine_switch')
        except:
            ms = None
        try:
            ct = Setting.objects.get(setting_name='compressor_trigger') #time to trigger compressor in seconds
        except:
            ct = None
        try:
            bs = Setting.objects.get(setting_name='bottle_size')
        except:
            bs = None
        print (ms)
        print (str(ct) + " (" + str(int(seconds))+ ")")
        print (str(bs.value*.33) + " current grams: " + str(val))
        if int(seconds) >= ct.value:
            rl.setup(compressor,rl.LOW)
            time.sleep(2)
            rl.setup(compressor,rl.HIGH)
            seconds = 0
        else:
            val = max(0, int(hx.get_weight(5)))
            hx.power_down()
            hx.power_up()
            time.sleep(0.2)
            seconds = seconds + 0.2
    if ms.value==0:
        rl.setup(shredder,rl.HIGH) 
        rl.setup(wiper,rl.HIGH)


