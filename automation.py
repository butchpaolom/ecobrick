import sys, os
import django
import time
import RPi.GPIO as rl
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecobrick.settings")
django.setup()

from eb.models import *

#model is 'Setting'
#automation for ecobrick is written here, from settings.
rl.setmode(rl.BOARD)
rl.setup(33,rl.OUT)
rl.setup(35,rl.OUT)
rl.setup(37,rl.OUT)
rl.setup(31,rl.OUT)
rl.setup(33,rl.HIGH)
rl.setup(35,rl.HIGH)
rl.setup(37,rl.HIGH)
rl.setup(31,rl.HIGH)


while (True):
    try:
        ms = Setting.objects.get(setting_name='machine_switch')
    except:
        ms = None
    try:
        ct = Setting.objects.get(setting_name='compressor_trigger')
    except:
        ct = None
    try:
        bs = Setting.objects.get(setting_name='bottle_size')
    except:
        bs = None
    if ms.value==1:
        rl.setup(33,rl.LOW)
        rl.setup(35,rl.LOW)
        rl.setup(37,rl.LOW)
        rl.setup(31,rl.LOW)
    else:
        rl.setup(33,rl.HIGH)
        rl.setup(35,rl.HIGH)
        rl.setup(37,rl.HIGH)
        rl.setup(31,rl.HIGH)
    print (ms)
    print (ct)
    print (bs)
    time.sleep(.3)