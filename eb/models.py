from django.db import models


class Setting(models.Model):
    setting_name = models.CharField(max_length=20, unique=True)
    value = models.IntegerField()

    def __str__(self):
        return str(self.setting_name) + ' - value: ' + str(self.value)

class Sensor(models.Model):
    weight = models.IntegerField()

    def __str__(self):
        return "current weight: " + str(self.weight)
    
# Create your models here.
