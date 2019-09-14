from django.shortcuts import render, redirect
from eb.models import *


# Create your views here.



def index(request):
    def_settings_check_add()
    return render(request, 'index.html')


def controller_view(request):
    return render(request, 'controller.html')

def def_settings_check_add():
    try:
        bot_sz = Setting.objects.get(setting_name='bottle_size')
    except:
        bot_sz = None
    try:
        com_tr = Setting.objects.get(setting_name='compressor_trigger')
    except:
        com_tr = None
    try:
        on_off = Setting.objects.get(setting_name='machine_switch')
    except:
        on_off = None

    if on_off or com_tr or bot_sz is None:
        try:
            bottle_size = Setting(setting_name='bottle_size', value=1500) #default is 1.5 liters
            bottle_size.save() 
        except:
            pass
        try:
            machine_switch = Setting(setting_name='machine_switch', value=1) #default is turned on
            machine_switch.save()
        except:
            pass
        try:
            compressor_trigger = Setting(setting_name='compressor_trigger', value=300) #default is 5 mins
            compressor_trigger.save()  
        except:
            pass


