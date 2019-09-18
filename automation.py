import sys, os
import django
import time
import RPi.GPIO as rl

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecobrick.settings")
django.setup()

from eb.models import *

#model is 'Setting'
#automation for ecobrick is written here, from settings.
compressor = 40 #pin 40 compressor (in4)
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
    try:
        print(ms)
        time.sleep(0.3)
        weight = Sensor.objects.first()
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
        while ms.value==1 and bs.value*(0.33) > weight.weight:
            weight = Sensor.objects.first()
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
            print (str(bs) + " current ml is: " + str(int(weight.weight/0.33)))
            if int(seconds) >= ct.value:
                rl.setup(compressor,rl.LOW)
                time.sleep(2)
                rl.setup(compressor,rl.HIGH)
                seconds = 0
            else:
                time.sleep(0.2)
                seconds = seconds + 0.2
        if ms.value==1 and bs.value*(0.33) < weight.weight:
            rl.setup(shredder,rl.HIGH) 
            rl.setup(wiper,rl.HIGH)
            time.sleep(5)
            ms.value = 0
            ms.save()
        if ms.value==0:
            rl.setup(shredder,rl.HIGH) 
            rl.setup(wiper,rl.HIGH)
    except (KeyboardInterrupt, SystemExit):
        rl.cleanup()
        print("GPIO CLEANED")


