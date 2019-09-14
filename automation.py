import sys, os
import django
import time
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecobrick.settings")
django.setup()

from eb.models import *

#model is 'Setting'
#automation for ecobrick is written here, from settings.


while (True):
    try:
        x = Setting.objects.get(setting_name='machine_switch')
    except:
        x = None
    print (x)
    time.sleep(.3)