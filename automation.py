import sys, os
import django
import time
import RPi.GPIO as rl
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecobrick.settings")
django.setup()

from eb.models import *

#model is 'Setting'
#automation for ecobrick is written here, from settings.
compressor = 31 #pin 31 compressor
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

ms=0
ct=0
bs=0

def update():
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
    print (ct)
    print (bs)

while True:
    update()
    while ms.value==1:
        update()
        if int(seconds) == ct.value:
            rl.setup(compressor,rl.LOW)
            time.sleep(2)
            rl.setup(compressor,rl.HIGH)
            seconds = 0
        else:
            seconds = seconds + 0.2
        time.sleep(0.2)

