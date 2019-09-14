from django.db import models


class Setting(models.Model):
    setting_name = models.CharField(max_length=20, unique=True)
    value = models.IntegerField()

    def __str__(self):
        return str(self.setting_name) + ' - value: ' + str(self.value)

    
# Create your models here.
