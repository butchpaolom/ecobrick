from django.http import JsonResponse
from django.shortcuts import HttpResponse, redirect, render
from eb.models import *
from eb.serializer import *

def update_settings(request):
    try:
        if request.method == 'POST':
            setting = request.POST['setting']
            value = request.POST['value']
            if setting == 'switch':
                machine_switch = Setting.objects.get(setting_name='machine_switch')
                machine_switch.value = value 
                machine_switch.save()
                print(machine_switch.value)
            elif setting == 'compressor_trigger':
                compressor_trigger = Setting.objects.get(setting_name='compressor_trigger')
                compressor_trigger.value = value 
                compressor_trigger.save()
            elif setting == 'bottle_size':
                bottle_size = Setting.objects.get(setting_name='bottle_size')
                bottle_size.value = value 
                bottle_size.save()
        print(str(setting) + ' new value: ' + value )       
        success = True
    except:
        success = False
        setting = None
        value = None
    
    data = {
        "success": success,
        "setting": setting,
        "value": value,
    }

    return JsonResponse(data)

def get_settings(request):
    if request.method == 'GET':
        settings = Setting.objects.all()
        data = SettingSerializer(settings, many=True)

    return JsonResponse(data.data, safe=False)
