from rest_framework import serializers
from eb.models import *

class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = ['setting_name', 'value']
    